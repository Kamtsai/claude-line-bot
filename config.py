import os
from dotenv import load_dotenv

load_dotenv()

LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
