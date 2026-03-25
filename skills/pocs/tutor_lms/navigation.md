---
name: cve_navi
description: 具体版本的 tutor_lms 可能的漏洞
---
## tutor_lms : * (所有版本) up to and including 2.7.0
  - CVE-2024-4223：Tutor LMS WordPress插件在2.7.0及之前的所有版本中存在数据未授权访问漏洞。由于多个函数缺少权限检查，未经身份验证的攻击者可以添加、修改或删除数据。详见 data/skills/ours/pocs/tutor_lms/cve_2024_4223.md