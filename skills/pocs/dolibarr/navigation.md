---
name: cve_navi
description: 具体版本的 dolibarr 可能的漏洞
---
## dolibarr : 9.0.1 (affected)
  - CVE-2024-5315：Dolibarr ERP - CRM 版本 9.0.1 存在SQL注入漏洞。远程攻击者可通过向系统发送特制的SQL查询，通过 /dolibarr/commande/list.php 中的 viewstatut 参数检索数据库中存储的所有信息。详见 data/skills/ours/pocs/dolibarr/cve_2024_5315.md
  - CVE-2024-5314：Dolibarr ERP - CRM 版本 9.0.1 存在SQL注入漏洞。远程攻击者可通过向系统发送特制的SQL查询，通过 /dolibarr/admin/dict.php 中的 sortorder 和 sortfield 参数检索数据库中存储的所有信息。详见 data/skills/ours/pocs/dolibarr/cve_2024_5314.md