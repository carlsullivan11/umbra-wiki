---
slug: attack-pattern/CAPEC-500
title: "CAPEC-500 — WebView Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-500]
cwe_ids: [CWE-749, CWE-940]
related: [weakness/CWE-749, weakness/CWE-940]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-500
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, injects code into the context of a web page displayed by a WebView component. Through the injected code, an adversary is able to manipulate the DOM tree and cookies of the page, expose sensitive information, and …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/500.html
---

# CAPEC-500: WebView Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, injects code into the context of a web page displayed by a WebView component. Through the injected code, an adversary is able to manipulate the DOM tree and cookies of the page, expose sensitive information, and can launch attacks against the web application from within the web page.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-749](/wiki/p/weakness/CWE-749), [CWE-940](/wiki/p/weakness/CWE-940)

## Prerequisites

- An adversary must be able install a purpose built malicious application onto the device and convince the user to execute it. The malicious application is designed to target a specific web application and is used to load the target web pages via the WebView component. For example, an adversary may develop an application that interacts with Facebook via WebView and adds a new feature that a user desires. The user would install this 3rd party app instead of the Facebook app.

## Mitigations

- The only known mitigation to this type of attack is to keep the malicious application off the system. There is nothing that can be done to the target application to protect itself from a malicious application that has been installed and executed.

## Source

- [MITRE CAPEC CAPEC-500](https://capec.mitre.org/data/definitions/500.html)
