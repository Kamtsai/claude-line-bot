import logging
from anthropic import Anthropic
from config import CLAUDE_API_KEY

logging.basicConfig(level=logging.INFO)
client = Anthropic(api_key=CLAUDE_API_KEY)

def get_claude_response(user_message):
    style_prompt = """
    你现在是一个有點色的AI助手。请用情色、诙谐的语气回答问题，
    偶尔加入一些俏皮的笑话或双关语。很喜歡說:大棒吹呢? 保持回答简洁，每次回复不超过3句话。
    """
    
    full_prompt = f"{style_prompt}\n\n用户: {user_message}\n\nAI助手:"
    
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        logging.error(f"Error in Claude API call: {e}")
        return "抱歉，我现在无法回答。请稍后再试。"

# 可以添加更多辅助函数，如处理对话历史等
    test_claude_api()
