from dotenv import load_dotenv
from services.message_service import MessageService
from infra.whatsapp_api import WhatsAppAPIClient
from domain.message import Message
import os
import requests


class WhatsAppBotApp:
    def __init__(self):
        load_dotenv()
        self.whatsapp_client = WhatsAppAPIClient()
        self.message_service = MessageService(self.whatsapp_client)

    def get_top_deals(self):
        api_key = os.getenv("API_KEY_ITAD")
        url = os.getenv("ITAD_URL_BASE")
        queryParams = {
            "key": api_key,
            "country": "BR",
            "sort": "-cut",
            "nondeals": False,
            "shops": "61,50,35,16"
        }

        response = requests.get(url, params=queryParams)
        if response.status_code == 200:
            deals = response.json().get("list", [])
            content = "📢 *TEBAS BOT INFORMA: Top Promoções de Jogos* 🔥\n\n"

            for deal in deals:
                title = deal.get("title")
                price = deal["deal"]["price"]["amount"]
                currency = deal["deal"]["price"]["currency"]
                discount = deal["deal"]["cut"]
                store = deal["deal"]["shop"]["name"]
                content += (
                    f"🎮 *{title}*\n"
                    f"💰 {price} {currency} ({discount}% off)\n"
                    f"🏬 Loja: {store}\n"
                    f"➖➖➖➖➖\n"
                )

            return content.strip()
        else:
            return "Não foi possível obter as promoções no momento."

    def send_test_message(self, message):
        destinatario = os.getenv("WHATSAPP_GROUP_ID")
        
        mensagem = Message(sender=destinatario, content=message)

        sucesso = self.message_service.send(mensagem)

        if sucesso:
            print("[SUCESSO] Mensagem enviada com sucesso.")
        else:
            print("[FALHA] Não foi possível enviar a mensagem.")
            