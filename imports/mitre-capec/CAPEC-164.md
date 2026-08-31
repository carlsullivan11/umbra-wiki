---
slug: attack-pattern/CAPEC-164
title: "CAPEC-164 — Mobile Phishing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-164]
cwe_ids: [CWE-451]
related: [weakness/CWE-451]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-164
updated_at: 2026-08-31
summary: "An adversary targets mobile phone users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Mobile Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a text or SMS messa…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/164.html
---

# CAPEC-164: Mobile Phishing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary targets mobile phone users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Mobile Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a text or SMS message, rather than email. The user is enticed to provide information or visit a compromised web site via this message. Apart from the manner in which the attack is initiated, the attack proceeds as a standard Phishing attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-451](/wiki/p/weakness/CWE-451)

## Prerequisites

- An adversary needs mobile phone numbers to initiate contact with the victim.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills required

- Medium: Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Do not follow any links that you receive within text messages and do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. Safe practices also include leveraging the entity's mobile application or directly typing the entity's URL in the browser and only then logging in. Never reply to any text messages that ask you to provide sensitive information of any kind.

## Source

- [MITRE CAPEC CAPEC-164](https://capec.mitre.org/data/definitions/164.html)
