# Google Cybersecurity Professional Certificate - Portfolio

## Start here

- [Artifact index and evidence status](ARTIFACTS.md)
- [Run the Python and SQL examples](REPRODUCE.md)
- [Featured integrated case](integrated-security-case/README.md)


## Overview

This repository documents my practical work completed alongside the **Google Cybersecurity Professional Certificate**.

Rather than using the repository as a collection of course notes, I focused on converting the material into security artifacts, technical analysis, scripts, investigation workflows, and documented findings.

The portfolio covers:

```text
Security Foundations
Risk & Controls
Network Security
Linux & SQL
Threats & Vulnerabilities
Detection & Incident Response
Python Automation
Career Preparation
```

It also includes an **Integrated Security Case** that connects these areas into a single investigation workflow.

---

## Professional Certificate

**Google Cybersecurity Professional Certificate**  
**Issued by:** Google / Coursera  
**Completed:** June 1, 2026  
**Courses Completed:** 9

[View Certificate and Credential Details](certificate/README.md)

The certificate currently contains nine courses.

This repository focuses primarily on the first eight cybersecurity-focused courses.

The ninth course, **Accelerate Your Job Search with AI**, is career-development focused and is documented through the credential rather than as a separate technical module.

---

# Portfolio Structure

```text
google-cybersecurity-portfolio-pack/
│
├── 01_Module-1_Foundations-of-Cybersecurity/
├── 02_Module-2_Play-It-Safe_Manage-Security-Risks/
├── 03_Module-3_Connect-and-Protect_Networks/
├── 04_Module-4_Tools-of-the-Trade_Linux-and-SQL/
├── 05_Module-5_Assets-Threats-and-Vulnerabilities/
├── 06_Module-6_Sound-the-Alarm_Detection-and-Response/
├── 07_Module-7_Automate-Cybersecurity-Tasks-with-Python/
├── 08_Module-8_Put-It-to-Work_Prepare-for-Cybersecurity-Jobs/
│
├── integrated-security-case/
├── certificate/
├── related-tryhackme-labs.md
└── README.md
```

---

# Modules

## 01 - Foundations of Cybersecurity

Introduces the security mindset and core concepts used throughout the portfolio.

Topics include:

- CIA triad
- threats, vulnerabilities, and risks
- security controls
- security domains
- evidence-based documentation

[View Module 1](01_Module-1_Foundations-of-Cybersecurity/)

---

## 02 - Manage Security Risks

Focuses on governance, risk, and security controls.

Portfolio artifacts include:

- risk register
- controls mapping
- preventive, detective, and corrective control analysis

[View Module 2](02_Module-2_Play-It-Safe_Manage-Security-Risks/)

---

## 03 - Networks and Network Security

Covers networking fundamentals from a defensive security perspective.

Topics include:

- IP addressing
- TCP and UDP
- ports and services
- DNS
- network baselines
- firewalls
- segmentation
- secure protocols

[View Module 3](03_Module-3_Connect-and-Protect_Networks/)

---

## 04 - Linux and SQL

Applies Linux command-line and SQL skills to security analysis.

Portfolio artifacts include:

- Linux security cheatsheet
- practical Linux commands
- log-analysis commands
- SQL security queries

Tools and concepts include:

```text
grep
awk
cut
sort
uniq
chmod
user / group management
SELECT
WHERE
GROUP BY
JOIN
```

[View Module 4](04_Module-4_Tools-of-the-Trade_Linux-and-SQL/)

---

## 05 - Assets, Threats, and Vulnerabilities

Focuses on identifying important assets and evaluating security exposure.

Topics include:

- asset classification
- threat identification
- vulnerabilities
- attack surface
- defense in depth
- risk prioritisation

Portfolio artifact:

[Asset Risk Assessment](05_Module-5_Assets-Threats-and-Vulnerabilities/asset-risk-assessment.md)

[View Module 5](05_Module-5_Assets-Threats-and-Vulnerabilities/)

---

## 06 - Detection and Incident Response

Applies monitoring, alert triage, investigation, and incident-response concepts.

Topics include:

- security monitoring
- SIEM
- log correlation
- indicators of compromise
- alert validation
- containment
- eradication
- recovery

