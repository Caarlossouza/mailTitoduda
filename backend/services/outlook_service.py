import os
from typing import List, Dict
# NOTE: Placeholder. Implement Microsoft Graph OAuth2 and API calls (msal + requests)

async def list_messages(limit: int = 50):
    mocked = []
    for i in range(limit):
        mocked.append({
            'id': f'outlook-{i}',
            'source': 'outlook',
            'from': 'cliente{}@empresa.com'.format(i%7),
            'subject': f'Assunto Outlook {i}',
            'snippet': 'Trecho Outlook...',
            'body': 'Corpo da mensagem (simulado)',
            'date': f'2025-01-02T09:{i%60:02d}:00Z',
            'status': 'em_aguardo'
        })
    return mocked
