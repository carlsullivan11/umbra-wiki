---
slug: attack-pattern/CAPEC-42
title: "CAPEC-42 — MIME Conversion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-42]
cwe_ids: [CWE-20, CWE-74, CWE-119, CWE-120]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-119, weakness/CWE-120]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-42
updated_at: 2026-08-31
summary: "An attacker exploits a weakness in the MIME conversion routine to cause a buffer overflow and gain control over the mail server machine. The MIME system is designed to allow various different information formats to be interpreted and sent via e-mail. Attack points exist when data…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/42.html
---

# CAPEC-42: MIME Conversion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a weakness in the MIME conversion routine to cause a buffer overflow and gain control over the mail server machine. The MIME system is designed to allow various different information formats to be interpreted and sent via e-mail. Attack points exist when data are converted to MIME compatible format and back.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120)

## Prerequisites

- The target system uses a mail server.
- Mail server vendor has not released a patch for the MIME conversion routine, the patch itself has a security hole or does not fix the original problem, or the patch has not been applied to the user's system.

## Skills required

- Low: It may be trivial to cause a DoS via this attack pattern
- High: Causing arbitrary code to execute on the target system.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Availability: Unreliable Execution
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Stay up to date with third party vendor patches
- Disable the 7 to 8 bit conversion. This can be done by removing the F=9 flag from all Mailer specifications in the sendmail.cf file. For example, a sendmail.cf file with these changes applied should look similar to (depending on your system and configuration): Mlocal, P=/usr/libexec/mail.local, F=lsDFMAw5:/|@qrmn, S=10/30, R=20/40,T=DNS/RFC822/X-Unix,A=mail -d $u Mprog, P=/bin/sh, F=lsDFMoqeu, S=10/30, R=20/40,D=$z:/,T=X-Unix,A=sh -c $u This can be achieved for the "Mlocal" and "Mprog" Mailers by modifying the ".mc" file to include the following lines: define(`LOCAL_MAILER_FLAGS',ifdef(`LOCAL_MAILER_FLAGS',`translit(LOCAL_MAILER_FLAGS, `9')',`rmn')) define(`LOCAL_SHELL_FLAGS',ifdef(`LOCAL_SHELL_FLAGS',`translit(LOCAL_SHELL_FLAGS, `9')',`eu')) and then rebuilding the sendmail.cf file using m4(1). From "Exploiting Software", please see reference below.
- Use the sendmail restricted shell program (smrsh)
- Use mail.local

## Source

- [MITRE CAPEC CAPEC-42](https://capec.mitre.org/data/definitions/42.html)
