---
slug: attack-pattern/CAPEC-690
title: "CAPEC-690 — Metadata Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-690]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-690
updated_at: 2026-08-31
summary: "An adversary alters the metadata of a resource (e.g., file, directory, repository, etc.) to present a malicious resource as legitimate/credible."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/690.html
---

# CAPEC-690: Metadata Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary alters the metadata of a resource (e.g., file, directory, repository, etc.) to present a malicious resource as legitimate/credible.

## Prerequisites

- Identification of a resource whose metadata is to be spoofed

## Skills required

- Medium: Ability to spoof a variety of metadata to convince victims the source is trusted

## Consequences

- Integrity: Modify Data
- Accountability: Hide Activities
- Access Control, Authorization: Execute Unauthorized Commands

## Mitigations

- Validate metadata of resources such as authors, timestamps, and statistics.
- Confirm the pedigree of open source packages and ensure the code being downloaded does not originate from another source.
- Even if the metadata is properly checked and a user believes it to be legitimate, there may still be a chance that they've been duped. Therefore, leverage automated testing techniques to determine where malicious areas of the code may exist.

## Source

- [MITRE CAPEC CAPEC-690](https://capec.mitre.org/data/definitions/690.html)
