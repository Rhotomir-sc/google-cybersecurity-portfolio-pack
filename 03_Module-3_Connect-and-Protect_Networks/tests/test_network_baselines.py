"""Unit tests for the offline comparator; samples are synthetic, not live hosts."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "tools"))
from compare_network_baselines import read_snapshot, compare, main

FIXTURES = BASE / "tests" / "fixtures"


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.before = read_snapshot(FIXTURES / "before.json")
        self.after = read_snapshot(FIXTURES / "after.json")

    def write_test_data(self, data):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "snapshot.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def valid_sample(self):
        return json.loads((FIXTURES / "before.json").read_text(encoding="utf-8"))

    def test_reproducible_synthetic_changes(self):
        result = compare(self.before, self.after)
        self.assertEqual(result["before_count"], 3)
        self.assertEqual(result["after_count"], 4)
        self.assertEqual(result["added"], [
            {"protocol": "tcp", "port": 5985, "bind_scope": "specific"},
            {"protocol": "tcp", "port": 8000, "bind_scope": "wildcard"},
        ])
        self.assertEqual(result["removed"], [
            {"protocol": "tcp", "port": 8000, "bind_scope": "loopback"}
        ])
        self.assertEqual(result["scope_changes"], [{
            "protocol": "tcp", "port": 8000,
            "before_scopes": ["loopback"], "after_scopes": ["wildcard"],
        }])
        self.assertIn("does not prove external", " ".join(result["limitations"]))

    def test_identical_snapshots_have_no_differences(self):
        result = compare(self.before, self.before)
        self.assertEqual(result["added"], [])
        self.assertEqual(result["removed"], [])
        self.assertEqual(result["scope_changes"], [])

    def test_endpoint_protocol_distinguishes_same_number(self):
        a = self.valid_sample()
        a["endpoints"].append({"protocol": "udp", "port": 443, "bind_scope": "wildcard"})
        result = compare(self.before, read_snapshot(self.write_test_data(a)))
        self.assertEqual(result["added"], [
            {"protocol": "udp", "port": 443, "bind_scope": "wildcard"}
        ])

    def test_bad_ports_and_types(self):
        for value in [0, -1, 65536, True, "443", None]:
            with self.subTest(value=value):
                a = self.valid_sample()
                a["endpoints"][0]["port"] = value
                with self.assertRaises(ValueError):
                    read_snapshot(self.write_test_data(a))

    def test_invalid_scope_protocol_and_duplicate(self):
        for k, v in (("protocol", "smtp"), ("bind_scope", "internet")):
            a = self.valid_sample()
            a["endpoints"][0][k] = v
            with self.assertRaises(ValueError):
                read_snapshot(self.write_test_data(a))
        a = self.valid_sample()
        a["endpoints"].append(a["endpoints"][0])
        with self.assertRaises(ValueError):
            read_snapshot(self.write_test_data(a))

    def test_invalid_timestamps_and_missing_schema(self):
        for stamp in ["2026-10-01T10:00:00", "invalid", "2026-10-01T10:00:00+03:00"]:
            a = self.valid_sample()
            a["captured_at_utc"] = stamp
            with self.assertRaises(ValueError):
                read_snapshot(self.write_test_data(a))
        a = self.valid_sample()
        a["schema_version"] = 2
        with self.assertRaises(ValueError):
            read_snapshot(self.write_test_data(a))

    def test_invalid_json_and_missing_file(self):
        with tempfile.TemporaryDirectory() as td:
            invalid = Path(td) / "broken.json"
            invalid.write_text("not-json", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                read_snapshot(invalid)
            with self.assertRaises(OSError):
                read_snapshot(Path(td) / "absent.json")

    def test_source_and_scope_must_be_known(self):
        for field, value in [
            ("source", "unknown-source"),
            ("scope", "all-network-traffic"),
        ]:
            a = self.valid_sample()
            a[field] = value
            with self.assertRaises(ValueError):
                read_snapshot(self.write_test_data(a))

    def test_json_cli_and_text_cli(self):
        for format_name in ["json", "text"]:
            with self.subTest(format_name=format_name):
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    main(["--before", str(FIXTURES / "before.json"),
                          "--after", str(FIXTURES / "after.json"),
                          "--format", format_name])
                output = buf.getvalue()
                if format_name == "json":
                    report = json.loads(output)
                    self.assertEqual(report["after_count"], 4)
                    self.assertEqual(len(report["scope_changes"]), 1)
                else:
                    self.assertIn("Binding-scope changes: 1", output)
                    self.assertIn("not proof of internet exposure", output)

    def test_reverse_time_order_is_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                main(["--before", str(FIXTURES / "after.json"),
                      "--after", str(FIXTURES / "before.json")])
        self.assertEqual(cm.exception.code, 2)

    def test_mixing_local_and_synthetic_evidence_is_rejected(self):
        a = self.valid_sample()
        a["source"] = "local-windows-readonly-collector"
        path = self.write_test_data(a)
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                main(["--before", str(path),
                      "--after", str(FIXTURES / "after.json")])
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
