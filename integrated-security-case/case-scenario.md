# Integrated Security Case - Scenario

## Scenario

This case is based on a fictional small company called **Northstar Solutions**.

The company uses:

- Microsoft 365 for email and collaboration
- employee Windows laptops
- a Linux web server
- an internal customer database
- remote administration services
- cloud user accounts

The security team receives reports of unusual authentication activity and suspicious web traffic.

The goal of this case is to investigate the environment by combining concepts from multiple Google Cybersecurity Certificate modules.

---

## Environment

| Asset | Purpose | Security Importance |
|---|---|---|
| Microsoft 365 Accounts | Employee identity and cloud access | High |
| Linux Web Server | Hosts company web services | High |
| Customer Database | Stores customer information | Critical |
| Windows Endpoints | Employee workstations | Medium |
| Corporate Email | Business communication | High |
| Remote Administration | IT management | High |

---

## Initial Security Concerns

The investigation begins with several observations:

- repeated failed login attempts against a cloud user
- a later successful login from the same source
- repeated requests to a sensitive web endpoint
- an administrative service exposed too broadly
- suspicious indicators that require correlation

These observations are treated as investigation leads rather than confirmed malicious activity until supporting evidence is reviewed.

---

## Investigation Objectives

The case will answer the following questions:

1. Which assets are most important?
2. What risks and vulnerabilities affect them?
3. Which security controls should reduce those risks?
4. Does the network or web activity show suspicious patterns?
5. Can Linux and SQL be used to reduce the investigation dataset?
6. Is there enough evidence to escalate the activity?
7. What incident-response actions should be taken?
8. Can part of the analysis be automated with Python?

---

## Case Workflow

```text
Asset Identification
        ↓
Risk Assessment
        ↓
Control Selection
        ↓
Log / Network Analysis
        ↓
Linux & SQL Investigation
        ↓
Detection & Correlation
        ↓
Incident Response
        ↓
Python Automation
        ↓
Final Recommendations
```
