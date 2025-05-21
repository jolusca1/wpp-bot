from abc import ABC, abstractmethod
from domain.message import Message

class WhatsAppClientInterface(ABC):
    @abstractmethod
    def send_message(self, sender: str, content: str) -> bool:
        """Envia uma mensagem para o número ou grupo especificado."""
        pass

    @abstractmethod
    def receive_message(self, payload: dict) -> Message:
        """Converte um payload recebido da API de WhatsApp em uma entidade Message."""
        pass
