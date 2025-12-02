from django.core.cache import cache
import requests
from decouple import config

def enviar_notificacao(numero: str):
    url = 'https://graph.facebook.com/v22.0/964251236763798/messages'
    token = config('TOKEN_WHATSAPP')

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "template",
        "template": {
            "name": "hello_world",
        "language": {
            "code": "en_US"
            }
        } 
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        response.raise_for_status()
        print(response.text)
    except Exception as e:
        print(f'Erro: {e}')

