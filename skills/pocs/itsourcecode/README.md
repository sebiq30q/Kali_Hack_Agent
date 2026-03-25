# itsourcecode 软件漏洞 PoC Skills

本目录包含itsourcecode系列软件的漏洞PoC技能文件。

## 可用PoC技能

### [CVE-2024-37849](cve_2024_37849.md)
- **漏洞类型**: SQL注入
- **影响软件**: itsourcecode Billing System 1.0
- **CVSS评分**: 9.8 (CRITICAL)
- **漏洞描述**: SQL注入漏洞允许本地攻击者通过username参数在process.php中执行任意代码

## 软件信息

itsourcecode是一个提供各种开源软件和系统的平台，包括：
- Billing System（计费系统）
- 其他各种管理系统

## 安全注意事项

1. 这些PoC技能仅用于授权的安全测试环境
2. 测试前请确保获得合法的授权
3. 遵守当地法律法规和道德规范
4. 建议在隔离的测试环境中进行验证

## 更新日志

- 2024-01-01: 创建目录，添加CVE-2024-37849 PoC技能