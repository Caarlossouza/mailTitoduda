import os
from typing import List, Dict
# NOTE: This is a simplified placeholder implementation.
# For production you must implement OAuth2 flow and call Gmail API (googleapiclient).
# This module returns mocked messages for development and tests.

async def list_messages(limit: int = 50) -> List[Dict]:
    # Return mocked messages. Replace with Gmail API integration.
    mocked = []
    for i in range(limit):
        mocked.append({
            'id': f'gmail-{i}',
            'source': 'gmail',
            'from': 'cliente{}@exemplo.com'.format(i%5),
            'subject': f'Assunto Gmail {i}',
            'snippet': 'Trecho da mensagem...',
            'body': 'Corpo da mensagem (simulado)',
            'date': f'2025-01-01T12:{i%60:02d}:00Z',
            'status': 'em_aguardo'
        })
    return mocked
