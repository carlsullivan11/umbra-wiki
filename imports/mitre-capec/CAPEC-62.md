---
slug: attack-pattern/CAPEC-62
title: "CAPEC-62 — Cross Site Request Forgery"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-62]
cwe_ids: [CWE-306, CWE-352, CWE-664, CWE-732, CWE-1275]
related: [weakness/CWE-306, weakness/CWE-352, weakness/CWE-664, weakness/CWE-732, weakness/CWE-1275]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-62
updated_at: 2026-08-31
summary: "An attacker crafts malicious web links and distributes them (via web pages, email, etc.), typically in a targeted manner, hoping to induce users to click on the link and execute the malicious action against some third-party application. If successful, the action embedded in the m…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/62.html
---

# CAPEC-62: Cross Site Request Forgery

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker crafts malicious web links and distributes them (via web pages, email, etc.), typically in a targeted manner, hoping to induce users to click on the link and execute the malicious action against some third-party application. If successful, the action embedded in the malicious link will be processed and accepted by the targeted application with the users' privilege level. This type of attack leverages the persistence and implicit trust placed in user session cookies by many web applications today. In such an architecture, once the user authenticates to an application and a session cookie is created on the user's system, all following transactions for that session are authenticated using that cookie including potential actions initiated by an attacker and simply "riding" the existing session cookie.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-306](/wiki/p/weakness/CWE-306), [CWE-352](/wiki/p/weakness/CWE-352), [CWE-664](/wiki/p/weakness/CWE-664), [CWE-732](/wiki/p/weakness/CWE-732), [CWE-1275](/wiki/p/weakness/CWE-1275)

## Skills required

- Medium: The attacker needs to figure out the exact invocation of the targeted malicious action and then craft a link that performs the said action. Having the user click on such a link is often accomplished by sending an email or posting such a link to a bulletin board or the likes.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Use cryptographic tokens to associate a request with a specific action. The token can be regenerated at every request so that if a request with an invalid token is encountered, it can be reliably discarded. The token is considered invalid if it arrived with a request other than the action it was supposed to be associated with.
- Although less reliable, the use of the optional HTTP Referrer header can also be used to determine whether an incoming request was actually one that the user is authorized for, in the current context.
- Additionally, the user can also be prompted to confirm an action every time an action concerning potentially sensitive data is invoked. This way, even if the attacker manages to get the user to click on a malicious link and request the desired action, the user has a chance to recover by denying confirmation. This solution is also implicitly tied to using a second factor of authentication before performing such actions.
- In general, every request must be checked for the appropriate authentication token as well as authorization in the current session context.

## Source

- [MITRE CAPEC CAPEC-62](https://capec.mitre.org/data/definitions/62.html)
