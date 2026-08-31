---
slug: attack-pattern/CAPEC-133
title: "CAPEC-133 — Try All Common Switches"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-133]
cwe_ids: [CWE-912]
related: [weakness/CWE-912]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-133
updated_at: 2026-08-31
summary: "An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal se…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/133.html
---

# CAPEC-133: Try All Common Switches

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal sensitive processing or configuration information to an attacker. This attack differs from other forms of API abuse in that the attacker is indiscriminately attempting to invoke options in the hope that one of them will work rather than specifically targeting a known option. Nonetheless, even if the attacker is familiar with the published options of a targeted application this attack method may still be fruitful as it might discover unpublicized functionality.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-912](/wiki/p/weakness/CWE-912)

## Prerequisites

- The attacker must be able to control the options or switches sent to the target.

## Mitigations

- Design: Minimize switch and option functionality to only that necessary for correct function of the command.
- Implementation: Remove all debug and testing options from production code.

## Source

- [MITRE CAPEC CAPEC-133](https://capec.mitre.org/data/definitions/133.html)
