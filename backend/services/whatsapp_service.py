import os
from typing import List, Dict
# NOTE: WhatsApp integration sample. Disabled by default. To enable:
# 1) Set WHATSAPP_TOKEN and WHATSAPP_PHONE_NUMBER_ID in .env
# 2) Implement the actual HTTP calls to WhatsApp Cloud API.
#
# Example commented pseudocode:
#
# import requests
# WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')
# PHONE_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
#
# async def list_messages(limit: int = 50):
#     if not WHATSAPP_TOKEN or not PHONE_ID:
#         return []  # Not configured
#     url = f'https://graph.facebook.com/v17.0/{PHONE_ID}/messages'
#     headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}'}
#     resp = requests.get(url, headers=headers, params={'limit': limit})
#     return resp.json()

async def list_messages(limit: int = 50):
    # Return mocked whatsapp messages for development
    mocked = []
    for i in range(limit):
        mocked.append({
            'id': f'wa-{i}',
            'source': 'whatsapp',
            'from': f'+55 9 0000-000{i%10}',
            'subject': None,
            'snippet': 'Mensagem WhatsApp...',
            'body': 'Olá, preciso de suporte sobre meu pedido...',
            'date': f'2025-01-03T15:{i%60:02d}:00Z',
            'status': 'em_aguardo'
        })
    return mocked
