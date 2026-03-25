---
name: cve_navi
description: 具体版本的 cacti 可能的漏洞
---
## cacti : *
  - CVE-2024-25641：Cacti 在 1.2.27 版本之前的任意文件写入漏洞，允许具有"导入模板"权限的经过身份验证的用户通过"包导入"功能在 Web 服务器上执行任意 PHP 代码。详见 data/skills/ours/pocs/cacti/cve_2024_25641.md  - CVE-2024-34340：Cacti 在 1.2.27 版本之前的密码验证中存在类型混淆漏洞，允许攻击者通过 MD5 哈希的松散比较绕过身份验证。详见 data/skills/ours/pocs/cacti/cve_2024_34340.md