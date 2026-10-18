# Module 3 - Connect and Protect: Networks and Network Security

**Evidence status:** local network baseline capture is pending. See the [collection procedure](network-baseline-and-security-notes.md). Existing concept notes are not a completed capture.


| Information | Details |
|---|---|
| Course | Connect and Protect: Networks and Network Security |
| Program | Google Cybersecurity Professional Certificate |
| Focus | Networking, Traffic Analysis & Network Defense |
| Status | Completed |

---

## Overview

This module focused on how computer networks operate and how network activity can be analysed from a security perspective.

I learned how systems communicate using IP addresses, ports, protocols, DNS, and routing, and how defenders can use this information to identify suspicious or unexpected activity.

The main topics I focused on were:

- network architecture
- TCP/IP
- ports and protocols
- DNS
- network traffic
- firewalls
- VPNs
- network segmentation
- network monitoring
- security baselines

---

## Key Networking Concepts

### IP Addresses

IP addresses identify systems on a network.

During an investigation, source and destination IP addresses can help answer:

```text
Who initiated the connection?
Where was the connection going?
Is the destination expected?
```

---

### Ports and Services

Ports help identify which network service is being used.

Examples include:

```text
22   → SSH
53   → DNS
80   → HTTP
443  → HTTPS
445  → SMB
3389 → RDP
```

An open port is not automatically malicious, but unexpected or unnecessary exposed services can increase attack surface.

---

### DNS

DNS translates domain names into IP addresses.

From a security perspective, DNS logs can help identify:

- unusual domains
- suspicious lookups
- malware infrastructure
- unexpected external destinations

---

### TCP and UDP

I learned the difference between connection-oriented TCP traffic and connectionless UDP traffic.

Understanding the transport protocol provides useful context when analysing network behaviour.

---

## Network Baseline

One of the practical concepts I documented was creating a simple network baseline.

See:

[Network Baseline & Security Notes](network-baseline-and-security-notes.md)

The baseline included:

- IP configuration
- DNS information
- default gateway
- active connections
- listening ports

The purpose of a baseline is to understand what is normal before investigating what is unusual.

---

## Baseline Approach

The planned baseline investigation follows:

```text
Establish normal network state
        ↓
Review active connections
        ↓
Review listening ports
        ↓
Identify anomalies
        ↓
Correlate with endpoint evidence
```

This helps reduce false assumptions during network investigations.

---

## Evidence

The previous image link pointed to a one-byte placeholder. No usable baseline capture is currently available here.

Follow the [collection procedure](network-baseline-and-security-notes.md), then add the actual output and its interpretation. [Evidence status](evidence/README.md).

---

## Network Security Controls

This module introduced several controls used to protect networks.

### Firewalls

Firewalls can allow or block network traffic based on rules such as:

```text
Source
Destination
Protocol
Port
Direction
```

A firewall rule should normally be as restrictive as practical while still allowing required business traffic.

---

### Network Segmentation

Segmentation separates systems or services into different network zones.

This can reduce the impact of compromise by limiting unnecessary communication between systems.

---

### VPNs

VPNs can provide encrypted communication across untrusted networks and are commonly used for secure remote access.

---

### Secure Protocols

Where possible, encrypted protocols should be preferred over plaintext alternatives.

Examples:

```text
HTTPS instead of HTTP
SSH instead of Telnet
SFTP instead of FTP
```

---

## Monitoring Network Activity

Network monitoring can help identify:

- unexpected external connections
- unusual ports
- repeated connection attempts
- suspicious DNS activity
- unusual traffic patterns
- exposed services

However, network findings should be analysed in context.

For example:

```text
Connection to unusual IP
```

does not automatically mean:

```text
Confirmed malicious traffic
```

Additional evidence may be required.

---

## Related TryHackMe Practice

I reinforced this module with several hands-on labs from my TryHackMe portfolio.

### Wireshark Traffic Analysis

[03 - Wireshark Traffic Analysis](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/03-wireshark-traffic-analysis)

I used Wireshark filters to analyse:

- FTP traffic
- failed FTP authentication
- HTTP requests
- protocol distribution

This reinforced packet inspection and protocol analysis.

---

### Nmap Host Discovery

[04 - Nmap Host Discovery](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/04-nmap-host-discovery)

I compared several Nmap discovery methods and identified live hosts and exposed services.

This reinforced:

- host discovery
- network reconnaissance
- port awareness
- interpreting scan results carefully

---

### Firewall Rule Audit

[11 - Firewall Rule Audit](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/11-firewall-rule-audit)

I reviewed Windows firewall profiles and identified an overly permissive WinRM rule.

This reinforced:

- network access control
- inbound rules
- source restrictions
- attack-surface reduction

---

## What I Practiced

During this module, I practiced:

- understanding TCP/IP fundamentals
- identifying common ports and protocols
- reviewing IP configuration
- establishing a simple network baseline
- identifying active and listening network services
- understanding DNS from a security perspective
- analysing network traffic concepts
- understanding firewall rules
- understanding VPNs and segmentation
- distinguishing expected from unexpected network activity
- connecting network findings with endpoint evidence

---

## Key Takeaways

### 1. Baselines make anomalies easier to identify

It is difficult to decide whether network activity is suspicious without first understanding normal behaviour.

---

### 2. Ports require context

An open port may be legitimate.

The important questions are:

```text
Should this service be exposed?
Who can reach it?
Is the service required?
```

---

### 3. Network evidence should be correlated

A suspicious IP, DNS query, or connection becomes stronger evidence when it can be connected to:

- a process
- a user
- an authentication event
- a known indicator
- a security alert

---

### 4. Network controls reduce attack surface

Firewalls, segmentation, secure protocols, and controlled remote access can reduce unnecessary exposure.

---

## Result

This module helped me build a stronger understanding of how networks operate and how defenders can analyse network activity.

I created a simple network baseline, reviewed common network indicators, and connected the concepts with hands-on Wireshark, Nmap, and firewall auditing practice.

The most important lesson was that network security is not only about identifying connections.

It is also about understanding what normal communication looks like, reducing unnecessary exposure, and correlating network evidence with other security data.

---

## Next Step

Module 4 focuses on Linux and SQL as practical tools for cybersecurity analysis and system administration.
