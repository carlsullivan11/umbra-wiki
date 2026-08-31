---
slug: attack-pattern/CAPEC-229
title: "CAPEC-229 — Serialized Data Parameter Blowup"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-229]
cwe_ids: [CWE-770]
related: [weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-229
updated_at: 2026-08-31
summary: "This attack exploits certain serialized data parsers (e.g., XML, YAML, etc.) which manage data in an inefficient manner. The attacker crafts an serialized data file with multiple configuration parameters in the same dataset. In a vulnerable parser, this results in a denial of ser…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/229.html
---

# CAPEC-229: Serialized Data Parameter Blowup

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack exploits certain serialized data parsers (e.g., XML, YAML, etc.) which manage data in an inefficient manner. The attacker crafts an serialized data file with multiple configuration parameters in the same dataset. In a vulnerable parser, this results in a denial of service condition where CPU resources are exhausted because of the parsing algorithm. The weakness being exploited is tied to parser implementation and not language specific.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- The server accepts input in the form of serialized data and is using a parser with a runtime longer than O(n) for the insertion of a new configuration parameter in the data container.(examples are .NET framework 1.0 and 1.1)

## Mitigations

- This attack may be mitigated completely by using a parser that is not using a vulnerable container.
- Mitigation may limit the number of configuration parameters per dataset.

## Source

- [MITRE CAPEC CAPEC-229](https://capec.mitre.org/data/definitions/229.html)
