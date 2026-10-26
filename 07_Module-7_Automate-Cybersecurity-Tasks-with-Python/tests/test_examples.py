"""Offline smoke tests for the three introductory Module 7 Python examples.

These tests verify the committed synthetic fixtures and script behavior; they
are not evidence of deployment, detection accuracy, or real security incidents.
"""
import contextlib
import io
from collections import Counter
from pathlib import Path
import runpy
import unittest

BASE = Path(__file__).resolve().parents[1]
SCRIPTS = BASE / "scripts"


class Module7ExamplesTests(unittest.TestCase):
    def test_failed_login_fixture_and_output(self):
        ns = runpy.run_path(str(SCRIPTS / "failed_login_analyzer.py"), run_name="module_under_test")
        failures = ns["load_failed_logins"](ns["LOG_FILE"])
        self.assertEqual(len(failures), 8)
        self.assertEqual(ns["count_failed_attempts"](failures, "username"), Counter({"alice": 4, "charlie": 4}))
        self.assertEqual(ns["count_failed_attempts"](failures, "source_ip"),
                         Counter({"10.10.10.15": 4, "185.44.21.90": 4}))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            runpy.run_path(str(SCRIPTS / "failed_login_analyzer.py"), run_name="__main__")
        self.assertIn("Total failed attempts: 8", out.getvalue())
        self.assertIn("alice: 4 <-- REVIEW", out.getvalue())
        self.assertIn("charlie: 4 <-- REVIEW", out.getvalue())

    def test_ioc_extractor_known_fixture(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ns = runpy.run_path(str(SCRIPTS / "ioc_extractor.py"), run_name="__main__")
        self.assertEqual(ns["ip_addresses"], ["185.44.21.90", "193.46.217.4"])
        self.assertEqual(ns["domains"], ["fshjaifhajfa.click"])
        self.assertEqual(len(ns["sha256_hashes"]), 1)
        self.assertEqual(len(ns["sha256_hashes"][0]), 64)
        self.assertIn("IOC Extraction Results", out.getvalue())

    def test_in_memory_allow_list_update(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ns = runpy.run_path(str(SCRIPTS / "access_list_updater.py"), run_name="__main__")
        self.assertEqual(ns["allowed_ips"], [
            "192.168.10.10", "192.168.10.15", "192.168.10.20"
        ])
        self.assertEqual(ns["remove_ips"], ["10.10.10.15", "185.44.21.90"])
        self.assertIn("Updated Allow List", out.getvalue())


if __name__ == "__main__":
    unittest.main()
