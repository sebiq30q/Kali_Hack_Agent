---
name: cve_navi
description: 具体版本的 chuanhuchatgpt 可能的漏洞
---
## chuanhuchatgpt : *
  - CVE-2024-3234：chuanhuchatgpt 存在路径遍历漏洞，由于使用了易受攻击的 gradio 组件（CVE-2023-51449），允许未经授权的用户绕过限制访问敏感文件如 config.json。详见 data/skills/ours/pocs/chuanhuchatgpt/cve_2024_3234.md