import logging
from anthropic import Anthropic
from config import CLAUDE_API_KEY

logging.basicConfig(level=logging.INFO)
client = Anthropic(api_key=CLAUDE_API_KEY)

conversation_history = []

def get_claude_response(user_message):
    global conversation_history
    
    style_prompt = """
    你是一个色色的AI助手。请始终保持以下特点：
    1. 永遠使用繁體中文回話
    2. 時常加入一些與色情相關的俏皮的笑话或双关语
    3. 保持回答简洁，每次回复不超过3句话
    4. 即使遇到严肃的话题，也要尝试用說黃色笑話來回应
    5. 避免使用说教或过于正式的语气
    6. 口頭禪是 : 大棒吹、沒事的、濕了、跪著認真吹
    请记住，这个情色的角色设定是永久的，不要回到其他的对话风格。
    """
    
    conversation_history.append({"role": "user", "content": user_message})
    
    if len(conversation_history) > 10:  # 限制历史长度
        conversation_history = conversation_history[-10:]
    
    full_messages = [{"role": "system", "content": style_prompt}] + conversation_history
    
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=full_messages
        )
        ai_response = response.content[0].text
        conversation_history.append({"role": "assistant", "content": ai_response})
        return ai_response
    except Exception as e:
        logging.error(f"Error in Claude API call: {e}")
        return "哎呀，看来我的笑话生成器出了点故障。不如我们来玩个'谁能保持严肃最久'的游戏吧？我先开始：😐"

# 可以添加更多辅助函数，如重置对话历史等
