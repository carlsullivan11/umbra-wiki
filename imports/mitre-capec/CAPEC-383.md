---
slug: attack-pattern/CAPEC-383
title: "CAPEC-383 — Harvesting Information via API Event Monitoring"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-383]
cwe_ids: [CWE-311, CWE-319, CWE-419, CWE-602]
mitre_ids: [T1056.004]
related: [weakness/CWE-311, weakness/CWE-319, weakness/CWE-419, weakness/CWE-602, technique/T1056.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-383
updated_at: 2026-08-31
summary: "An adversary hosts an event within an application framework and then monitors the data exchanged during the course of the event for the purpose of harvesting any important data leaked during the transactions. One example could be harvesting lists of usernames or userIDs for the p…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/383.html
---

# CAPEC-383: Harvesting Information via API Event Monitoring

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary hosts an event within an application framework and then monitors the data exchanged during the course of the event for the purpose of harvesting any important data leaked during the transactions. One example could be harvesting lists of usernames or userIDs for the purpose of sending spam messages to those users. One example of this type of attack involves the adversary creating an event within the sub-application. Assume the adversary hosts a "virtual sale" of rare items. As other users enter the event, the attacker records via AiTM (CAPEC-94) proxy the user_ids and usernames of everyone who attends. The adversary would then be able to spam those users within the application using an automated script.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-319](/wiki/p/weakness/CWE-319), [CWE-419](/wiki/p/weakness/CWE-419), [CWE-602](/wiki/p/weakness/CWE-602)

**ATT&CK techniques:** [T1056.004](/wiki/p/technique/T1056.004)

## Prerequisites

- The target software is utilizing application framework APIs

## Consequences

- Confidentiality: Read Data

## Mitigations

- Leverage encryption techniques during information transactions so as to protect them from attack patterns of this kind.

## Source

- [MITRE CAPEC CAPEC-383](https://capec.mitre.org/data/definitions/383.html)
