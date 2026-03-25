---
name: cve_navi
description: 具体版本的 samba 可能的漏洞
---
## samba : 3.5.0 to before 4.6.4, 4.5.10 and 4.4.14
  - CVE-2017-7494：Samba since version 3.5.0 and before 4.6.4, 4.5.10 and 4.4.14 is vulnerable to remote code execution vulnerability, allowing a malicious client to upload a shared library to a writable share, and then cause the server to load and execute it. 详见 data/skills/ours/pocs/samba/cve_2017_7494.md