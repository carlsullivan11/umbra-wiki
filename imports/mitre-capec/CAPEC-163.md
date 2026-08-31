---
slug: attack-pattern/CAPEC-163
title: "CAPEC-163 — Spear Phishing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-163]
cwe_ids: [CWE-451]
mitre_ids: [T1534, T1566.001, T1566.002, T1566.003, T1598.001, T1598.002, T1598.003]
related: [weakness/CWE-451, technique/T1534, technique/T1566.001, technique/T1566.002, technique/T1566.003, technique/T1598.001, technique/T1598.002, technique/T1598.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-163
updated_at: 2026-08-31
summary: "An adversary targets a specific user or group with a Phishing (CAPEC-98) attack tailored to a category of users in order to have maximum relevance and deceptive capability. Spear Phishing is an enhanced version of the Phishing attack targeted to a specific user or group. The qual…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/163.html
---

# CAPEC-163: Spear Phishing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary targets a specific user or group with a Phishing (CAPEC-98) attack tailored to a category of users in order to have maximum relevance and deceptive capability. Spear Phishing is an enhanced version of the Phishing attack targeted to a specific user or group. The quality of the targeted email is usually enhanced by appearing to come from a known or trusted entity. If the email account of some trusted entity has been compromised the message may be digitally signed. The message will contain information specific to the targeted users that will enhance the probability that they will follow the URL to the compromised site. For example, the message may indicate knowledge of the targets employment, residence, interests, or other information that suggests familiarity. As soon as the user follows the instructions in the message, the attack proceeds as a standard Phishing attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-451](/wiki/p/weakness/CWE-451)

**ATT&CK techniques:** [T1534](/wiki/p/technique/T1534), [T1566.001](/wiki/p/technique/T1566.001), [T1566.002](/wiki/p/technique/T1566.002), [T1566.003](/wiki/p/technique/T1566.003), [T1598.001](/wiki/p/technique/T1598.001), [T1598.002](/wiki/p/technique/T1598.002), [T1598.003](/wiki/p/technique/T1598.003)

## Prerequisites

- None. Any user can be targeted by a Spear Phishing attack.

## Skills required

- Medium: Spear phishing attacks require specific knowledge of the victims being targeted, such as which bank is being used by the victims, or websites they commonly log into (Google, Facebook, etc).

## Consequences

- Confidentiality: Read Data
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Source

- [MITRE CAPEC CAPEC-163](https://capec.mitre.org/data/definitions/163.html)
