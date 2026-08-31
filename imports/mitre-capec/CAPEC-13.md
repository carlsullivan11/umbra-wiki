---
slug: attack-pattern/CAPEC-13
title: "CAPEC-13 — Subverting Environment Variable Values"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-13]
cwe_ids: [CWE-15, CWE-20, CWE-73, CWE-74, CWE-200, CWE-285, CWE-302, CWE-353]
mitre_ids: [T1562.003, T1574.006, T1574.007]
related: [weakness/CWE-15, weakness/CWE-20, weakness/CWE-73, weakness/CWE-74, weakness/CWE-200, weakness/CWE-285, weakness/CWE-302, weakness/CWE-353, technique/T1574.006, technique/T1574.007]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-13
updated_at: 2026-08-31
summary: "The adversary directly or indirectly modifies environment variables used by or controlling the target software. The adversary's goal is to cause the target software to deviate from its expected operation in a manner that benefits the adversary."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/13.html
---

# CAPEC-13: Subverting Environment Variable Values

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary directly or indirectly modifies environment variables used by or controlling the target software. The adversary's goal is to cause the target software to deviate from its expected operation in a manner that benefits the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-20](/wiki/p/weakness/CWE-20), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-200](/wiki/p/weakness/CWE-200), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-353](/wiki/p/weakness/CWE-353)

**ATT&CK techniques:** [T1562.003](/wiki/p/technique/T1562.003), [T1574.006](/wiki/p/technique/T1574.006), [T1574.007](/wiki/p/technique/T1574.007)

## Prerequisites

- An environment variable is accessible to the user.
- An environment variable used by the application can be tainted with user supplied data.
- Input data used in an environment variable is not validated properly.
- The variables encapsulation is not done properly. For instance setting a variable as public in a class makes it visible and an adversary may attempt to manipulate that variable.

## Skills required

- Low: In a web based scenario, the client controls the data that it submitted to the server. So anybody can try to send malicious data and try to bypass the authentication mechanism.
- High: Some more advanced attacks may require knowledge about protocols and probing technique which help controlling a variable. The malicious user may try to understand the authentication mechanism in order to defeat it.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism
- Availability: Unreliable Execution
- Confidentiality: Read Data
- Accountability: Hide Activities

## Mitigations

- Protect environment variables against unauthorized read and write access.
- Protect the configuration files which contain environment variables against illegitimate read and write access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Apply the least privilege principles. If a process has no legitimate reason to read an environment variable do not give that privilege.

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1562.003`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
