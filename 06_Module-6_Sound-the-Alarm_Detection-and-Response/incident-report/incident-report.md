# Incident Report - Suspicious Windows Malware Activity

## Incident Summary

A Windows workstation showed unusually high CPU usage.

During investigation, I identified a suspicious executable named:

```text
32th4ckm3.exe
```

running from a temporary user directory.

Further analysis connected the process to a macro-enabled Word document, suspicious network activity, and Registry Run-key persistence.

The incident was handled through detection, analysis, containment, eradication, and recovery.

---

## Environment

| Field | Value |
|---|---|
| Platform | Windows |
| Incident Type | Malware / Suspicious Executable |
| Initial Indicator | High CPU usage |
| Suspicious Process | `32th4ckm3.exe` |
| User | `TryCleanUser` |

---

# Detection

The investigation started after unusually high CPU usage was observed.

Task Manager showed:

```text
32th4ckm3.exe
```

consuming approximately half of the available CPU resources.

The executable was located in:

```text
C:\Users\TryCleanUser\AppData\Local\Temp\2\
```

A randomly named executable running from a temporary directory was considered suspicious and required further investigation.

---

# Analysis

## Network Activity

I identified the process ID and reviewed its network activity using `netstat`.

The process attempted an outbound connection to:

```text
45.33.32.156:42424
```

The connection state was:

```text
SYN_SENT
```

This showed an outbound connection attempt.

I did not treat the state as proof that a complete connection was successfully established.

---

## Infection Vector

Browser download history showed a macro-enabled document:

```text
invoice n. 65748224.docm
```

downloaded from:

```text
http://172.233.61.246
```

The `.docm` file was reviewed as a possible infection vector.

---

## VBA Macro

The document contained an `AutoOpen()` macro.

The code referenced:

```text
http://172.233.61.246/32th4ckm3.exe
```

and used `certutil` to download the executable into the user's temporary directory.

The macro also launched the downloaded executable and configured persistence.

---

## Persistence

I reviewed:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

and identified a value named:

```text
DefaultApp
```

pointing to:

```text
C:\Users\TryCleanUser\AppData\Local\Temp\2\32th4ckm3.exe
```

This confirmed a persistence mechanism through the user's Registry Run key.

---

# Indicators of Compromise

| Type | Indicator |
|---|---|
| Process | `32th4ckm3.exe` |
| Malware Path | `C:\Users\TryCleanUser\AppData\Local\Temp\2\32th4ckm3.exe` |
| Remote Address | `45.33.32.156:42424` |
| Malicious Document | `invoice n. 65748224.docm` |
| Document Source | `http://172.233.61.246` |
| Malware URL | `http://172.233.61.246/32th4ckm3.exe` |
| Registry Key | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| Registry Value | `DefaultApp` |

---

# Containment

After collecting the relevant evidence, I verified that the suspicious process was no longer running.

The purpose of this step was to stop active malicious execution before removing the remaining artefacts.

---

# Eradication

I removed the persistence entry:

```text
DefaultApp
```

from the user's Registry Run key.

I then deleted:

```text
32th4ckm3.exe
```

from the temporary directory.

The original malicious document:

```text
invoice n. 65748224.docm
```

was also removed.

---

# Recovery

After remediation, I verified that:

```text
Suspicious process      → not running
Registry persistence    → removed
Malware executable      → removed
Malicious DOCM          → removed
```

The browser download history associated with the malicious document was also cleared in the lab environment.

---

# Incident Timeline

| Stage | Activity |
|---|---|
| Detection | High CPU usage identified |
| Process Analysis | `32th4ckm3.exe` located in Temp directory |
| Network Analysis | Outbound connection attempt identified |
| Infection Vector | Suspicious `.docm` found |
| Macro Analysis | AutoOpen download and execution logic identified |
| Persistence | Registry Run-key persistence confirmed |
| Containment | Suspicious process stopped |
| Eradication | Persistence and malware artefacts removed |
| Recovery | Removal verified |

---

# Lessons Learned

This investigation showed why deleting a suspicious process immediately is not enough.

If I had removed only the executable, I could have missed:

```text
Original malicious document
Registry persistence
Network indicators
Download infrastructure
```

Collecting evidence first helped reconstruct how the compromise worked.

---

# Response Workflow

```text
Detect
  ↓
Collect evidence
  ↓
Analyse process behaviour
  ↓
Identify infection vector
  ↓
Identify persistence
  ↓
Contain
  ↓
Eradicate
  ↓
Verify recovery
```

---

# Related Hands-On Evidence

The original hands-on investigation is documented in my TryHackMe portfolio:

[07 - Incident Response Journal](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/07-incident-response-journal)

The screenshots remain in the TryHackMe repository so that evidence is not duplicated across portfolio projects.

---

# Key Takeaway

Incident response is stronger when remediation is performed **after** evidence collection and analysis.

Understanding how the malware entered the system, executed, communicated, and persisted provides a more complete response than simply deleting the suspicious file.
