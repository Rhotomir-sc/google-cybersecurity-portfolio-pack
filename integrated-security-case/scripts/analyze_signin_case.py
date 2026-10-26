"""Analyze the fictional CSV using time-bounded authentication sequences."""
import argparse
import csv
import json
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


def build_report(events, threshold=3, window_minutes=10):
    """Return a deterministic, machine-readable investigation summary.

    Later application sign-ins share an identity and IP, but may belong to
    separate sessions. The rule itself is a lead for analyst review.
    """
    findings = detect_sequences(events, threshold, window_minutes)
    ordered = sorted(events, key=lambda item: item['timestamp'])
    results = []
    for finding in findings:
        later = [
            {'application': item['application'],
             'timestamp': item['timestamp'].isoformat(sep=' ')}
            for item in ordered
            if (item['user'], item['source_ip']) ==
            (finding['user'], finding['source_ip'])
            and item['status'] == 'success'
            and item['timestamp'] >= finding['success_time']
        ]
        results.append({
            'user': finding['user'],
            'source_ip': finding['source_ip'],
            'failed_count': finding['failed_count'],
            'first_failure': finding['first_failure'].isoformat(sep=' '),
            'first_matching_success': finding['success_time'].isoformat(sep=' '),
            'later_successful_applications': later,
            'disposition': 'review_required',
        })
    return {
        'schema_version': 1,
        'rule_id': 'AUTH-001',
        'dataset': 'synthetic_educational_case',
        'rule': {
            'minimum_failures': threshold,
            'window_minutes': window_minutes,
            'group_by': ['user', 'source_ip'],
            'success_must_follow_failures': True,
        },
        'event_count': len(events),
        'finding_count': len(results),
        'findings': results,
        'limitations': [
            'A matched sequence does not prove an account compromise.',
            'Same user and IP do not prove the same authenticated session.',
            'Synthetic data does not establish detection performance in production.',
        ],
    }


def print_text_report(report):
    """Keep the original human-readable workflow as the default."""
    rule = report['rule']
    print('Integrated Security Case - Authentication Analysis')
    print(f"Events: {report['event_count']}")
    print(f"Rule: >= {rule['minimum_failures']} failures in "
          f"{rule['window_minutes']:g} minutes before success")
    print(f"Sequences requiring review: {report['finding_count']}")
    for finding in report['findings']:
        print(f"\nUser: {finding['user']}\nSource IP: {finding['source_ip']}")
        print(f"Failed attempts before success: {finding['failed_count']}")
        print(f"First failure: {finding['first_failure']}")
        print(f"First matching success: {finding['first_matching_success']}")
        print('Successful application events from this point (context, not proof of misuse):')
        for event in finding['later_successful_applications']:
            print(f"- {event['application']} at {event['timestamp']}")
        print('Assessment: REVIEW FOR POSSIBLE ACCOUNT COMPROMISE')
    if not report['findings']:
        print('No sequence met this rule; this does not establish that activity is benign.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--threshold', type=int, default=3)
    parser.add_argument('--window-minutes', type=float, default=10)
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                        help='Text summary (default) or JSON for offline analysis')
    args = parser.parse_args()
    try:
        events = load_events(args.input)
        report = build_report(events, args.threshold, args.window_minutes)
    except (OSError, ValueError, OverflowError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    if args.format == 'json':
        print(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False))
    else:
        print_text_report(report)


if __name__ == '__main__':
    main()
