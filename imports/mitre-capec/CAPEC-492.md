---
slug: attack-pattern/CAPEC-492
title: "CAPEC-492 — Regular Expression Exponential Blowup"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-492]
cwe_ids: [CWE-400, CWE-1333]
related: [weakness/CWE-400, weakness/CWE-1333]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-492
updated_at: 2026-08-31
summary: "An adversary may execute an attack on a program that uses a poor Regular Expression(Regex) implementation by choosing input that results in an extreme situation for the Regex. A typical extreme situation operates at exponential time compared to the input size. This is due to most…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/492.html
---

# CAPEC-492: Regular Expression Exponential Blowup

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute an attack on a program that uses a poor Regular Expression(Regex) implementation by choosing input that results in an extreme situation for the Regex. A typical extreme situation operates at exponential time compared to the input size. This is due to most implementations using a Nondeterministic Finite Automaton(NFA) state machine to be built by the Regex algorithm since NFA allows backtracking and thus more complex regular expressions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-400](/wiki/p/weakness/CWE-400), [CWE-1333](/wiki/p/weakness/CWE-1333)

## Prerequisites

- This type of an attack requires the ability to identify hosts running a poorly implemented Regex, and the ability to send crafted input to exploit the regular expression.

## Mitigations

- Test custom written Regex with fuzzing to determine if the Regex is a poor one. Add timeouts to processes that handle the Regex logic. If an evil Regex is found rewrite it as a good Regex.

## Source

- [MITRE CAPEC CAPEC-492](https://capec.mitre.org/data/definitions/492.html)
