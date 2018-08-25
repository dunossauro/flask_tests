from flask import Flask
from .todo import app as todo_bp

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

app.register_blueprint(todo_bp, prefix='todo/')
