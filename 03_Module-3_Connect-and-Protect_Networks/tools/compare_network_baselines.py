"""Compare two minimized Windows listener snapshots without network access.

Only TCP listeners and local UDP endpoints are compared. Neither a wildcard
bind nor a new listener proves remote reachability, exposure, or maliciousness.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

VALID_PROTOCOLS = {"tcp", "udp"}
VALID_SCOPES = {"loopback", "wildcard", "specific", "unknown"}
VALID_SOURCES = {"local-windows-readonly-collector", "synthetic-test-fixture"}
TOP_LEVEL_FIELDS = {"schema_version", "source", "captured_at_utc", "scope", "endpoints"}
ENDPOINT_FIELDS = {"protocol", "port", "bind_scope"}


def read_snapshot(path):
    with Path(path).open("r", encoding="utf-8-sig") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Snapshot must be a JSON object")
    if set(data) != TOP_LEVEL_FIELDS:
        raise ValueError("Snapshot has missing or unexpected fields; only minimized data is accepted")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("Unsupported snapshot schema_version")
    if data.get("source") not in VALID_SOURCES:
        raise ValueError("Unknown snapshot source")
    if data.get("scope") != "listening_tcp_and_local_udp_endpoints_only":
        raise ValueError("Unknown snapshot scope")

    stamp = data.get("captured_at_utc")
    if not isinstance(stamp, str):
        raise ValueError("Missing UTC collection timestamp")
    try:
        timestamp = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid collection timestamp") from exc
    if timestamp.tzinfo is None or timestamp.utcoffset().total_seconds() != 0:
        raise ValueError("Collection timestamp must be UTC")

    endpoints = data.get("endpoints")
    if not isinstance(endpoints, list):
        raise ValueError("endpoints must be an array")
    unique = set()
    for index, endpoint in enumerate(endpoints, 1):
        if not isinstance(endpoint, dict):
            raise ValueError(f"Endpoint {index} must be an object")
        if set(endpoint) != ENDPOINT_FIELDS:
            raise ValueError(f"Endpoint {index}: unexpected or missing fields")
        protocol = endpoint.get("protocol")
        port = endpoint.get("port")
        scope = endpoint.get("bind_scope")
        if protocol not in VALID_PROTOCOLS:
            raise ValueError(f"Endpoint {index}: unsupported protocol")
        if type(port) is not int or not (1 <= port <= 65535):
            raise ValueError(f"Endpoint {index}: invalid port")
        if scope not in VALID_SCOPES:
            raise ValueError(f"Endpoint {index}: invalid bind_scope")
        key = (protocol, port, scope)
        if key in unique:
            raise ValueError(f"Endpoint {index}: duplicate endpoint")
        unique.add(key)
    return {"timestamp": timestamp, "endpoints": unique, "source": data["source"]}


def describe(endpoint):
    protocol, port, scope = endpoint
    return {"protocol": protocol, "port": port, "bind_scope": scope}


def compare(before, after):
    """Return reproducible differences and a scope-change review list."""
    old, new = before["endpoints"], after["endpoints"]
    sort = lambda key: (key[0], key[1], key[2])
    old_pairs = {(protocol, port) for protocol, port, _ in old}
    new_pairs = {(protocol, port) for protocol, port, _ in new}
    scope_changes = []
    for protocol, port in sorted(old_pairs & new_pairs):
        prev = sorted(scope for p, n, scope in old if p == protocol and n == port)
        curr = sorted(scope for p, n, scope in new if p == protocol and n == port)
        if prev != curr:
            scope_changes.append({
                "protocol": protocol, "port": port,
                "before_scopes": prev, "after_scopes": curr,
            })
    return {
        "schema_version": 1,
        "comparison": "local_listening_endpoint_sets_only",
        "before_utc": before["timestamp"].isoformat(),
        "after_utc": after["timestamp"].isoformat(),
        "before_count": len(old),
        "after_count": len(new),
        "added": [describe(x) for x in sorted(new - old, key=sort)],
        "removed": [describe(x) for x in sorted(old - new, key=sort)],
        "scope_changes": scope_changes,
        "limitations": [
            "A wildcard bind does not prove external network reachability.",
            "A new listener is not automatically suspicious; verify its service and owner.",
            "Firewall, routing, process ownership, DNS and remote connections are not captured.",
            "Differences across restarts or changing networks may be normal.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", type=Path, required=True)
    parser.add_argument("--after", type=Path, required=True)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)
    try:
        before = read_snapshot(args.before)
        after = read_snapshot(args.after)
        if before["source"] != after["source"]:
            raise ValueError("Cannot compare synthetic and local evidence snapshots")
        if after["timestamp"] < before["timestamp"]:
            raise ValueError("--after snapshot predates --before snapshot")
        result = compare(before, after)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print("Local listener baseline comparison (read-only)")
    print(f"Before: {result['before_count']} endpoints")
    print(f"After: {result['after_count']} endpoints")
    for title, key in (("Added", "added"), ("Removed", "removed")):
        print(f"{title}: {len(result[key])}")
        for endpoint in result[key]:
            print(f"  {endpoint['protocol'].upper()} {endpoint['port']} "
                  f"({endpoint['bind_scope']})")
    print(f"Binding-scope changes: {len(result['scope_changes'])}")
    for change in result["scope_changes"]:
        print(f"  {change['protocol'].upper()} {change['port']}: "
              f"{','.join(change['before_scopes'])} -> "
              f"{','.join(change['after_scopes'])}")
    print("Requires service/firewall context; not proof of internet exposure.")


if __name__ == "__main__":
    main()
