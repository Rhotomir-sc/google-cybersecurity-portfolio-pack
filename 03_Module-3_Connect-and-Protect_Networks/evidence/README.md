# Network evidence status

**Live host baseline: pending.** The repository does not yet include an authorized Windows host snapshot or an observed before/after comparison.

The [collection guide](../network-baseline-and-security-notes.md) now offers a read-only, privacy-minimized Windows PowerShell collector, an offline Python comparator, and synthetic test fixtures. Passing the synthetic tests validates the comparator logic; it is **not proof of having performed a real network baseline**.

Previously included one-byte image placeholders were removed and must not be treated as evidence.

To close this gap, collect real snapshots on an authorized machine, review port/service context and privacy implications, and document:
- the system's role and the collection date/time;
- the commands/tool version and conditions for both snapshots;
- the actual comparison, expected versus unexpected differences, and limitations;
- redactions and permission to share any sanitized material.

Do not upload sensitive configuration details or unreviewed local snapshots.
