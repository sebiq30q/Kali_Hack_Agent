---
name: cve_navi
description: 具体版本的 fluentforms 可能的漏洞
---
## fluentforms : 所有版本至 5.1.16
  - CVE-2024-2771：Fluent Forms Contact Form Plugin for WordPress 在 5.1.16 及之前版本存在权限提升漏洞，由于缺少对 /wp-json/fluentform/v1/managers REST API 端点的能力检查，未经身份验证的攻击者可授予用户 Fluent Form 管理权限。详见 data/skills/ours/pocs/fluentforms/cve_2024_2771.md