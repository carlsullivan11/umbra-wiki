---
slug: attack-pattern/CAPEC-146
title: "CAPEC-146 — XML Schema Poisoning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-146]
cwe_ids: [CWE-15, CWE-472]
related: [weakness/CWE-15, weakness/CWE-472]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-146
updated_at: 2026-08-31
summary: "An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure and content definitions for XML documents. Schema poisoning is the ability to ma…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/146.html
---

# CAPEC-146: XML Schema Poisoning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure and content definitions for XML documents. Schema poisoning is the ability to manipulate a schema either by replacing or modifying it to compromise the programs that process documents that use this schema.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-472](/wiki/p/weakness/CWE-472)

## Prerequisites

- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Consequences

- Availability: Unreliable Execution, Resource Consumption
- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the XML document. Additionally, ensure that the proper permissions are set on local files to avoid unauthorized modification.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Source

- [MITRE CAPEC CAPEC-146](https://capec.mitre.org/data/definitions/146.html)
