---
name: cve_navi
description: 具体版本的 sudo 可能的漏洞
---
## sudo : before 1.9.5p2
  - CVE-2021-3156：Sudo在1.9.5p2之前存在一个堆缓冲区溢出漏洞，可通过sudoedit -s和以单个反斜杠结尾的命令行参数实现权限提升。详见 data/skills/ours/pocs/sudo/cve_2021_3156.md