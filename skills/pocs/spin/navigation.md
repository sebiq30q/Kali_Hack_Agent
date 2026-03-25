---
name: cve_navi
description: 具体版本的 spin 可能的漏洞
---
## spin : < 2.4.3
  - CVE-2024-32980：Spin WebAssembly服务器应用工具在2.4.3之前版本存在SSRF漏洞，攻击者可通过Host HTTP头诱导应用向任意主机发送请求。详见 data/skills/ours/pocs/spin/cve_2024_32980.md