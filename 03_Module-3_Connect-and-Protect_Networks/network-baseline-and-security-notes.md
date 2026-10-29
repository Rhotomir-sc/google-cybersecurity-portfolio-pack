# Network baseline — collection pending

**Status:** An offline comparison tool, a read-only Windows collection script, and synthetic test fixtures are available. **No real host baseline has been collected or verified for this repository.**

This exercise focuses on **local TCP listening endpoints and UDP bind endpoints**. It does not capture all traffic, prove internet exposure, or establish which process owns a port.

## 1. Collect two local snapshots (Windows)

Use **only a computer you own or are authorized to inspect**. Open Windows PowerShell 5.1 or newer (with the NetTCPIP cmdlets available), go to the repository root, and run:

```powershell
.\03_Module-3_Connect-and-Protect_Networks\tools\collect-network-baseline.ps1
```

The script:
- reads `Get-NetTCPConnection -State Listen` and `Get-NetUDPEndpoint` without changing any network or firewall settings;
- records protocol, port, and a coarse bind category: `loopback`, `wildcard`, `specific`, or `unknown`;
- records a UTC capture timestamp but **does not export** raw IP addresses, usernames, machine names, process IDs, DNS data, or remote connections;
- saves to a newly named **local file in the Windows temporary directory**, outside the repository.

The JSON parser enforces an explicit field allowlist. Files containing unexpected raw IP addresses, hostnames, process details, or other additional fields are rejected instead of silently processed. This validation reduces accidental exposure; it does not make a local snapshot automatically safe to publish.

Port numbers and bind information may still be sensitive. Review the output locally before sharing anything. If system policy prevents PowerShell script execution, respect that policy and use the manual review procedure below instead. Do not loosen security controls merely to produce portfolio evidence.

Repeat the command **later on the same authorized host**, ideally after a documented service or environment change. Save both printed output paths for the next step. Do **not** change firewall rules or open ports as part of this baseline exercise.

## 2. Compare the snapshots (Python 3.10+)

From the repository root, substitute the real paths printed by the collector:

```powershell
py .\03_Module-3_Connect-and-Protect_Networks\tools\compare_network_baselines.py --before "C:\path\to\first.json" --after "C:\path\to\second.json"
```

For a machine-readable comparison add `--format json`.

The comparator reports **added**, **removed**, and **changed binding-scope** entries. An endpoint changing from `loopback` to `wildcard` deserves review, but **wildcard binding alone is not proof that another computer can reach it**; host firewall, routing, and service context matter.

## 3. Reproduce the tests without touching a live network

The bundled examples are **synthetic** and intentionally separate from real host evidence:

```powershell
py .\03_Module-3_Connect-and-Protect_Networks\tools\compare_network_baselines.py --before .\03_Module-3_Connect-and-Protect_Networks\tests\fixtures\before.json --after .\03_Module-3_Connect-and-Protect_Networks\tests\fixtures\after.json

py -m unittest discover -s .\03_Module-3_Connect-and-Protect_Networks\tests -v
```

Expected synthetic changes: one new TCP port `5985` entry, and a TCP port `8000` bind-scope change from `loopback` to `wildcard`. These **do not** describe an actual system, incident, or discovered vulnerability.

## 4. Investigate unexpected endpoints locally

On the authorized Windows host, inspect a specific local listener and its process context:

```powershell
Get-NetTCPConnection -State Listen | Sort-Object LocalPort
Get-NetUDPEndpoint | Sort-Object LocalPort
Get-NetIPConfiguration
```

If needed, follow up locally using the port and owning process from `Get-NetTCPConnection`, then verify the service purpose, firewall profile/rule and expected network reachability through authorized testing. Never infer that a wildcard bind is directly reachable from the internet.

The `Get-NetIPConfiguration` output can contain local addresses, interface and DNS details; **do not upload unreviewed output or screenshots**. The privacy-minimized JSON intentionally omits those fields. No automatic network scanner, connection attempt, firewall modification or administrative change is part of these scripts.

## Evidence checklist (not completed yet)

| Required evidence | Current status |
|---|---|
| Host role / authorized environment, collection date and UTC timestamp | Awaiting actual host run |
| Two minimized snapshot files created on that host | Awaiting actual host run |
| Reproduced comparator output and explanation of any changes | Awaiting actual host run |
| Port/service/firewall context for an unexpected finding | Awaiting analyst review |
| Redaction/privacy inspection before committing evidence | Awaiting user review |
| Python synthetic-fixture comparison and automated tests | Available; verified by CI when green |

When you have a real capture, upload **only reviewed, permitted extracts** and write what the results actually support. Do not replace synthetic fixtures with live data. The source script is not proof that it was executed on an actual Windows host.

[Module overview](README.md) · [Evidence status](evidence/README.md) · [Artifact index](../ARTIFACTS.md)
