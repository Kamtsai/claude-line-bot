import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import anthropic

app = Flask(__name__)

# 設置LINE Bot API憑證
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# 設置Claude API憑證
claude = anthropic.Client(api_key="YOUR_CLAUDE_API_KEY")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    
    # 調用Claude API
    response = claude.completions.create(
        model="claude-3-opus-20240229",
        prompt=f"Human: {user_message}\n\nAssistant:",
        max_tokens_to_sample=300
    )
    
    # 獲取Claude的回复
    claude_response = response.completion
    
    # 發送回复給用戶
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=claude_response)
    )

if __name__ == "__main__":
    app.run()
