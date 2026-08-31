---
slug: attack-pattern/CAPEC-98
title: "CAPEC-98 — Phishing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-98]
cwe_ids: [CWE-451]
mitre_ids: [T1566, T1598]
related: [weakness/CWE-451, technique/T1566, technique/T1598]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-98
updated_at: 2026-08-31
summary: "Phishing is a social engineering technique where an attacker masquerades as a legitimate entity with which the victim might do business in order to prompt the user to reveal some confidential information (very frequently authentication credentials) that can later be used by an at…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/98.html
---

# CAPEC-98: Phishing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Phishing is a social engineering technique where an attacker masquerades as a legitimate entity with which the victim might do business in order to prompt the user to reveal some confidential information (very frequently authentication credentials) that can later be used by an attacker. Phishing is essentially a form of information gathering or "fishing" for information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-451](/wiki/p/weakness/CWE-451)

**ATT&CK techniques:** [T1566](/wiki/p/technique/T1566), [T1598](/wiki/p/technique/T1598)

## Prerequisites

- An attacker needs to have a way to initiate contact with the victim. Typically that will happen through e-mail.
- An attacker needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An attacker needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills required

- Medium: Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Source

- [MITRE CAPEC CAPEC-98](https://capec.mitre.org/data/definitions/98.html)
