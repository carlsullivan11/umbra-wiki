---
slug: attack-pattern/CAPEC-60
title: "CAPEC-60 — Reusing Session IDs (aka Session Replay)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-60]
cwe_ids: [CWE-200, CWE-285, CWE-290, CWE-294, CWE-346, CWE-384, CWE-488, CWE-539, CWE-664, CWE-732]
mitre_ids: [T1134.001, T1550.004]
related: [weakness/CWE-200, weakness/CWE-285, weakness/CWE-290, weakness/CWE-294, weakness/CWE-346, weakness/CWE-384, weakness/CWE-488, weakness/CWE-539, weakness/CWE-664, weakness/CWE-732, technique/T1134.001, technique/T1550.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-60
updated_at: 2026-08-31
summary: "This attack targets the reuse of valid session ID to spoof the target system in order to gain privileges. The attacker tries to reuse a stolen session ID used previously during a transaction to perform spoofing and session hijacking. Another name for this type of attack is Sessio…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/60.html
---

# CAPEC-60: Reusing Session IDs (aka Session Replay)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the reuse of valid session ID to spoof the target system in order to gain privileges. The attacker tries to reuse a stolen session ID used previously during a transaction to perform spoofing and session hijacking. Another name for this type of attack is Session Replay.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-384](/wiki/p/weakness/CWE-384), [CWE-488](/wiki/p/weakness/CWE-488), [CWE-539](/wiki/p/weakness/CWE-539), [CWE-664](/wiki/p/weakness/CWE-664), [CWE-732](/wiki/p/weakness/CWE-732)

**ATT&CK techniques:** [T1134.001](/wiki/p/technique/T1134.001), [T1550.004](/wiki/p/technique/T1550.004)

## Prerequisites

- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are not well protected from session theft.

## Skills required

- Low: If an attacker can steal a valid session ID, they can then try to be authenticated with that stolen session ID.
- Medium: More sophisticated attack can be used to hijack a valid session from a user and spoof a legitimate user by reusing their valid session ID.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Always invalidate a session ID after the user logout.
- Setup a session time out for the session IDs.
- Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate adversary in the middle attacks (CAPEC-94).
- Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.
- Encrypt the session data associated with the session ID.
- Use multifactor authentication.

## Source

- [MITRE CAPEC CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
