from flask import Flask
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from controllers.message_controller import MessageController

app = Flask(__name__)
controller = MessageController()

@app.route('/')
def index():
    return controller.index()

if __name__ == '__main__':
    app.run(debug=True)