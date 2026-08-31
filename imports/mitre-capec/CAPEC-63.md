---
slug: attack-pattern/CAPEC-63
title: "CAPEC-63 — Cross-Site Scripting (XSS)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-63]
cwe_ids: [CWE-20, CWE-79]
related: [weakness/CWE-20, weakness/CWE-79]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-63
updated_at: 2026-08-31
summary: "An adversary embeds malicious scripts in content that will be served to web browsers. The goal of the attack is for the target software, the client-side browser, to execute the script with the users' privilege level. An attack of this type exploits a programs' vulnerabilities tha…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/63.html
---

# CAPEC-63: Cross-Site Scripting (XSS)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary embeds malicious scripts in content that will be served to web browsers. The goal of the attack is for the target software, the client-side browser, to execute the script with the users' privilege level. An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute code and scripts. Web browsers, for example, have some simple security controls in place, but if a remote attacker is allowed to execute scripts (through injecting them in to user-generated content like bulletin boards) then these controls may be bypassed. Further, these attacks are very difficult for an end user to detect.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-79](/wiki/p/weakness/CWE-79)

## Prerequisites

- Target client software must be a client that allows scripting communication from remote hosts, such as a JavaScript-enabled Web Browser.

## Skills required

- Low: To achieve a redirection and use of less trusted source, an attacker can simply place a script in bulletin board, blog, wiki, or other user-generated content site that are echoed back to other client machines.
- High: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Source

- [MITRE CAPEC CAPEC-63](https://capec.mitre.org/data/definitions/63.html)
