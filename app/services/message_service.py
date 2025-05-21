from domain.message import Message
from interfaces.whatsapp_client import WhatsAppClientInterface


class MessageService:
    def __init__(self, whatsapp_client: WhatsAppClientInterface):
        self.whatsapp_client = whatsapp_client

    def send(self, message: Message) -> bool:
        """
        Envia uma mensagem para o destinatário especificado.
        """
        success = self.whatsapp_client.send_text_message(text=message.content, number=message.sender)
        return success

    def process_webhook(self, payload: dict) -> Message:
        """
        Processa um payload recebido via webhook e retorna a mensagem tratada.
        """
        return self.whatsapp_client.receive_message(payload)
