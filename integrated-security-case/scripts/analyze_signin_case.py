"""Analyze the fictional CSV using time-bounded authentication sequences."""
import argparse
import csv
from datetime import datetime
from pathlib import Path
from auth_patterns import detect_sequences

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / 'sample-data' / 'signin-events.csv'


def load_events(path):
    events = []
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        required = {'timestamp', 'user', 'source_ip', 'status', 'application'}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError('CSV missing required columns: ' + ', '.join(sorted(required)))
        for line, row in enumerate(reader, 2):
            try:
                event = {key: row[key].strip() for key in required}
                if not all(event.values()):
                    raise ValueError('empty required field')
                event['timestamp'] = datetime.fromisoformat(event['timestamp'])
                if event['timestamp'].tzinfo is not None:
                    raise ValueError('use naive timestamps in one documented timezone')
                if event['status'] not in {'failed', 'success'}:
                    raise ValueError('unknown status')
                events.append(event)
            except (ValueError, AttributeError) as exc:
                raise ValueError(f'Invalid CSV row {line}: {exc}') from exc
    return events


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--threshold', type=int, default=3)
    parser.add_argument('--window-minutes', type=float, default=10)
    args = parser.parse_args()
    try:
        events = load_events(args.input)
        findings = detect_sequences(events, args.threshold, args.window_minutes)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print('Integrated Security Case - Authentication Analysis')
    print(f'Events: {len(events)}')
    print(f'Rule: >= {args.threshold} failures in {args.window_minutes:g} minutes before success')
    print(f'Sequences requiring review: {len(findings)}')
    for finding in findings:
        print(f"\nUser: {finding['user']}\nSource IP: {finding['source_ip']}")
        print(f"Failed attempts before success: {finding['failed_count']}")
        print(f"First failure: {finding['first_failure'].isoformat(sep=' ')}")
        print(f"First matching success: {finding['success_time'].isoformat(sep=' ')}")
        print('Successful application events from this point (context, not proof of misuse):')
        for event in sorted(events, key=lambda item: item['timestamp']):
            if ((event['user'], event['source_ip']) == (finding['user'], finding['source_ip'])
                    and event['status'] == 'success' and event['timestamp'] >= finding['success_time']):
                print(f"- {event['application']} at {event['timestamp'].isoformat(sep=' ')}")
        print('Assessment: REVIEW FOR POSSIBLE ACCOUNT COMPROMISE')
    if not findings:
        print('No sequence met this rule; this does not establish that activity is benign.')


if __name__ == '__main__':
    main()
