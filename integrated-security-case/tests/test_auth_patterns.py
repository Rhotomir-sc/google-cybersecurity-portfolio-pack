import sys
import unittest
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from auth_patterns import detect_sequences


class SequenceTests(unittest.TestCase):
    def event(self, minute, status, user='alice', ip='192.0.2.10'):
        return dict(timestamp=datetime(2026, 1, 1) + timedelta(minutes=minute),
                    user=user, source_ip=ip, status=status)

    def test_unsorted_input(self):
        events = [self.event(3, 'success')] + [self.event(n, 'failed') for n in range(3)]
        self.assertEqual(detect_sequences(events)[0]['failed_count'], 3)

    def test_success_before_failures(self):
        self.assertEqual(detect_sequences([self.event(0, 'success')] +
                         [self.event(n, 'failed') for n in range(1, 4)]), [])

    def test_expired_failures(self):
        self.assertEqual(detect_sequences([self.event(n, 'failed') for n in range(3)] +
                         [self.event(20, 'success')]), [])

    def test_other_identity_or_ip(self):
        failures = [self.event(n, 'failed') for n in range(3)]
        for kwargs in (dict(user='bob'), dict(ip='192.0.2.20')):
            self.assertEqual(detect_sequences(failures + [self.event(3, 'success', **kwargs)]), [])

    def test_success_resets_sequence(self):
        events = [self.event(n, 'failed') for n in range(3)]
        events += [self.event(3, 'success'), self.event(4, 'success')]
        self.assertEqual(len(detect_sequences(events)), 1)

    def test_equal_timestamps(self):
        self.assertEqual(detect_sequences([self.event(0, 'failed')] * 3 +
                         [self.event(0, 'success')]), [])

    def test_threshold_and_inclusive_boundary(self):
        events = [self.event(0, 'failed'), self.event(1, 'failed'), self.event(10, 'success')]
        self.assertEqual(len(detect_sequences(events, threshold=2)), 1)
        self.assertEqual(detect_sequences(events), [])

    def test_empty_or_failures_only(self):
        self.assertEqual(detect_sequences([]), [])
        self.assertEqual(detect_sequences([self.event(n, 'failed') for n in range(3)]), [])

    def test_invalid_configuration(self):
        with self.assertRaises(ValueError):
            detect_sequences([], threshold=0)


if __name__ == '__main__':
    unittest.main()
