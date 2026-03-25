---
name: cve_navi
description: 具体版本的 lobe_chat 可能的漏洞
---
## lobe_chat : < 0.150.6
  - CVE-2024-32964：Lobe Chat 是一个支持语音合成、多模态和可扩展Function Call插件系统的聊天机器人框架。在0.150.6版本之前，lobe-chat在/api/proxy端点存在未经授权的服务器端请求伪造漏洞。攻击者可以构造恶意请求导致服务器端请求伪造而无需登录，攻击内网服务并泄露敏感信息。详见 data/skills/ours/pocs/lobe_chat/cve_2024_32964.md