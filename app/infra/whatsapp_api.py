import os
import requests
import time

class WhatsAppAPIClient:
    def __init__(self):
        self.base_url = os.getenv("WHATSAPP_API_URL")
        self.instance = os.getenv("INSTANCE_WHATSAPP")
        self.api_key = os.getenv("WHATSAPP_TOKEN")
        self.group_jid = os.getenv("WHATSAPP_GROUP_ID")

    def send_text_message(self, number: str, text: str, options: dict = None) -> bool:
        """
        Envia uma mensagem de texto para o número informado.
        """

        payload = {
            "number": number,
            "mentionsEveryOne": False,
            "text": text
        }

        #if options:
         #   payload["options"] = options

        url = f"{self.base_url}/message/sendText/{self.instance}"

        headers = {
            "Content-Type": "application/json",
            "apikey": self.api_key
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"[WhatsAppAPIClient] Erro ao enviar mensagem: {e}")
            return False
