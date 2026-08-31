---
slug: attack-pattern/CAPEC-645
title: "CAPEC-645 — Use of Captured Tickets (Pass The Ticket)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-645]
cwe_ids: [CWE-294, CWE-308, CWE-522]
mitre_ids: [T1550.003]
related: [weakness/CWE-294, weakness/CWE-308, weakness/CWE-522, technique/T1550.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-645
updated_at: 2026-08-31
summary: "An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested serv…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/645.html
---

# CAPEC-645: Use of Captured Tickets (Pass The Ticket)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. An adversary can obtain any one of these tickets (e.g. Service Ticket, Ticket Granting Ticket, Silver Ticket, or Golden Ticket) to authenticate to a system/resource without needing the account's credentials. Depending on the ticket obtained, the adversary may be able to access a particular resource or generate TGTs for any account within an Active Directory Domain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-294](/wiki/p/weakness/CWE-294), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1550.003](/wiki/p/technique/T1550.003)

## Prerequisites

- The adversary needs physical access to the victim system.
- The use of a third-party credential harvesting tool.

## Skills required

- Low: Determine if Kerberos authentication is used on the server.
- High: The adversary uses a third-party tool to obtain the necessary tickets to execute the attack.

## Consequences

- Integrity: Gain Privileges

## Mitigations

- Reset the built-in KRBTGT account password twice to invalidate the existence of any current Golden Tickets and any tickets derived from them.
- Monitor system and domain logs for abnormal access.

## Source

- [MITRE CAPEC CAPEC-645](https://capec.mitre.org/data/definitions/645.html)
