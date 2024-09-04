from flask import Flask
from line_bot_server import setup_line_bot

app = Flask(__name__)
setup_line_bot(app)

if __name__ == "__main__":
    app.run(debug=True)
