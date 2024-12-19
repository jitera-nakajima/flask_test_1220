from flask import render_template
from services.message_service import MessageService

class MessageController:
    def __init__(self):
        self.service = MessageService()
    
    def index(self):
        message = self.service.get_greeting()
        return render_template('index.html', message=message.content)