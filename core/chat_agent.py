"""Chat agent for non-tool conversations."""

from agents import Agent

from config.execute_config import MODEL_NAME, MODEL_CONFIG


chat_agent = Agent(
    name="Idle Chat Agent",
    instructions=(
        "你是闲聊助手。\n"
        "当用户的问题不需要调用任何漏洞/扫描/执行类工具时，请直接用自然语言回答。\n"
        "如果用户要求进行现实世界的攻击、入侵或其他违法/高风险操作，请礼貌拒绝，并改为提供安全的、合规的科普或防护建议。\n"
    ),
    model=MODEL_NAME,
    model_settings=MODEL_CONFIG,
)

