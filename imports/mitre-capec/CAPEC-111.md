---
slug: attack-pattern/CAPEC-111
title: "CAPEC-111 — JSON Hijacking (aka JavaScript Hijacking)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-111]
cwe_ids: [CWE-345, CWE-346, CWE-352]
related: [weakness/CWE-345, weakness/CWE-346, weakness/CWE-352]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-111
updated_at: 2026-08-31
summary: "An attacker targets a system that uses JavaScript Object Notation (JSON) as a transport mechanism between the client and the server (common in Web 2.0 systems using AJAX) to steal possibly confidential information transmitted from the server back to the client inside the JSON obj…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/111.html
---

# CAPEC-111: JSON Hijacking (aka JavaScript Hijacking)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker targets a system that uses JavaScript Object Notation (JSON) as a transport mechanism between the client and the server (common in Web 2.0 systems using AJAX) to steal possibly confidential information transmitted from the server back to the client inside the JSON object by taking advantage of the loophole in the browser's Same Origin Policy that does not prohibit JavaScript from one website to be included and executed in the context of another website.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-352](/wiki/p/weakness/CWE-352)

## Prerequisites

- JSON is used as a transport mechanism between the client and the server
- The target server cannot differentiate real requests from forged requests
- The JSON object returned from the server can be accessed by the attackers' malicious code via a script tag

## Skills required

- Medium: Once this attack pattern is developed and understood, creating an exploit is not very complex.The attacker needs to have knowledge of the URLs that need to be accessed on the target system to request the JSON objects.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Ensure that server side code can differentiate between legitimate requests and forged requests. The solution is similar to protection against Cross Site Request Forger (CSRF), which is to use a hard to guess random nonce (that is unique to the victim's session with the server) that the attacker has no way of knowing (at least in the absence of other weaknesses). Each request from the client to the server should contain this nonce and the server should reject all requests that do not contain the nonce.
- On the client side, the system's design could make it difficult to get access to the JSON object content via the script tag. Since the JSON object is never assigned locally to a variable, it cannot be readily modified by the attacker before being used by a script tag. For instance, if while(1) was added to the beginning of the JavaScript returned by the server, trying to access it with a script tag would result in an infinite loop. On the other hand, legitimate client side code can remove the while(1) statement after which the JavaScript can be evaluated. A similar result can be achieved by surrounding the returned JavaScript with comment tags, or using other similar techniques (e.g. wrapping the JavaScript with HTML tags).
- Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session.
- Ensure that to the extent possible, no sensitive data is passed from the server to the client via JSON objects. JavaScript was never intended to play that role, hence the same origin policy does not adequate address this scenario.

## Source

- [MITRE CAPEC CAPEC-111](https://capec.mitre.org/data/definitions/111.html)
