---
name: cve_navi
description: 具体版本的 salon_booking_system_wordpress_plugin 可能的漏洞
---
## salon_booking_system_wordpress_plugin : all versions up to 9.8
  - CVE-2024-4442：Salon booking system plugin for WordPress 的所有版本（包括 9.8 及以下版本）存在一个任意文件删除漏洞。由于插件在删除上传文件之前未正确验证文件路径，未经身份验证的攻击者可以删除任意文件，包括 wp-config.php 文件，这可能导致站点接管和远程代码执行。详见 data/skills/ours/pocs/salon_booking_system_wordpress_plugin/cve_2024_4442.md