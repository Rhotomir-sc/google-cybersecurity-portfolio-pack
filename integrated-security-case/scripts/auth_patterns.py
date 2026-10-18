"""Educational authentication sequence detection; no external dependencies."""
from collections import defaultdict, deque
from datetime import timedelta


def detect_sequences(events, threshold=3, window_minutes=10):
    """Match strictly earlier failures by user and IP within a time window.

    Input events have datetime timestamp, user, source_ip and failed/success status.
    Success resets a sequence. Equal timestamps do not establish ordering.
    Duplicate rows count as events; findings are review leads, not attack verdicts.
    """
    if threshold < 1 or window_minutes <= 0:
        raise ValueError('threshold and window_minutes must be positive')
    pending = defaultdict(deque)
    findings = []
    window = timedelta(minutes=window_minutes)
    for event in sorted(events, key=lambda item: item['timestamp']):
        if event['status'] not in {'failed', 'success'}:
            raise ValueError('status must be failed or success')
        key = (event['user'], event['source_ip'])
        queue = pending[key]
        cutoff = event['timestamp'] - window
        while queue and queue[0]['timestamp'] < cutoff:
            queue.popleft()
        if event['status'] == 'failed':
            queue.append(event)
        else:
            earlier = [item for item in queue if item['timestamp'] < event['timestamp']]
            if len(earlier) >= threshold:
                findings.append(dict(user=key[0], source_ip=key[1], failed_count=len(earlier),
                                     first_failure=earlier[0]['timestamp'], success_time=event['timestamp']))
            queue.clear()
    return findings
