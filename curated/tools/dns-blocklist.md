---
slug: tool/dns-blocklist
title: Umbra DNS / Pi-hole blocklists
page_type: tool
tags: [dns, pihole, adguard, blocklist, malware, adult, parental, dnsbl]
related:
  - concept/email-authentication
provenance: curated
updated_at: 2026-08-20
summary: "Free malware and adult-content domain blocklists for Pi-hole, AdGuard Home, and hosts files."
sources:
  - name: abuse.ch URLhaus
    url: https://urlhaus.abuse.ch/
  - name: abuse.ch ThreatFox
    url: https://threatfox.abuse.ch/
  - name: abuse.ch Feodo Tracker
    url: https://feodotracker.abuse.ch/
  - name: Blocklist Project (porn)
    url: https://github.com/blocklistproject/Lists
  - name: StevenBlack hosts (porn-only)
    url: https://github.com/StevenBlack/hosts
---

# Umbra DNS blocklists

Umbra publishes free **DNS blocklists** you can paste into **Pi-hole**,
**AdGuard Home**, **dnsmasq**, or a classic hosts file.

Two independent families:

1. **Malware** — hostnames/IPs from Umbra’s **owned abuse.ch lake** (URLhaus,
   ThreatFox, Feodo). Same CTI collectors use. Not Internet scanning.
2. **Adult content** — domains from public filter projects (Blocklist Project +
   StevenBlack porn lists), mirrored and re-served. Optional parental /
   workplace filter.

## Malware feeds

| Format | URL |
|--------|-----|
| **Domains** (recommended) | `https://umbra-osint.com/lists/malware-domains.txt` |
| **Hosts file** | `https://umbra-osint.com/lists/malware-hosts.txt` |
| **Adblock** | `https://umbra-osint.com/lists/malware-adblock.txt` |
| **IPs** | `https://umbra-osint.com/lists/malware-ips.txt` |

## Adult-content feeds

| Format | URL |
|--------|-----|
| **Domains** (recommended) | `https://umbra-osint.com/lists/adult-domains.txt` |
| **Hosts file** | `https://umbra-osint.com/lists/adult-hosts.txt` |
| **Adblock** | `https://umbra-osint.com/lists/adult-adblock.txt` |

Index of all lists: `https://umbra-osint.com/lists/`

## Pi-hole

1. **Group Management → Adlists**
2. Add one or both:
   ```text
   https://umbra-osint.com/lists/malware-domains.txt
   https://umbra-osint.com/lists/adult-domains.txt
   ```
3. **Tools → Update Gravity**

## AdGuard Home

**Filters → DNS blocklists → Add blocklist** for each URL above.

## What is (and is not) on the lists

**Malware list**

- Hosts from URLhaus / ThreatFox / Feodo in Umbra’s lake

**Adult list**

- Domains classified as adult by upstream open filter projects

**Neither list includes**

- Advertising / tracking (use a dedicated ad list)
- Whole TLDs without a feed hit
- Private / loopback / CGNAT addresses
- Results of Umbra actively probing random Internet hosts

False positives happen on any open list — whitelist locally when needed.

## Attribution

- Malware: **abuse.ch** terms apply to upstream data
- Adult: **Blocklist Project** and **StevenBlack/hosts** (see their repos)
- Umbra packaging: MIT
