---
slug: attack-pattern/CAPEC-261
title: "CAPEC-261 — Fuzzing for garnering other adjacent user/sensitive data"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-261]
cwe_ids: [CWE-20]
related: [weakness/CWE-20]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-261
updated_at: 2026-08-31
summary: "An adversary who is authorized to send queries to a target sends variants of expected queries in the hope that these modified queries might return information (directly or indirectly through error logs) beyond what the expected set of queries should provide."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/261.html
---

# CAPEC-261: Fuzzing for garnering other adjacent user/sensitive data

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary who is authorized to send queries to a target sends variants of expected queries in the hope that these modified queries might return information (directly or indirectly through error logs) beyond what the expected set of queries should provide.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20)

## Prerequisites

- The server must assume that the queries it receives follow specific templates and/or have fields or attributes that follow specific procedures. The server must process queries that it receives without adequately checking or sanitizing queries to ensure they follow these templates.

## Source

- [MITRE CAPEC CAPEC-261](https://capec.mitre.org/data/definitions/261.html)
