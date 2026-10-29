# Google Cybersecurity — Applied Portfolio

**Google Cybersecurity Professional Certificate · Risk & Controls · Linux/SQL · SOC/IR · Python**

This repository turns certificate coursework into reviewable security artifacts: risk assessments, investigation notes, small Python tools and a **reproducible fictional security case**. It is not a transcript of course slides.

## Start here

- **[Integrated Security Case — Northstar Solutions](integrated-security-case/README.md)** — an end-to-end *synthetic* investigation combining cloud sign-ins, Linux web logs, SQL, incident response and Python.
- **[Artifact and evidence index](ARTIFACTS.md)** — what exists, what was executed, and what evidence is still missing.
- **[Reproduce the Python and SQL work](REPRODUCE.md)** — commands, fixtures, unit tests and expected results.
- **[Google certificate (PDF)](certificate/README.md)** — credential evidence and scope.

## Featured investigation

The [Northstar case](integrated-security-case/README.md) follows **asset context → risk → controls → authentication/web/SQL analysis → response → automation → recommendations**.

The synthetic sign-in dataset includes **six failed attempts followed by a success for the same user and source**. The detector implements a configurable time-bounded sequence rule, with [tests](integrated-security-case/tests/test_auth_patterns.py) and a [reproduction guide](REPRODUCE.md). It identifies a **review lead**, not a confirmed account takeover.

Web log findings and identity events are separate leads; the available evidence does not attribute them to one attacker. The case uses fictional accounts and documentation-only IP ranges.

## Technical modules

| Course area | Practical focus |
|---|---|
| [01 · Foundations](01_Module-1_Foundations-of-Cybersecurity/README.md) | Scope, security concepts and evidence discipline |
| [02 · Risk management](02_Module-2_Play-It-Safe_Manage-Security-Risks/README.md) | Risk register and security control mapping |
| [03 · Networks](03_Module-3_Connect-and-Protect_Networks/README.md) | Read-only Windows baseline collector, [tested comparison workflow](03_Module-3_Connect-and-Protect_Networks/network-baseline-and-security-notes.md); owner's host capture **pending** |
| [04 · Linux and SQL](04_Module-4_Tools-of-the-Trade_Linux-and-SQL/README.md) | Command-line analysis and query examples |
| [05 · Assets and vulnerabilities](05_Module-5_Assets-Threats-and-Vulnerabilities/README.md) | Fictional asset risk assessment |
| [06 · Detection and response](06_Module-6_Sound-the-Alarm_Detection-and-Response/README.md) | Incident report and response documentation |
| [07 · Python automation](07_Module-7_Automate-Cybersecurity-Tasks-with-Python/README.md) | Login counting, IOC extraction and access-list simulation |
| [08 · Career preparation](08_Module-8_Put-It-to-Work_Prepare-for-Cybersecurity-Jobs/README.md) | Evidence-based portfolio development |

The credential records **nine courses**. This technical portfolio is organized around the first eight security-focused areas; the ninth, *Accelerate Your Job Search with AI*, is a career-development course, not presented here as a technical security lab.

## Scope and evidence standard

I separate **executed work**, **synthetic scenarios**, **proposed controls**, and **pending verification**. The integrated Python analysis and SQL examples can be reproduced from committed data. The Module 7 screenshots are historical and may differ from current fixture output. The Module 3 network baseline still needs a genuine local capture.

The goal is to show reasoning and verifiable artifacts rather than inflate screenshots, certifications, or claimed production experience.

## Related hands-on work

- [TryHackMe defensive security portfolio](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack) — 12 documented investigations spanning SOC, incident response, networks, Windows, identity and phishing.
- [Google ↔ TryHackMe topic mapping](related-tryhackme-labs.md) — connections between course topics and hands-on labs.
- [Security capstone](https://github.com/Rhotomir-sc/security-capstone) — a separate small fictional security assessment with reproducible SSH authentication analysis.

**Development focus:** cloud and identity security, detection/incident response, and security automation. Longer term, I aim to combine defensive analysis with controlled attacker-informed testing and AI security.

*The scenarios and datasets described as fictional are not real production incidents. Findings never exceed the supporting evidence.*
