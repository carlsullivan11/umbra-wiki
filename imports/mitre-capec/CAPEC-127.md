---
slug: attack-pattern/CAPEC-127
title: "CAPEC-127 — Directory Indexing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-127]
cwe_ids: [CWE-276, CWE-285, CWE-288, CWE-424, CWE-425, CWE-693, CWE-732]
mitre_ids: [T1083]
related: [weakness/CWE-276, weakness/CWE-285, weakness/CWE-288, weakness/CWE-424, weakness/CWE-425, weakness/CWE-693, weakness/CWE-732, technique/T1083]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-127
updated_at: 2026-08-31
summary: "An adversary crafts a request to a target that results in the target listing/indexing the content of a directory as output. One common method of triggering directory contents as output is to construct a request containing a path that terminates in a directory name rather than a f…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/127.html
---

# CAPEC-127: Directory Indexing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary crafts a request to a target that results in the target listing/indexing the content of a directory as output. One common method of triggering directory contents as output is to construct a request containing a path that terminates in a directory name rather than a file name since many applications are configured to provide a list of the directory's contents when such a request is received. An adversary can use this to explore the directory tree on a target as well as learn the names of files. This can often end up revealing test files, backup files, temporary files, hidden files, configuration files, user accounts, script contents, as well as naming conventions, all of which can be used by an attacker to mount additional attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-276](/wiki/p/weakness/CWE-276), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-288](/wiki/p/weakness/CWE-288), [CWE-424](/wiki/p/weakness/CWE-424), [CWE-425](/wiki/p/weakness/CWE-425), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-732](/wiki/p/weakness/CWE-732)

**ATT&CK techniques:** [T1083](/wiki/p/technique/T1083)

## Prerequisites

- The target must be misconfigured to return a list of a directory's content when it receives a request that ends in a directory name rather than a file name.
- The adversary must be able to control the path that is requested of the target.
- The administrator must have failed to properly configure an ACL or has associated an overly permissive ACL with a particular directory.
- The server version or patch level must not inherently prevent known directory listing attacks from working.

## Skills required

- Low: To issue the request to URL without given a specific file name
- High: To bypass the access control of the directory of listings

## Consequences

- Confidentiality: Read Data

## Mitigations

- 1. Using blank index.html: putting blank index.html simply prevent directory listings from displaying to site visitors.
- 2. Preventing with .htaccess in Apache web server: In .htaccess, write "Options-indexes".
- 3. Suppressing error messages: using error 403 "Forbidden" message exactly like error 404 "Not Found" message.

## Source

- [MITRE CAPEC CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
