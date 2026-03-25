---
name: cve_navi
description: 具体版本的 openssl 可能的漏洞
---
## openssl : 1.0.1 before 1.0.1g
  - CVE-2014-0160：OpenSSL 1.0.1 在 1.0.1g 之前的版本存在 Heartbleed 漏洞，远程攻击者可通过精心构造的 Heartbeat Extension 数据包触发缓冲区过度读取，从而获取进程内存中的敏感信息（如私钥）。详见 data/skills/ours/pocs/openssl/cve_2014_0160.md