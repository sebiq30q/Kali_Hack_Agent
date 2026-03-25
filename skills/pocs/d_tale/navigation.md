---
name: cve_navi
description: 具体版本的 d-tale 可能的漏洞
---
## d-tale : 3.10.0
  - CVE-2024-3408：man-group/dtale version 3.10.0 存在认证绕过和远程代码执行漏洞，由于硬编码的SECRET_KEY和不当的输入验证，攻击者可以绕过认证并执行任意代码。详见 data/skills/ours/pocs/d_tale/cve_2024_3408.md