from flask import Flask
app = Flask(__name__)

@app.route('/')
def minimal():
    return "I'm a minimal Flask app"