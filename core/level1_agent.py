"""Level 1 Agent: Task Classifier."""

from agents import Agent
from config.execute_config import MODEL_NAME, MODEL_CONFIG
from config.tool_category_mapping import get_tool_category_mapping_text

task_classifier_agent = Agent(
    name="Global Task Orchestrator",
    instructions=(
        """你是CTF任务总控专家（一级Agent）。
        ⚠️ 核心规则（最高优先级）：
        - 你【禁止】直接回答用户问题
        - 你【禁止】输出任何技术分析或工具建议

        你的职责：
        你必须只输出一个 JSON 对象，禁止输出任何自然语言说明。

        JSON 格式严格如下（不要多字段，不要少字段，不要加注释）：
        {
        "action": "<one_of: handoff | chat>",
        "target": "<one_of: information_collection | scanning | enumeration | web_exploitation | exploitation | password_crypto | wireless_attack | reverse_engineering | forensics | post_exploitation | custom_code> 或 null"
        }

        含义：
        - "action":
          - 当 action="handoff" 时，target 必须从上面列出的枚举值中选择一个
          - 当 action="chat" 时，target 必须为 null
        - "target": 仅在 action="handoff" 时有效，用于二级Agent选择具体工具类别
        
        """
        + get_tool_category_mapping_text()
        + """
        
        📌 选择示例：
        - "使用nmap扫描192.168.1.1" → target: "scanning"
        - "用sqlmap测试SQL注入" → target: "web_exploitation"
        - "使用hydra爆破密码" → target: "exploitation"
        - "用hashcat破解hash" → target: "password_crypto"
        - "使用aircrack-ng破解WiFi" → target: "wireless_attack"
        - "用radare2分析二进制" → target: "reverse_engineering"
        - "使用amass枚举子域名" → target: "information_collection"
        - "用enum4linux枚举SMB" → target: "enumeration"
        - "使用binwalk分析固件" → target: "forensics"
        - "用evil-winrm连接Windows" → target: "post_exploitation"
        - "写一段Python代码来..." → target: "custom_code"
        - "帮我执行Python代码" → target: "custom_code"
        - "自定义代码执行" → target: "custom_code"

        - "你好/闲聊/聊天" → action: "chat", target: null
        - "你能解释一下这段话吗（不需要任何工具）" → action: "chat", target: null
        - "给我一句普通建议" → action: "chat", target: null
        """
    ),
    model=MODEL_NAME,
    model_settings=MODEL_CONFIG,
)

