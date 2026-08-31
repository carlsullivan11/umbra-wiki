---
slug: attack-pattern/CAPEC-503
title: "CAPEC-503 — WebView Exposure"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-503]
cwe_ids: [CWE-284]
related: [weakness/CWE-284]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-503
updated_at: 2026-08-31
summary: "An adversary, through a malicious web page, accesses application specific functionality by leveraging interfaces registered through WebView's addJavascriptInterface API. Once an interface is registered to WebView through addJavascriptInterface, it becomes global and all pages loa…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/503.html
---

# CAPEC-503: WebView Exposure

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a malicious web page, accesses application specific functionality by leveraging interfaces registered through WebView's addJavascriptInterface API. Once an interface is registered to WebView through addJavascriptInterface, it becomes global and all pages loaded in the WebView can call this interface.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

## Prerequisites

- This type of an attack requires the adversary to convince the user to load the malicious web page inside the target application. Once loaded, the malicious web page will have the same permissions as the target application and will have access to all registered interfaces. Both the permission and the interface must be in place for the functionality to be exposed.

## Mitigations

- To mitigate this type of an attack, an application should limit permissions to only those required and should verify the origin of all web content it loads.

## Source

- [MITRE CAPEC CAPEC-503](https://capec.mitre.org/data/definitions/503.html)
