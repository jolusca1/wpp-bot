from datetime import datetime

class Message:
    def __init__(self, sender: str, content: str):
        self.sender = sender
        self.content = content

    def is_command(self) -> bool:
        return self.content.strip().startswith("!")

    def get_command_name(self) -> str:
        if self.is_command():
            return self.content.strip().split()[0][1:].lower()
        return ""

    def get_command_args(self) -> list[str]:
        if self.is_command():
            return self.content.strip().split()[1:]
        return []

    def __repr__(self):
        return f"<Message from={self.sender} content='{self.content}'>"