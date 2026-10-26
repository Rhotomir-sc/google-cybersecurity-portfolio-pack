import sys
import json
import io
import contextlib
from unittest.mock import patch
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_signin_case import load_events, DEFAULT_INPUT, build_report, main
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

    def test_json_report_matches_fixture_and_labels_uncertainty(self):
        report = build_report(load_events(DEFAULT_INPUT))
        self.assertEqual(report['schema_version'], 1)
        self.assertEqual(report['rule_id'], 'AUTH-001')
        self.assertEqual(report['event_count'], 12)
        self.assertEqual(report['finding_count'], 1)
        finding = report['findings'][0]
        self.assertEqual(finding['user'], 'emma.lee@northstar.example')
        self.assertEqual(finding['source_ip'], '198.51.100.23')
        self.assertEqual(finding['failed_count'], 6)
        self.assertEqual(finding['first_matching_success'], '2026-09-10 08:15:19')
        self.assertEqual([a['application'] for a in finding['later_successful_applications']],
                         ['OfficeHome', 'Outlook Web', 'My Profile'])
        self.assertEqual(finding['disposition'], 'review_required')
        self.assertIn('does not prove an account compromise', ' '.join(report['limitations']))
        self.assertEqual(json.loads(json.dumps(report))['finding_count'], 1)

    def test_cli_json_and_original_text_modes(self):
        for output_format in ('json', 'text'):
            with self.subTest(output_format=output_format):
                buffer = io.StringIO()
                with patch.object(sys, 'argv', ['analyze_signin_case.py', '--format', output_format]):
                    with contextlib.redirect_stdout(buffer):
                        main()
                output = buffer.getvalue()
                if output_format == 'json':
                    obj = json.loads(output)
                    self.assertEqual(obj['finding_count'], 1)
                    self.assertEqual(obj['findings'][0]['failed_count'], 6)
                else:
                    self.assertIn('Events: 12', output)
                    self.assertIn('Sequences requiring review: 1', output)
                    self.assertIn('Assessment: REVIEW FOR POSSIBLE ACCOUNT COMPROMISE', output)

    def test_json_with_no_matching_sequence(self):
        report = build_report(load_events(DEFAULT_INPUT), threshold=7)
        self.assertEqual(report['finding_count'], 0)
        self.assertEqual(report['findings'], [])

    def test_invalid_detection_window_cannot_be_nan_or_infinite(self):
        events = load_events(DEFAULT_INPUT)
        for value in (float('nan'), float('inf'), float('-inf'), 0, -1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    build_report(events, window_minutes=value)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(OSError):
                load_events(Path(directory) / 'missing.csv')
