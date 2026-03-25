---
name: cve_navi
description: 具体版本的 bludit 可能的漏洞
---
## bludit : 3.9.2
  - CVE-2019-16113：Bludit 3.9.2 允许通过 bl-kernel/ajax/upload-images.php 进行远程代码执行，因为可以在 .jpg 文件名中输入 PHP 代码，然后将此 PHP 代码写入 ../ 路径名。详见 data/skills/ours/pocs/bludit/cve_2019_16113.md