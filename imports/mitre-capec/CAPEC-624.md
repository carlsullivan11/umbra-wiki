---
slug: attack-pattern/CAPEC-624
title: "CAPEC-624 — Hardware Fault Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-624]
cwe_ids: [CWE-1247, CWE-1248, CWE-1256, CWE-1319, CWE-1332, CWE-1334, CWE-1338, CWE-1351]
related: [weakness/CWE-1247, weakness/CWE-1248, weakness/CWE-1256, weakness/CWE-1319, weakness/CWE-1332, weakness/CWE-1334, weakness/CWE-1338, weakness/CWE-1351]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-624
updated_at: 2026-08-31
summary: "The adversary uses disruptive signals or events, or alters the physical environment a device operates in, to cause faulty behavior in electronic devices. This can include electromagnetic pulses, laser pulses, clock glitches, ambient temperature extremes, and more. When performed …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/624.html
---

# CAPEC-624: Hardware Fault Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary uses disruptive signals or events, or alters the physical environment a device operates in, to cause faulty behavior in electronic devices. This can include electromagnetic pulses, laser pulses, clock glitches, ambient temperature extremes, and more. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1247](/wiki/p/weakness/CWE-1247), [CWE-1248](/wiki/p/weakness/CWE-1248), [CWE-1256](/wiki/p/weakness/CWE-1256), [CWE-1319](/wiki/p/weakness/CWE-1319), [CWE-1332](/wiki/p/weakness/CWE-1332), [CWE-1334](/wiki/p/weakness/CWE-1334), [CWE-1338](/wiki/p/weakness/CWE-1338), [CWE-1351](/wiki/p/weakness/CWE-1351)

## Prerequisites

- Physical access to the system
- The adversary must be cognizant of where fault injection vulnerabilities exist in the system in order to leverage them for exploitation.

## Skills required

- High: Adversaries require non-trivial technical skills to create and implement fault injection attacks. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required.

## Consequences

- Confidentiality: Read Data, Bypass Protection Mechanism, Hide Activities
- Integrity: Execute Unauthorized Commands

## Mitigations

- Implement robust physical security countermeasures and monitoring.

## Source

- [MITRE CAPEC CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
