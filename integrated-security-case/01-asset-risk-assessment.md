# 01 - Asset & Risk Assessment

## Objective

The first step of the investigation is to identify the most important assets in the Northstar Solutions environment and evaluate the main security risks affecting them.

---

## Critical Assets

| Asset | Importance | Main Security Concern |
|---|---:|---|
| Customer Database | Critical | Sensitive data exposure |
| Microsoft 365 Accounts | High | Account takeover |
| Corporate Email | High | Phishing and credential theft |
| Linux Web Server | High | Web attacks and unauthorised access |
| Windows Endpoints | Medium | Malware and credential theft |
| Remote Administration Service | High | Unauthorised remote access |

---

# Risk Assessment

## Risk 1 - Cloud Account Compromise

### Asset

Microsoft 365 employee accounts

### Threat

Credential theft or brute-force activity

### Vulnerabilities

- weak or reused passwords
- missing or ineffective MFA controls
- insufficient sign-in monitoring

### Possible Impact

```text
Email access
Cloud application access
Sensitive data exposure
Account misuse
```
