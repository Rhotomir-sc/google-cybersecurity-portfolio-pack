# 01 - Asset & Risk Assessment

## Objective and scope

Identify the assets that matter most to **Northstar Solutions**, a fictional company, and prioritize security risks before examining authentication and web logs.

This is a **qualitative scenario-based assessment**, not a production audit or a claim that the listed weaknesses were discovered on real systems. Likelihood ratings are illustrative planning assumptions; a finding is not confirmed until technical evidence supports it.

## Asset inventory

| Asset | Importance | Main exposure to assess |
|---|---|---|
| Customer database | Critical | Unauthorized access or disclosure |
| Microsoft 365 identities | High | Account takeover and excessive access |
| Corporate email | High | Phishing and unauthorized mailbox access |
| Linux web server | High | Internet-facing application attack surface |
| Windows endpoints | Medium | Malware and credential theft |
| Remote administration | High | Overly broad management access |

## Risk prioritization method

Likelihood is assessed as **Low / Medium / High**, and potential impact as **Low / Medium / High / Critical**. Priorities below are analyst judgments for this invented environment, not calculated probabilities or validated business-impact values. **Critical** means investigate or mitigate first; **High** means next priority; **Medium** means track and reduce.

| ID | Risk scenario | Likelihood* | Impact* | Priority |
|---|---|---|---|---|
| R1 | Cloud identity compromise | High | High | Critical |
| R2 | Customer database exposure | Medium | Critical | Critical |
| R3 | Phishing and credential theft | High | High | Critical |
| R4 | Web server attack | Medium | High | High |
| R5 | Remote administration exposure | Medium | High | High |
| R6 | Endpoint malware | Medium | Medium | Medium |

*All likelihood and impact assignments are illustrative scenario assumptions.*

## R1 - Cloud identity compromise

**Assets:** Microsoft 365 identities and connected cloud services.  
**Threat scenario:** Password guessing or stolen credentials followed by unauthorized access.  
**Weaknesses to verify:** Password reuse, ineffective MFA or Conditional Access, excessive permissions, insufficient sign-in monitoring. None is proven by the dataset.

**Potential impact:** Unauthorized access to email, cloud applications and sensitive information.  
**Recommended controls:** MFA, Conditional Access, least privilege, sign-in correlation, session revocation and account recovery procedures.

**Relevant case evidence:** The [authentication dataset](sample-data/signin-events.csv) contains six failed attempts followed by a successful sign-in from the same source for one synthetic account. This supports **escalation for possible compromise**, not a confirmed takeover. See [Stage 03](03-authentication-log-analysis.md).

## R2 - Customer database exposure

**Asset:** Customer database.  
**Threat scenario:** Unauthorized reading, modification or disclosure of sensitive records.  
**Weaknesses to verify:** Broad database access, exposed service endpoints, insufficient access review or audit logging.

**Potential impact:** Customer harm, business disruption and compliance implications.  
**Recommended controls:** Role-based least privilege, network segmentation, strong administrator authentication, audit logs, backup and recovery validation.

**Evidence boundary:** The case does **not** contain database access logs or evidence of actual data exposure. This is a preventive risk assessment rather than an observed incident.

## R3 - Phishing and credential theft

**Assets:** Corporate email and employee accounts.  
**Threat scenario:** Deceptive email leads a user to reveal credentials or run malicious content.  
**Weaknesses to verify:** Inadequate email filtering, unsafe link handling, insufficient user reporting processes or weak authentication defenses.

**Potential impact:** Unauthorized mailbox access, identity misuse or endpoint infection.  
**Recommended controls:** Email filtering, sender/domain checks, awareness, phishing-report workflows, MFA and account-activity monitoring.

**Evidence boundary:** No phishing email is supplied in this synthetic integrated dataset. Phishing remains a credible scenario risk, **not an identified entry point**.

## R4 - Web server attack

**Asset:** Linux web server.  
**Threat scenario:** Reconnaissance, credential guessing or exploitation against internet-facing services.  
**Weaknesses to verify:** Exposed administrative pages, missing patches, unnecessary services or weak application access controls.

**Potential impact:** Unauthorized access, service disruption or data exposure.  
**Recommended controls:** Patching, secure configuration, web access logging, rate limiting, restricted administration and firewall review.

**Relevant case evidence:** The [web log](sample-data/access.log) contains rapid requests to common sensitive paths. Another source made repeated login requests; the final HTTP 200 response **does not prove authentication succeeded**. See [Stage 04](04-web-linux-log-analysis.md).

## R5 - Remote administration exposure

**Asset:** Remote administration service.  
**Threat scenario:** Unauthorized actors reach management services through permissive rules or weak access controls.  
**Weaknesses to verify:** Broad source-IP ranges, unneeded management ports, weak authentication or missing monitoring.

**Potential impact:** Unauthorized administrative activity and potential lateral movement.  
**Recommended controls:** Restrict management networks, disable unused services, least-privilege rules, strong authentication and administrative audit logs.

**Evidence boundary:** There is no remote-management firewall export in this case. Excessive exposure is a **hypothesis to validate**, not a confirmed configuration finding.

## R6 - Endpoint malware

**Asset:** Windows endpoints.  
**Threat scenario:** Malicious files execute or steal credentials after a user action or system compromise.  
**Weaknesses to verify:** Missing patches, unnecessary privileges, ineffective endpoint protection or poor logging.

**Potential impact:** Local disruption, credential exposure and further intrusion opportunities.  
**Recommended controls:** Endpoint protection, patching, application control where appropriate, least privilege and investigation-ready logging.

**Evidence boundary:** No endpoint compromise is demonstrated by the fictional Northstar dataset.

## Priority actions

1. **Investigate the cloud sign-in sequence first.** Verify the user's activity, MFA/Conditional Access context, session history and mailbox changes.
2. **Protect high-value assets.** Confirm database permissions, identity access boundaries and recovery readiness.
3. **Review the web attack surface.** Examine sensitive paths, authentication telemetry, patch status and administrative exposure.
4. **Validate the assumed weaknesses.** Do not report missing MFA, exposed ports or compromised endpoints as observed without supporting evidence.
5. **Define monitoring and response ownership.** Route validated findings to the appropriate cloud, endpoint, web and data owners.

## Evidence versus assumptions

| Supported by synthetic case data | Not established by current evidence |
|---|---|
| Six failed cloud sign-ins followed by a success from the same user and source | Confirmed unauthorized account takeover |
| Rapid requests to multiple sensitive web paths | Successful exploitation of the web server |
| Two HTTP 401 responses followed by HTTP 200 on a login endpoint | Successful web application authentication |
| An inventory of fictional business assets | Database theft, active phishing, endpoint malware or an exposed management rule |

The external IPs in this case use documentation-only address ranges, not alleged real threat infrastructure. The cloud and web events are **distinct investigation leads**; they are not attributed to a single attacker.

## Next stage

[02 - Security Controls Mapping](02-security-controls-mapping.md) maps these risks to preventive, detective and corrective controls. The [case overview](README.md) links the full investigation.
