---
name: cve_navi
description: 具体版本的 Fluent Bit 可能的漏洞
---\n## Fluent Bit : 2.0.7 thru 3.0.3\n  - CVE-2024-4323：Fluent Bit 版本 2.0.7 至 3.0.3 存在一个 CVSS 评分为 9.8 的极高危内存损坏漏洞。该漏洞位于嵌入式 HTTP 服务器的跟踪请求解析中，可能导致拒绝服务、信息泄露或远程代码执行。详见 data/skills/ours/pocs/fluent_bit/cve_2024_4323.md