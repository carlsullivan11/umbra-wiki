---
slug: attack-pattern/CAPEC-613
title: "CAPEC-613 — WiFi SSID Tracking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-613]
cwe_ids: [CWE-201, CWE-300]
related: [weakness/CWE-201, weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-613
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients th…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/613.html
---

# CAPEC-613: WiFi SSID Tracking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients that are accessing the network (e.g., the handset/mobile device). Once the attacker is able to associate an SSID with a particular user or set of users (for example, when attending a public event), the attacker can then scan for this SSID to track that user in the future.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201), [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- None

## Skills required

- Low: Open source and commercial software tools are available and open databases of known WiFi SSID addresses are available online.

## Mitigations

- Do not enable the feature of "Hidden SSIDs" (also known as "Network Cloaking") – this option disables the usual broadcasting of the SSID by the access point, but forces the mobile handset to send requests on all supported radio channels which contains the SSID. The result is that tracking of the mobile device becomes easier since it is transmitting the SSID more frequently.
- Frequently change the SSID to new and unrelated values

## Source

- [MITRE CAPEC CAPEC-613](https://capec.mitre.org/data/definitions/613.html)
