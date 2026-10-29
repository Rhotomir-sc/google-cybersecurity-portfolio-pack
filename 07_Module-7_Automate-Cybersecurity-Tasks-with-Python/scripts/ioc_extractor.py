"""Extract candidate IPv4 addresses, domains and SHA-256 digests from text.

This is an educational parser, not a maliciousness verdict or threat-intel feed.
"""
import ipaddress
import re

security_text = """
Suspicious activity was detected from 185.44.21.90.
The process attempted to contact fshjaifhajfa.click.
Another connection was observed to 193.46.217.4.

File SHA256:
d202ed020ed8e36bd8a0f5b571a19d386c12abecb2a28c989d50bbf92c78f54e
"""

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
domain_pattern = r"\b[a-zA-Z0-9.-]+\.(?:com|net|org|click|top|io|thm)\b"
sha256_pattern = r"\b[a-fA-F0-9]{64}\b"


def extract_iocs(text):
    """Return candidate indicators; validate IPv4 octets before reporting.

    Regex only proposes candidates. Domain suffixes are intentionally limited,
    so absence of a match does not mean an input is safe.
    """
    valid_ipv4 = []
    for candidate in re.findall(ip_pattern, text):
        try:
            address = ipaddress.ip_address(candidate)
        except ValueError:
            continue
        if isinstance(address, ipaddress.IPv4Address):
            valid_ipv4.append(candidate)
    domains = re.findall(domain_pattern, text)
    sha256_hashes = re.findall(sha256_pattern, text)
    return {"ip_addresses": valid_ipv4, "domains": domains, "sha256_hashes": sha256_hashes}


# Keep the original demonstration data available to the existing smoke tests.
indicators = extract_iocs(security_text)
ip_addresses = indicators["ip_addresses"]
domains = indicators["domains"]
sha256_hashes = indicators["sha256_hashes"]


def main():
    print("IOC Extraction Results")
    print("======================")
    for title, values in (
        ("IP Addresses", ip_addresses),
        ("Domains", domains),
        ("SHA-256 Hashes", sha256_hashes),
    ):
        print()
        print(title)
        print("-" * len(title))
        for value in values:
            print(value)


if __name__ == "__main__":
    main()
