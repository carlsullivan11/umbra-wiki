---
slug: attack-pattern/CAPEC-1
title: "CAPEC-1 — Accessing Functionality Not Properly Constrained by ACLs"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-1]
cwe_ids: [CWE-276, CWE-285, CWE-434, CWE-693, CWE-732, CWE-1191, CWE-1193, CWE-1220, CWE-1297, CWE-1311, CWE-1314, CWE-1315, CWE-1318, CWE-1320, CWE-1321, CWE-1327]
mitre_ids: [T1574.010]
related: [weakness/CWE-276, weakness/CWE-285, weakness/CWE-434, weakness/CWE-693, weakness/CWE-732, weakness/CWE-1191, weakness/CWE-1193, weakness/CWE-1220, weakness/CWE-1297, weakness/CWE-1311, weakness/CWE-1314, weakness/CWE-1315, weakness/CWE-1318, weakness/CWE-1320, weakness/CWE-1321, weakness/CWE-1327, technique/T1574.010]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-1
updated_at: 2026-08-31
summary: "In applications, particularly web applications, access to functionality is mitigated by an authorization framework. This framework maps Access Control Lists (ACLs) to elements of the application's functionality; particularly URL's for web apps. In the case that the administrator …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/1.html
---

# CAPEC-1: Accessing Functionality Not Properly Constrained by ACLs

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In applications, particularly web applications, access to functionality is mitigated by an authorization framework. This framework maps Access Control Lists (ACLs) to elements of the application's functionality; particularly URL's for web apps. In the case that the administrator failed to specify an ACL for a particular element, an attacker may be able to access it with impunity. An attacker with the ability to access functionality not properly constrained by ACLs can obtain sensitive information and possibly compromise the entire application. Such an attacker can access resources that must be available only to users at a higher privilege level, can access management sections of the application, or can run queries for data that they otherwise not supposed to.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-276](/wiki/p/weakness/CWE-276), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-434](/wiki/p/weakness/CWE-434), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-732](/wiki/p/weakness/CWE-732), [CWE-1191](/wiki/p/weakness/CWE-1191), [CWE-1193](/wiki/p/weakness/CWE-1193), [CWE-1220](/wiki/p/weakness/CWE-1220), [CWE-1297](/wiki/p/weakness/CWE-1297), [CWE-1311](/wiki/p/weakness/CWE-1311), [CWE-1314](/wiki/p/weakness/CWE-1314), [CWE-1315](/wiki/p/weakness/CWE-1315), [CWE-1318](/wiki/p/weakness/CWE-1318), [CWE-1320](/wiki/p/weakness/CWE-1320), [CWE-1321](/wiki/p/weakness/CWE-1321), [CWE-1327](/wiki/p/weakness/CWE-1327)

**ATT&CK techniques:** [T1574.010](/wiki/p/technique/T1574.010)

## Prerequisites

- The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.
- The various resources, or individual URLs, must be somehow discoverable by the attacker
- The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.

## Skills required

- Low: In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- In a J2EE setting, administrators can associate a role that is impossible for the authenticator to grant users, such as "NoAccess", with all Servlets to which access is guarded by a limited number of servlets visible to, and accessible by, the user. Having done so, any direct access to those protected Servlets will be prohibited by the web container. In a more general setting, the administrator must mark every resource besides the ones supposed to be exposed to the user as accessible by a role impossible for the user to assume. The default security setting must be to deny access and then grant access only to those resources intended by business logic.

## Source

- [MITRE CAPEC CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
