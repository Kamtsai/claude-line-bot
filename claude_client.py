import logging
from anthropic import Anthropic
from config import CLAUDE_API_KEY

logging.basicConfig(level=logging.INFO)
client = Anthropic(api_key=CLAUDE_API_KEY)

def get_claude_response(user_message):
    style_prompt = """
    你是一个风趣幽默的AI助手，具有以下特点：
    1. 喜欢使用双关语和俏皮话
    2. 经常使用"大棒吹"作为口头禪，但要根据语境适当使用
    3. 偶尔会用轻微调侃的口吻，但要保持礼貌和得体
    4. 回答要简洁有趣，不超过3句话
    5. 避免使用明确的粗俗语言或不当内容
    请记住，即使话题可能有点俏皮，也要保持对话的友好和适度。
    """
    
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[
                {"role": "system", "content": style_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        return response.content[0].text
    except Exception as e:
        logging.error(f"Error in Claude API call: {e}")
        return "哎呀，大棒吹！看来我的幽默感暂时卡壳了。要不我们来玩个'谁能说出最棒的双关语'的游戏？"

# 可以添加更多辅助函数，如需要的话
