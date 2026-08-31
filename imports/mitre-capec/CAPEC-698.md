---
slug: attack-pattern/CAPEC-698
title: "CAPEC-698 — Install Malicious Extension"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-698]
cwe_ids: [CWE-507, CWE-829]
mitre_ids: [T1176, T1505.004]
related: [weakness/CWE-507, weakness/CWE-829, technique/T1176, technique/T1505.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-698
updated_at: 2026-08-31
summary: "An adversary directly installs or tricks a user into installing a malicious extension into existing trusted software, with the goal of achieving a variety of negative technical impacts."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/698.html
---

# CAPEC-698: Install Malicious Extension

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary directly installs or tricks a user into installing a malicious extension into existing trusted software, with the goal of achieving a variety of negative technical impacts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-507](/wiki/p/weakness/CWE-507), [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1176](/wiki/p/technique/T1176), [T1505.004](/wiki/p/technique/T1505.004)

## Prerequisites

- The adversary must craft malware based on the type of software and system(s) they intend to exploit.
- If the adversary intends to install the malicious extension themself, they must first compromise the target machine via some other means.

## Skills required

- Medium: Ability to create malicious extensions that can exploit specific software applications and systems.
- Medium: Optional: Ability to exploit target system(s) via other means in order to gain entry.

## Consequences

- Confidentiality, Access Control: Read Data
- Integrity, Access Control: Modify Data
- Authorization, Access Control: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations

- Only install extensions/plugins from official/verifiable sources.
- Confirm extensions/plugins are legitimate and not malware masquerading as a legitimate extension/plugin.
- Ensure the underlying software leveraging the extension/plugin (including operating systems) is up-to-date.
- Implement an extension/plugin allow list, based on the given security policy.
- If applicable, confirm extensions/plugins are properly signed by the official developers.
- For web browsers, close sessions when finished to prevent malicious extensions/plugins from executing the the background.

## Source

- [MITRE CAPEC CAPEC-698](https://capec.mitre.org/data/definitions/698.html)
