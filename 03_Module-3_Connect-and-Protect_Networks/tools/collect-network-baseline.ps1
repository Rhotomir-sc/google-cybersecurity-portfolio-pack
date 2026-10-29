#requires -Version 5.1
<#
.SYNOPSIS
Collects a minimized, read-only local TCP/UDP listening-endpoint snapshot.
.DESCRIPTION
Windows PowerShell 5.1+ with NetTCPIP cmdlets. Does NOT change firewall or
network configuration. Does NOT export local/remote IPs, hostnames, usernames,
process IDs, executable names, DNS details, or credentials. Port and binding
scope can still be sensitive; review locally before sharing.
#>
[CmdletBinding()]
param(
    [string] $OutputPath = (Join-Path $env:TEMP (
        'module3-network-baseline-' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffZ') + '.json'
    ))
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-BindScope {
    param([Parameter(Mandatory = $true)][string] $Address)
    try {
        $parsed = [System.Net.IPAddress]::Parse($Address)
        if ($parsed.Equals([System.Net.IPAddress]::Any) -or
            $parsed.Equals([System.Net.IPAddress]::IPv6Any)) {
            return 'wildcard'
        }
        if ([System.Net.IPAddress]::IsLoopback($parsed)) {
            return 'loopback'
        }
        return 'specific'
    }
    catch {
        # Do not serialize unrecognized addresses to avoid leaking them.
        return 'unknown'
    }
}

if (Test-Path -LiteralPath $OutputPath) {
    throw "Output already exists; choose a new -OutputPath. No file was overwritten."
}

# If either command fails, stop without creating a partial or misleading snapshot.
$tcp = @(Get-NetTCPConnection -State Listen -ErrorAction Stop)
$udp = @(Get-NetUDPEndpoint -ErrorAction Stop)

$entries = @()
foreach ($entry in $tcp) {
    $entries += [PSCustomObject]@{
        protocol = 'tcp'
        port = [int]$entry.LocalPort
        bind_scope = (Get-BindScope -Address ([string]$entry.LocalAddress))
    }
}
foreach ($entry in $udp) {
    $entries += [PSCustomObject]@{
        protocol = 'udp'
        port = [int]$entry.LocalPort
        bind_scope = (Get-BindScope -Address ([string]$entry.LocalAddress))
    }
}

$uniqueEntries = @($entries | Sort-Object -Property protocol, port, bind_scope -Unique)
$snapshot = [ordered]@{
    schema_version = 1
    source = 'local-windows-readonly-collector'
    captured_at_utc = [DateTime]::UtcNow.ToString('o')
    scope = 'listening_tcp_and_local_udp_endpoints_only'
    endpoints = $uniqueEntries
}

$json = ConvertTo-Json -InputObject $snapshot -Depth 6
$folder = Split-Path -Path $OutputPath -Parent
if ($folder -and -not (Test-Path -LiteralPath $folder)) {
    throw "Output directory does not exist: $folder"
}
# PS 5.1 emits UTF-8 BOM; the companion Python reader accepts UTF-8 with BOM.
$json | Set-Content -LiteralPath $OutputPath -Encoding UTF8 -ErrorAction Stop
Write-Host "Saved minimized local snapshot: $OutputPath"
Write-Host "Unique listening/bound endpoints: $($uniqueEntries.Count)"
Write-Host 'Inspect port numbers before any sharing. No network settings were changed.'
