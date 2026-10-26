# Integrated Security Case

[Reproduce this case](../REPRODUCE.md). The current detector requires timestamp-ordered failures within ten minutes before success. A success resets the sequence. Screenshots show an earlier script version; use the current commands for current output.


## Detection engineering

The [AUTH-001 detection rule](DETECTION-RULE.md) specifies the failure-then-success sequence, expected test cases, false-positive boundaries, and an optional machine-readable **JSON output**. It uses synthetic data and is not a deployed cloud detection.

## Overview

This case brings together the main skills developed across my Google Cybersecurity Certificate portfolio into one fictional security investigation.

Instead of treating each topic separately, the case connects:

```text
Asset Identification
        ↓
Risk Assessment
        ↓
Security Controls
        ↓
Authentication Analysis
        ↓
Linux Web Log Analysis
        ↓
SQL Investigation
        ↓
Detection & Incident Response
        ↓
Python Automation
        ↓
Final Assessment
```

The objective is to demonstrate how different cybersecurity disciplines support the same investigation.

---

## Scenario

**Northstar Solutions** is a fictional small company using:

- Microsoft 365
- corporate email
- Windows endpoints
- a Linux web server
- a customer database
- remote administration services

The investigation begins after suspicious authentication activity and unusual web requests are identified.

Full scenario:

[Case Scenario](case-scenario.md)

---

# Investigation Stages

## 01 - Asset & Risk Assessment

Identified critical business assets and evaluated risks related to:

- cloud identity
- customer data
- phishing
- web services
- remote administration

[View Asset & Risk Assessment](01-asset-risk-assessment.md)

---

## 02 - Security Controls Mapping

Mapped the identified risks to:

```text
Preventive Controls
Detective Controls
Corrective Controls
```

Examples include:

- MFA
- Conditional Access
- least privilege
- firewall restrictions
- logging
- incident response

[View Security Controls Mapping](02-security-controls-mapping.md)

---

## 03 - Authentication Log Analysis

Investigated repeated authentication failures against:

```text
emma.lee@northstar.example
```

The dataset showed:

```text
6 failed sign-ins
        ↓
Successful authentication
        ↓
OfficeHome
        ↓
Outlook Web
        ↓
My Profile
```

The activity was classified as:

```text
Suspicious authentication activity
with possible account compromise
```

[View Authentication Analysis](03-authentication-log-analysis.md)

---

## 04 - Web & Linux Log Analysis

Analysed Apache-style access logs using Linux command-line tools.

Techniques included:

```bash
grep
awk
cut
sort
uniq
```

The analysis identified:

- sensitive endpoint enumeration
- repeated login attempts
- HTTP 401 / 404 activity
- suspicious source behaviour

[View Web & Linux Log Analysis](04-web-linux-log-analysis.md)

---

## 05 - SQL Security Analysis

Used SQL to investigate structured authentication and asset data.

Queries applied:

```text
SELECT
WHERE
AND
OR
GROUP BY
COUNT
ORDER BY
IN
```

The analysis correlated:

```text
Identity
+
Source IP
+
Authentication status
+
Application access
+
Asset importance
```

[View SQL Security Analysis](05-sql-security-analysis.md)

---

## 06 - Detection & Incident Response

Combined the technical findings into a structured security assessment.

Three main findings were investigated:

1. possible cloud account compromise
2. likely web enumeration
3. suspicious web authentication activity

The response followed:

```text
Detect
↓
Validate
↓
Correlate
↓
Contain
↓
Eradicate
↓
Recover
↓
Monitor
```

[View Detection & Incident Response](06-detection-incident-response.md)

---

## 07 - Python Automation

Created a Python script to analyse the authentication dataset automatically.

The script:

- reads CSV authentication events
- counts failed attempts
- groups events by user and source IP
- identifies repeated failures
- checks for successful sign-ins from the same source
- lists applications accessed
- generates an investigation-focused assessment

Script:

[`scripts/analyze_signin_case.py`](scripts/analyze_signin_case.py)

Analysis:

[View Python Automation](07-python-automation.md)

### Execution Evidence

![Python Authentication Analysis](evidence/01-python-authentication-analysis.png)

---

## 08 - Final Assessment

The final assessment prioritised the possible cloud identity compromise and provided remediation recommendations across:

- identity security
- web security
- endpoint security
- remote administration
- logging
- detection
- automation

[View Final Assessment & Recommendations](08-final-assessment-recommendations.md)

---

# Case Data

The investigation uses fictional datasets stored under:

```text
sample-data/
├── signin-events.csv
├── access.log
└── security-case.sql
```

These datasets were created specifically for portfolio practice.

Documentation-only IP ranges are used where external addresses are needed.

---

# Technical Skills Demonstrated

## Security Operations

- log analysis
- event correlation
- detection logic
- incident triage
- incident response

## Identity Security

- authentication analysis
- failed-login investigation
- session-risk thinking
- MFA and Conditional Access recommendations

## Linux

- `grep`
- `awk`
- `cut`
- `sort`
- `uniq`

## SQL

- filtering
- grouping
- counting
- structured investigation
- asset context

## Python

- CSV parsing
- dictionaries
- loops
- conditional logic
- list comprehensions
- file paths
- security automation

## Risk & Controls

- asset identification
- risk assessment
- control selection
- defense in depth
- remediation prioritisation

---

# Investigation Principle

A major focus of this case is separating:

```text
Observed Evidence
```

from:

```text
Analyst Assumptions
```

For example:

```text
HTTP 200
≠
Confirmed successful authentication
```

and:

```text
Suspicious sign-in sequence
≠
Automatically confirmed account compromise
```

Additional evidence must support stronger conclusions.

---

# Relationship to the Portfolio

This integrated case connects concepts from all eight Google Cybersecurity Certificate modules.

The broader hands-on lab portfolio is available here:

[TryHackMe Cybersecurity Portfolio](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack)

The Google portfolio focuses on structured cybersecurity fundamentals and artifacts, while the TryHackMe repository provides additional hands-on defensive security evidence.

---

# Result

This project demonstrates a complete investigation workflow:

```text
Understand the environment
        ↓
Identify risk
        ↓
Analyse technical evidence
        ↓
Correlate events
        ↓
Assess severity
        ↓
Respond
        ↓
Automate repetitive analysis
        ↓
Recommend improvements
```

The case is intentionally evidence-based and avoids claiming more than the available data supports.

---

## Disclaimer

This is a fictional cybersecurity portfolio scenario.

It does not represent a real organisation, production environment, or real security incident.
