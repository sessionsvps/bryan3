from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(20878509)
    api_hash = "c46b81016b7273f7799a8e88ec9200d0"
    phone_number = "51990965348"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmav3", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4722699331")

    @client.on(events.NewMessage)
    async def my_event_handler(event):
        # Verificar si el mensaje proviene de un chat privado
        if event.is_private:
            sender = await event.get_sender()
            sender_id = sender.id
            message = event.message.message
            # Responder solo en chats privados
            await client.send_message(sender_id, "Esta es una cuenta solo de Spam. Si estas interesado en algun servicio, escríbeme en @DeannWinch indicando el servicio.")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spmav3", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam","RESPALyaDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmav3", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmav3", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(10)
                        if j==12: break
            await client.send_message("@spmav3", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(100) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())
