---
slug: tool/dns-blocklist
title: Umbra DNS / Pi-hole blocklists
page_type: tool
tags: [dns, pihole, adguard, blocklist, malware, dnsbl]
related:
  - concept/email-authentication
provenance: curated
updated_at: 2026-08-20
summary: "Free malware domain blocklists for Pi-hole, AdGuard Home, and hosts files — built from Umbra's owned abuse.ch lake."
sources:
  - name: abuse.ch URLhaus
    url: https://urlhaus.abuse.ch/
  - name: abuse.ch ThreatFox
    url: https://threatfox.abuse.ch/
  - name: abuse.ch Feodo Tracker
    url: https://feodotracker.abuse.ch/
---

# Umbra DNS blocklists

Umbra publishes **malware infrastructure** hostnames and IPs from its **owned
abuse.ch lake** (URLhaus, ThreatFox, Feodo). These are the same public CTI feeds
Umbra already mirrors for collectors — **not** the result of scanning the public
Internet.

Use them with **Pi-hole**, **AdGuard Home**, **dnsmasq**, or a classic hosts file.

## Live feed URLs

| Format | URL | Use with |
|--------|-----|----------|
| **Domains** (recommended) | `https://umbra-osint.com/lists/malware-domains.txt` | Pi-hole adlist, AdGuard DNS blocklist |
| **Hosts file** | `https://umbra-osint.com/lists/malware-hosts.txt` | `/etc/hosts`, dnsmasq `addn-hosts` |
| **Adblock** | `https://umbra-osint.com/lists/malware-adblock.txt` | uBlock Origin / browser lists |
| **IPs** | `https://umbra-osint.com/lists/malware-ips.txt` | Firewall / IP blocking (not pure DNS) |
| Index | `https://umbra-osint.com/lists/` | human-readable pointer |

Lists refresh from the lake on each request (short cache). Keep the **abuse.ch
sync** timer healthy so the lake stays current.

## Pi-hole

1. Open **Group Management → Adlists**
2. Add:
   ```text
   https://umbra-osint.com/lists/malware-domains.txt
   ```
3. **Tools → Update Gravity** (or wait for the next scheduled update)

Optional: use the hosts format if your Pi-hole setup prefers hosts-style lists:

```text
https://umbra-osint.com/lists/malware-hosts.txt
```

## AdGuard Home

**Filters → DNS blocklists → Add blocklist → Add a custom list**

- Name: `Umbra malware domains`
- URL: `https://umbra-osint.com/lists/malware-domains.txt`

## AdGuard / uBlock (browser)

Subscribe to:

```text
https://umbra-osint.com/lists/malware-adblock.txt
```

## What is (and is not) on the list

**On the list**

- Hostnames seen serving malware URLs (URLhaus)
- IOC hosts from ThreatFox
- Botnet C2 IPs from Feodo Tracker

**Not on the list**

- Advertising / tracking (use dedicated ad lists)
- Whole TLDs or “suspicious” heuristics without a feed hit
- Private / loopback / CGNAT addresses
- Results of Umbra **active** probing of random Internet hosts

## Attribution & terms

- Upstream data: **abuse.ch** — respect their [terms](https://abuse.ch/) and
  rate limits. Umbra redistributes a **filtered snapshot** of what it already
  stores for OSINT collectors.
- Blocking is **best-effort CTI**. False positives happen; whitelist locally when
  needed. Absence from the list is **not** a clean bill of health.

## Local / offline

If you run Umbra yourself and the API can see your lake:

```bash
curl -fsS http://localhost:8000/lists/malware-domains.txt | head
```

After `umbra abuse sync`, the list updates on the next fetch (cache ≤ ~15 minutes).
