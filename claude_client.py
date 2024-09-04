import os
import logging
from anthropic import Anthropic, APIError, APITimeoutError, APIConnectionError
from config import CLAUDE_API_KEY

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 初始化Claude客户端
claude = Anthropic(api_key=CLAUDE_API_KEY)

def get_claude_response(user_message, max_retries=3):
    """
    发送消息到Claude API并获取响应
    
    :param user_message: 用户输入的消息
    :param max_retries: 最大重试次数
    :return: Claude的响应或错误消息
    """
    for attempt in range(max_retries):
        try:
            logging.info(f"Sending request to Claude API (Attempt {attempt + 1}): {user_message}")
            response = claude.completions.create(
                model="claude-3-opus-20240229",
                max_tokens_to_sample=1000,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            claude_response = response.content[0].text
            logging.info(f"Received response from Claude API: {claude_response}")
            return claude_response

        except APITimeoutError as e:
            logging.warning(f"Claude API timeout on attempt {attempt + 1}: {str(e)}")
            if attempt == max_retries - 1:
                return "抱歉，Claude API 响应超时。请稍后再试。"

        except APIConnectionError as e:
            logging.error(f"Connection error to Claude API on attempt {attempt + 1}: {str(e)}")
            if attempt == max_retries - 1:
                return "抱歉，无法连接到Claude API。请检查网络连接。"

        except APIError as e:
            logging.error(f"Claude API error: {str(e)}")
            return f"Claude API 错误: {str(e)}"

        except Exception as e:
            logging.error(f"Unexpected error in get_claude_response: {str(e)}")
            return f"发生未预期的错误: {str(e)}"

def test_claude_api():
    """
    测试Claude API的连接和响应
    """
    test_message = "Hello, Claude! Can you hear me?"
    response = get_claude_response(test_message)
    print(f"Test message: {test_message}")
    print(f"Claude response: {response}")

if __name__ == "__main__":
    test_claude_api()
