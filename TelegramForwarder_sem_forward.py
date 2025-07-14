import asyncio
from telethon import TelegramClient, events

api_id = 25898839
api_hash = '699f51fea67c98f94c5b4f08cf8ea9ef'
session_name = 'clonador_session'

grupos_origem = {
    -1002008424849: "Fire TV - Oficial",
    -1002150781193: "Rush Play Oficial"
}

grupo_destino = -1002682285509
usuario = "@WilliamMaster94"

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=list(grupos_origem.keys())))
async def handler(event):
    try:
        nome_origem = grupos_origem.get(event.chat_id, "Servidor Desconhecido")
        legenda = (event.message.text or "") + f"\n\n📣 {usuario} — Servidor: {nome_origem}"

        if event.message.media:
            await client.send_file(grupo_destino, file=event.message.media, caption=legenda)
        else:
            await client.send_message(grupo_destino, message=legenda)
    except Exception as e:
        print(f"Erro ao encaminhar mensagem: {e}")

print("Bot rodando... Escutando mensagens.")
client.start()
client.run_until_disconnected()