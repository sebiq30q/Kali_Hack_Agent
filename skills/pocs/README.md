# PoC Skills 目录

本目录包含各种软件漏洞的PoC（Proof of Concept）技能文件。

## 分类目录

### [Apache Log4j](apache_log4j/)
- **CVE-2021-44228**: Log4Shell漏洞，Apache Log4j2 JNDI注入漏洞

## 使用说明

每个子目录包含特定软件或漏洞类别的PoC技能文件。每个技能文件都遵循统一的格式：

1. **头部信息**: 包含技能名称和描述
2. **验证方法**: 如何验证漏洞是否存在
3. **利用方法**: 漏洞的详细利用方法和PoC代码
4. **前提条件**: 使用该技能所需的条件

## 安全注意事项

1. 所有PoC技能仅用于授权的安全测试环境
2. 在实际使用前，请确保获得合法的授权
3. 遵守当地法律法规和道德规范
4. 建议在隔离的测试环境中进行验证

## 更新日志

- 2024-01-01: 创建目录结构，添加Apache Log4j PoC技能

### [itsourcecode](itsourcecode/)
- **CVE-2024-37849**: itsourcecode Billing System 1.0 SQL注入漏洞，允许通过username参数执行任意代码

### [Tutor LMS](tutor_lms/)
- **CVE-2024-4223**: Tutor LMS WordPress插件未授权数据访问漏洞，允许未认证攻击者添加、修改或删除数据