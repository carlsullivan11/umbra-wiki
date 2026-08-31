---
slug: attack-pattern/CAPEC-222
title: "CAPEC-222 — iFrame Overlay"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-222]
cwe_ids: [CWE-1021]
related: [weakness/CWE-1021]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-222
updated_at: 2026-08-31
summary: "In an iFrame overlay attack the victim is tricked into unknowingly initiating some action in one system while interacting with the UI from seemingly completely different system."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/222.html
---

# CAPEC-222: iFrame Overlay

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In an iFrame overlay attack the victim is tricked into unknowingly initiating some action in one system while interacting with the UI from seemingly completely different system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

## Prerequisites

- The victim is communicating with the target application via a web based UI and not a thick client. The victim's browser security policies allow iFrames. The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser). The victim has an active session with the target system. The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system.

## Skills required

- High: Crafting the proper malicious site and luring the victim to this site is not a trivial task.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Configuration: Disable iFrames in the Web browser.
- Operation: When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.
- Operation: If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.

## Source

- [MITRE CAPEC CAPEC-222](https://capec.mitre.org/data/definitions/222.html)
