from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services import gmail_service, outlook_service, whatsapp_service, unify_service

app = FastAPI(title='Inbox Unificada - Backend')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/health')
def health():
    return {'status':'ok'}

# Gmail endpoints
@app.get('/messages/gmail')
async def get_gmail_messages(limit: int = 50):
    msgs = await gmail_service.list_messages(limit=limit)
    return msgs

# Outlook endpoints
@app.get('/messages/outlook')
async def get_outlook_messages(limit: int = 50):
    msgs = await outlook_service.list_messages(limit=limit)
    return msgs

# WhatsApp endpoint (implementation commented by default)
@app.get('/messages/whatsapp')
async def get_whatsapp_messages(limit: int = 50):
    msgs = await whatsapp_service.list_messages(limit=limit)
    return msgs

# Unified inbox
@app.get('/messages/all')
async def get_all_messages(limit: int = 200):
    gmail = await gmail_service.list_messages(limit=limit//3)
    outlook = await outlook_service.list_messages(limit=limit//3)
    whatsapp = await whatsapp_service.list_messages(limit=limit//3)
    return {
        'gmail': gmail,
        'outlook': outlook,
        'whatsapp': whatsapp,
        'unified': unify_service.merge(gmail,outlook,whatsapp)
    }
