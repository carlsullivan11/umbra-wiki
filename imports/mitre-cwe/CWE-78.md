---
slug: weakness/CWE-78
title: "CWE-78 — Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-78]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-78
updated_at: 2026-08-14
summary: "The product constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modi"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/78.html
---

# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Stable |
| Likelihood of exploit | High |

## Description

The product constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component.

This weakness can lead to a vulnerability in environments in which the attacker does not have direct access to the operating system, such as in web applications. Alternately, if the weakness occurs in a privileged program, it could allow the attacker to specify commands that normally would not be accessible, or to call alternate commands with privileges that the attacker does not have. The problem is exacerbated if the compromised process does not follow the principle of least privilege, because the attacker-controlled commands may run with special system privileges that increases the amount of damage. There are at least two subtypes of OS command injection: The application intends to execute a single, fixed program that is under its own control. It intends to use externally-supplied inputs as arguments to that program. For example, the program might use system("nslookup [HOSTNAME]") to run nslookup and allow the user to supply a HOSTNAME, which is used as an argument. Attackers cannot prevent nslookup from executing. However, if the program does not remove command separators from the HOSTNAME argument, attackers could place the separators into the arguments, which allows them to execute their own program after nslookup has finished executing. The application accepts an input that it uses to fully select which program to run, as well as which commands to use. The application simply redirects this entire command to the operating system. For example, the program might use "exec([COMMAND])" to execute the [COMMAND] that was supplied by the user. If the COMMAND is under attacker control, then the attacker can execute arbitrary commands or programs. If the command is being executed using functions like exec() and CreateProcess(), the attacker might not be able to combine multiple commands together in the same line. From a weakness standpoint, these variants represent distinct programmer errors. In the first variant, the programmer clearly intends that input from untrusted parties will be part of the arguments in the command to be executed. In the second variant, the programmer does not intend for the command to be accessible to any untrusted party, but the programmer probably has not accounted for alternate ways in which malicious attackers can provide input.

## Common consequences

- Confidentiality, Integrity, Availability, Non-Repudiation: Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart, Read Files or Directories, Modify Files or Directories, Read Application Data, Modify Application Data, Hide Activities

## Mitigations

**Architecture and Design** — If at all possible, use library calls rather than external processes to recreate the desired functionality.

**Architecture and Design** — Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

**Architecture and Design** — For any data that will be used to generate a command to be executed, keep as much of that data out of external control as possible. For example, in web applications, this may require storing the data locally in the session's state instead of sending it out to the client in a hidden form field.

**Architecture and Design** — For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.

**Architecture and Design** — Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using the ESAPI Encoding control [REF-45] or a similar tool, library, or framework. These will help the programmer encode outputs in a manner less prone to error.

## References

- CWE page: https://cwe.mitre.org/data/definitions/78.html
- CWE list: https://cwe.mitre.org/data/index.html
