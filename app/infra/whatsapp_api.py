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
            "options": {
                "mentions": {
                    "everyOne": True,
                    "mentioned": [
                        "559888984133@s.whatsapp.net",
                        "559885454725@s.whatsapp.net",
                "559885916236@s.whatsapp.net",
                "559887881104@s.whatsapp.net",
                "559887406722@s.whatsapp.net",
                "559888966906@s.whatsapp.net",
                "559884270935@s.whatsapp.net",
                "559891222906@s.whatsapp.net",
                "559892437127@s.whatsapp.net",
                "559891440884@s.whatsapp.net",
                "559892256474@s.whatsapp.net",
                "559885001019@s.whatsapp.net",
                "559891232312@s.whatsapp.net",
                "559887314208@s.whatsapp.net",
                "559889158825@s.whatsapp.net",
                "559891327090@s.whatsapp.net",
                "559884501718@s.whatsapp.net",
                "559883164470@s.whatsapp.net",
                "559885984315@s.whatsapp.net",
                "559882864173@s.whatsapp.net",
                "558199245493@s.whatsapp.net",
                "559881832694@s.whatsapp.net",
                "559882285508@s.whatsapp.net",
                "559881393798@s.whatsapp.net",
                "559884786701@s.whatsapp.net",
                "559888320711@s.whatsapp.net",
                "559891539580@s.whatsapp.net",
                "559884265251@s.whatsapp.net",
                "559887778153@s.whatsapp.net",
                "559884376986@s.whatsapp.net",
                "559885057639@s.whatsapp.net",
                "559884808955@s.whatsapp.net",
                "559881157076@s.whatsapp.net",
                "559885196326@s.whatsapp.net",
                "554792688010@s.whatsapp.net"
                        ]
                    }
                },
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
