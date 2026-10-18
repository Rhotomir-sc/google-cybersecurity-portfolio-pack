import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_signin_case import load_events, DEFAULT_INPUT
from auth_patterns import detect_sequences

class InputTests(unittest.TestCase):
    def test_real_fixture(self):
        events = load_events(DEFAULT_INPUT)
        self.assertEqual(len(events), 12)
        findings = detect_sequences(events)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]['failed_count'], 6)
    def test_bad_csv(self):
        for content in ['wrong,columns\na,b\n', 'timestamp,user,source_ip,status,application\nbad,a,192.0.2.1,failed,app\n', 'timestamp,user,source_ip,status,application\n2026-01-01 00:00:00,a,192.0.2.1,unknown,app\n']:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'input.csv'
                path.write_text(content)
                with self.assertRaises(ValueError):
                    load_events(path)
    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(OSError):
                load_events(Path(directory) / 'missing.csv')
