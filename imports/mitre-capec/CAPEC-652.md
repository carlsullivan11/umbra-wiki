---
slug: attack-pattern/CAPEC-652
title: "CAPEC-652 — Use of Known Kerberos Credentials"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-652]
cwe_ids: [CWE-262, CWE-263, CWE-294, CWE-307, CWE-308, CWE-309, CWE-522, CWE-654, CWE-836]
mitre_ids: [T1558]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-294, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-522, weakness/CWE-654, weakness/CWE-836, technique/T1558]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-652
updated_at: 2026-08-31
summary: "An adversary obtains (i.e. steals or purchases) legitimate Kerberos credentials (e.g. Kerberos service account userID/password or Kerberos Tickets) with the goal of achieving authenticated access to additional systems, applications, or services within the domain."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/652.html
---

# CAPEC-652: Use of Known Kerberos Credentials

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary obtains (i.e. steals or purchases) legitimate Kerberos credentials (e.g. Kerberos service account userID/password or Kerberos Tickets) with the goal of achieving authenticated access to additional systems, applications, or services within the domain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-522](/wiki/p/weakness/CWE-522), [CWE-654](/wiki/p/weakness/CWE-654), [CWE-836](/wiki/p/weakness/CWE-836)

**ATT&CK techniques:** [T1558](/wiki/p/technique/T1558)

## Prerequisites

- The system/application leverages Kerberos authentication.
- The system/application uses one factor password-based authentication, SSO, and/or cloud-based authentication for Kerberos service accounts.
- The system/application does not have a sound password policy that is being enforced for Kerberos service accounts.
- The system/application does not implement an effective password throttling mechanism for authenticating to Kerberos service accounts.
- The targeted network allows for network sniffing attacks to succeed.

## Skills required

- Low: Once an adversary obtains a known Kerberos credential, leveraging it is trivial.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Create a strong password policy and ensure that your system enforces this policy for Kerberos service accounts.
- Ensure Kerberos service accounts are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse Kerberos service account credentials across systems.
- Deny remote use of Kerberos service account credentials to log into domain systems.
- Do not allow Kerberos service accounts to be a local administrator on more than one system.
- Enable at least AES Kerberos encryption for tickets.
- Monitor system and domain logs for abnormal credential access.

## Source

- [MITRE CAPEC CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
