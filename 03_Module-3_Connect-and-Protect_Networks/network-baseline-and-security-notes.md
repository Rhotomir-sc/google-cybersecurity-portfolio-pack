# Network baseline — collection pending

The old evidence image files were one-byte placeholders. A verifiable local baseline is still pending.

## Collection procedure
On an authorized Windows lab host, record the date, timezone, network profile, and host role. Run:

```powershell
ipconfig /all
Get-NetTCPConnection | Sort-Object State,LocalPort
Get-NetUDPEndpoint | Sort-Object LocalPort
```

Save selected output or screenshots after reviewing personal information. Label redactions. Explain unexpected listeners using process and service context.

| Observation | Baseline | Evidence | Follow-up |
|---|---|---|---|
| IP / DNS / gateway | Pending | Pending | Confirm network context |
| TCP listeners/connections | Pending | Pending | Identify owning process and purpose |
| UDP endpoints | Pending | Pending | Identify owning process and purpose |

These commands are a procedure, not evidence of execution.
[Evidence status](evidence/README.md) · [Artifact index](../ARTIFACTS.md)
