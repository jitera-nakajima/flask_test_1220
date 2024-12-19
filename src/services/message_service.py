from models.message import Message

class MessageService:
    def get_greeting(self) -> Message:
        return Message("Hello, World!")