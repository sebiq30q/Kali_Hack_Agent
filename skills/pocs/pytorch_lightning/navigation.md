---
name: cve_navi
description: 具体版本的 pytorch_lightning 可能的漏洞
---
## pytorch_lightning : 2.2.1 (affected)
  - CVE-2024-5452：lightning-ai/pytorch-lightning 库版本 2.2.1 存在远程代码执行漏洞，由于对反序列化用户输入处理不当以及 deepdiff 库对 dunder 属性的管理不当。攻击者可构造通过反序列化白名单的序列化 delta 对象，利用 dunder 属性访问其他模块、类和实例，导致任意属性写入和完全远程代码执行。详见 data/skills/ours/pocs/pytorch_lightning/cve_2024_5452.md