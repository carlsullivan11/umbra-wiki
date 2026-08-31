---
slug: attack-pattern/CAPEC-74
title: "CAPEC-74 — Manipulating State"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-74]
cwe_ids: [CWE-315, CWE-353, CWE-372, CWE-693, CWE-1245, CWE-1253, CWE-1265, CWE-1271]
related: [weakness/CWE-315, weakness/CWE-353, weakness/CWE-372, weakness/CWE-693, weakness/CWE-1245, weakness/CWE-1253, weakness/CWE-1265, weakness/CWE-1271]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-74
updated_at: 2026-08-31
summary: "The adversary modifies state information maintained by the target software or causes a state transition in hardware. If successful, the target will use this tainted state and execute in an unintended manner. State management is an important function within a software application.…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/74.html
---

# CAPEC-74: Manipulating State

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary modifies state information maintained by the target software or causes a state transition in hardware. If successful, the target will use this tainted state and execute in an unintended manner. State management is an important function within a software application. User state maintained by the application can include usernames, payment information, browsing history as well as application-specific contents such as items in a shopping cart. Manipulating user state can be employed by an adversary to elevate privilege, conduct fraudulent transactions or otherwise modify the flow of the application to derive certain benefits. If there is a hardware logic error in a finite state machine, the adversary can use this to put the system in an undefined state which could cause a denial of service or exposure of secure data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-315](/wiki/p/weakness/CWE-315), [CWE-353](/wiki/p/weakness/CWE-353), [CWE-372](/wiki/p/weakness/CWE-372), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-1245](/wiki/p/weakness/CWE-1245), [CWE-1253](/wiki/p/weakness/CWE-1253), [CWE-1265](/wiki/p/weakness/CWE-1265), [CWE-1271](/wiki/p/weakness/CWE-1271)

## Prerequisites

- User state is maintained at least in some way in user-controllable locations, such as cookies or URL parameters.
- There is a faulty finite state machine in the hardware logic that can be exploited.

## Skills required

- Medium: The adversary needs to have knowledge of state management as employed by the target application, and also the ability to manipulate the state in a meaningful way.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data
- Availability: Unreliable Execution

## Mitigations

- Do not rely solely on user-controllable locations, such as cookies or URL parameters, to maintain user state.
- Avoid sensitive information, such as usernames or authentication and authorization information, in user-controllable locations.
- Sensitive information that is part of the user state must be appropriately protected to ensure confidentiality and integrity at each request.
- All possible states must be handled by hardware finite state machines.

## Source

- [MITRE CAPEC CAPEC-74](https://capec.mitre.org/data/definitions/74.html)
