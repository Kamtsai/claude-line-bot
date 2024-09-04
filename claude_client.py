from anthropic import Anthropic
from config import CLAUDE_API_KEY

claude = Anthropic(api_key=CLAUDE_API_KEY)

def get_claude_response(user_message):
    try:
        response = claude.completions.create(
            model="claude-3-opus-20240229",
            max_tokens_to_sample=1000,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return "抱歉，我现在无法回答。请稍后再试。"
