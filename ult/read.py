

import asyncio
import random, re
import datetime
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
#from userbot import CMD_HELP
#from userbot.utils import admin_cmd
#from var import Var
telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")

@ultroid_cmd(pattern="read")
#@borg.on(admin_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**Reply to a URL.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("**Reply to a url message.**")
       return
    chat = "@chotamreaderbot"
    sender = reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=272572121))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please unblock me @chotamreaderbot")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)




  
