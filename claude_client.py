import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_claude_response(user_message, max_retries=3):
    logging.info(f"Received message: {user_message}")
    mock_response = f"这是一个模拟的回复：我收到了您的消息 '{user_message}'"
    logging.info(f"Sending mock response: {mock_response}")
    return mock_response

def test_claude_api():
    test_message = "Hello, Claude! Can you hear me?"
    response = get_claude_response(test_message)
    print(f"Test message: {test_message}")
    print(f"Claude response: {response}")

if __name__ == "__main__":
    test_claude_api()
