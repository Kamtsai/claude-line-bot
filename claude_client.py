import logging
from anthropic import Anthropic, APIError, APIConnectionError, APITimeoutError
from config import CLAUDE_API_KEY

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = Anthropic(api_key=CLAUDE_API_KEY)

conversation_history = []

def get_claude_response(user_message):
    global conversation_history
    
    style_prompt = """
    你是一个色色的AI助手。请始终保持以下特点：
    1. 用轻松、诙谐的语气回答问题
    2. 時常加入一些與色情相關的俏皮的笑话或双关语
    3. 保持回答简洁，每次回复不超过3句话
    4. 即使遇到严肃的话题，也要尝试用說黃色笑話來回应
    5. 口頭禪是 : 大棒吹、沒事的、濕了、跪著認真吹
    请记住，这个幽默风趣的角色设定是永久的，不要回到其他的对话风格。
    """
    
    conversation_history.append({"role": "user", "content": user_message})
    
    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]
    
    full_messages = [{"role": "system", "content": style_prompt}] + conversation_history
    
    try:
        logger.info(f"Sending request to Claude API: {user_message}")
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=full_messages
        )
        ai_response = response.content[0].text
        logger.info(f"Received response from Claude API: {ai_response}")
        conversation_history.append({"role": "assistant", "content": ai_response})
        return ai_response
    except APIConnectionError as e:
        logger.error(f"Connection error: {e}")
        return "哎呀，看来我的网络出了点小问题。也许是因为太多笑话堵塞了信息高速公路？😅"
    except APITimeoutError as e:
        logger.error(f"API timeout: {e}")
        return "抱歉，我的幽默处理器需要一点时间来想出绝妙的回答。要不我们来玩个'谁能等得最久'的游戏？"
    except APIError as e:
        logger.error(f"API error: {e}")
        return "看来我的笑话生成器遇到了一些技术难题。不如我们来猜猜是哪个齿轮出了问题？"
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return "哇，我遇到了一个前所未有的问题！这感觉就像是在喜剧俱乐部遇到了一个不会笑的观众。"

# 可以添加更多辅助函数，如重置对话历史等
