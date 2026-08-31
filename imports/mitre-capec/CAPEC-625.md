---
slug: attack-pattern/CAPEC-625
title: "CAPEC-625 — Mobile Device Fault Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-625]
cwe_ids: [CWE-1247, CWE-1248, CWE-1256, CWE-1319, CWE-1332, CWE-1334, CWE-1338, CWE-1351]
related: [weakness/CWE-1247, weakness/CWE-1248, weakness/CWE-1256, weakness/CWE-1319, weakness/CWE-1332, weakness/CWE-1334, weakness/CWE-1338, weakness/CWE-1351]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-625
updated_at: 2026-08-31
summary: "Fault injection attacks against mobile devices use disruptive signals or events (e.g. electromagnetic pulses, laser pulses, clock glitches, etc.) to cause faulty behavior. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior c…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/625.html
---

# CAPEC-625: Mobile Device Fault Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Fault injection attacks against mobile devices use disruptive signals or events (e.g. electromagnetic pulses, laser pulses, clock glitches, etc.) to cause faulty behavior. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information. Although this attack usually requires physical control of the mobile device, it is non-destructive, and the device can be used after the attack without any indication that secret keys were compromised.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1247](/wiki/p/weakness/CWE-1247), [CWE-1248](/wiki/p/weakness/CWE-1248), [CWE-1256](/wiki/p/weakness/CWE-1256), [CWE-1319](/wiki/p/weakness/CWE-1319), [CWE-1332](/wiki/p/weakness/CWE-1332), [CWE-1334](/wiki/p/weakness/CWE-1334), [CWE-1338](/wiki/p/weakness/CWE-1338), [CWE-1351](/wiki/p/weakness/CWE-1351)

## Skills required

- High: Adversaries require non-trivial technical skills to create and implement fault injection attacks on mobile devices. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required. This prerequisite makes the attack challenging to perform (assuming that physical security countermeasures and monitoring are in place).

## Consequences

- Confidentiality, Access Control: Read Data

## Mitigations

- Strong physical security of all devices that contain secret key information. (even when devices are not in use)
- Frequent changes to secret keys and certificates.

## Source

- [MITRE CAPEC CAPEC-625](https://capec.mitre.org/data/definitions/625.html)
