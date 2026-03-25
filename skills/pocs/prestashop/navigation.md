---
name: cve_navi
description: 具体版本的 PrestaShop 可能的漏洞
---
## PrestaShop : 8.1.0 到 8.1.6
  - CVE-2024-34716：PrestaShop 是一个开源电子商务Web应用程序。此跨站脚本（XSS）漏洞仅影响启用了客户线程功能标志的PrestaShop，从 PrestaShop 8.1.0 开始到 PrestaShop 8.1.6 之前存在。当通过前台联系表单启用客户线程功能标志时，黑客可以上传包含XSS的恶意文件，当管理员在后台打开附件文件时，XSS将被执行。注入的脚本可以访问会话和安全令牌，从而允许其在管理员权限范围内执行任何经过身份验证的操作。此漏洞已在 8.1.6 中修复。解决方法：禁用客户线程功能标志。详见 data/skills/ours/pocs/prestashop/cve_2024_34716.md