Portfolio artifacts include an incident report and reusable incident-response documentation.

[View Module 6](06_Module-6_Sound-the-Alarm_Detection-and-Response/)

---

## 07 - Python Security Automation

Uses Python to reduce repetitive security-analysis tasks.

Scripts include:

```text
failed_login_analyzer.py
ioc_extractor.py
access_list_updater.py
```

The scripts demonstrate:

- authentication analysis
- IOC extraction
- access-list modification
- security-focused data processing

Execution evidence is included with the module.

[View Module 7](07_Module-7_Automate-Cybersecurity-Tasks-with-Python/)

---

## 08 - Prepare for Cybersecurity Jobs

Connects the technical work from the certificate to portfolio development and entry-level cybersecurity roles.

This module summarises the technical capabilities demonstrated throughout the repository and connects them to continued development in:

```text
Cloud Security
Identity Security
SOC / Incident Response
```

[View Module 8](08_Module-8_Put-It-to-Work_Prepare-for-Cybersecurity-Jobs/)

---

# Featured Project - Integrated Security Case

The strongest project in this repository is the:

## Northstar Solutions Integrated Security Case

This fictional investigation combines concepts from multiple certificate modules.

The workflow follows:

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

The case includes:

- fictional security datasets
- authentication analysis
- Linux web-log investigation
- SQL security queries
- detection logic
- incident-response assessment
- Python authentication automation
- remediation recommendations

The Python script analyses authentication events and identifies repeated failures followed by successful access from the same source.

[View Integrated Security Case](integrated-security-case/README.md)

---

# Hands-On Security Practice

The Google portfolio focuses on structured security fundamentals and portfolio artifacts.

Additional hands-on defensive security work is documented separately in my TryHackMe repository:

**[TryHackMe Cybersecurity Portfolio](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack)**

The TryHackMe portfolio includes practical work in areas such as:

- Linux administration
- permissions and least privilege
- Wireshark traffic analysis
- Nmap host discovery
- log analysis
- SIEM alert triage
- incident response
- threat intelligence
- Windows Event Logs
- cloud identity
- firewall auditing
- phishing analysis

Module-to-lab relationships are documented here:

[Google ↔ TryHackMe Lab Mapping](related-tryhackme-labs.md)

---

# Evidence Philosophy

This portfolio is designed around:

```text
Evidence > Claims
```

Screenshots are included only when they provide useful proof of technical work, such as:

- command execution
- script output
- analysis results
- system observations
- investigation findings

Course slides, repetitive screenshots, and screenshots that do not demonstrate practical work are intentionally avoided.

---

# Technical Skills Demonstrated

### Security Operations

```text
Log Analysis
SIEM Concepts
Alert Triage
Event Correlation
Incident Response
IOC Analysis
```

### Systems

```text
Linux
Windows Event Logs
Permissions
Users & Groups
Least Privilege
```

### Network Security

```text
TCP/IP
DNS
Ports
Wireshark
Nmap
Firewall Analysis
Web Logs
```

### Identity Security

```text
Authentication Analysis
Failed Sign-In Investigation
MFA
Conditional Access Concepts
Cloud Identity Monitoring
```

### Data & Automation

```text
SQL
Python
CSV Processing
IOC Extraction
Authentication Analysis
Security Automation
```

### Risk & Governance

```text
Asset Identification
Risk Assessment
Control Mapping
Defense in Depth
Remediation Prioritisation
```

---

# Current Direction

My current technical development is focused on:

```text
Cloud Security
        +
Identity Security
        +
SOC / Incident Response
```

with future expansion into:

```text
Cloud Security Engineering
AI Security
Security Automation
```

---

# Portfolio Approach

The repositories in my portfolio serve different purposes:

```text
Google Cybersecurity Portfolio
→ structured foundations + security artifacts

TryHackMe Portfolio
→ hands-on defensive security labs

Integrated Security Case
→ multi-stage investigation and correlation

Future Security Projects
→ deeper cloud, identity, automation, and AI-security work
```

This separation keeps course learning, practical labs, and larger security projects organised without duplicating evidence.

---

## Disclaimer

Some scenarios and datasets in this repository are fictional and were created for educational and portfolio purposes.

Conclusions are intentionally limited to what the available evidence supports.
