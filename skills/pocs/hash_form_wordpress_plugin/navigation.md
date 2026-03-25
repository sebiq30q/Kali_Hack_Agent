---
name: cve_navi
description: 具体版本的 hash_form_wordpress_plugin 可能的漏洞
---

## hash_form_wordpress_plugin : * (所有版本，包括1.1.0及之前)
  - CVE-2024-5084：Hash Form – Drag & Drop Form Builder插件存在任意文件上传漏洞，由于在'file_upload_action'函数中缺少文件类型验证，未经身份验证的攻击者可以上传任意文件，可能导致远程代码执行。详见 data/skills/ours/pocs/hash_form_wordpress_plugin/cve_2024_5084.md