

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


@borg.on(admin_cmd(pattern="flink ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@Files2LinkProBot"
    reply_message.sender
    await event.edit("**Making Downloading url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1474336646)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please restart me (@YtdlUBot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

        


@borg.on(admin_cmd(pattern="ycur ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@YtdlUBot"
    reply_message.sender
    await event.edit("**Making Downloading url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1682170438)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please restart me (@YtdlUBot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

        

@borg.on(admin_cmd(pattern="fcur ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@D2link_bot"
    reply_message.sender
    await event.edit("**Making Downloading url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1045309165)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please restart me (@D2link_bot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

        


@borg.on(admin_cmd(pattern="recognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user's media message.")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("reply to media file")
       return
    chat = "@Rekognition_Bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.")
       return
    cat = await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.edit("unblock @Rekognition_Bot and try again")
              await cat.delete()
              return
          if response.text.startswith("See next message."):
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              response = await response
              cat = response.message.message
              await event.edit(cat)
      
          else:
              await event.edit("sorry, I couldnt find it")
              





@borg.on(admin_cmd(pattern="purl ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

@borg.on(admin_cmd(pattern="limits ?(.*)",incoming=True))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                danish = await conv.get_response()
                final = ("HeHe", "")
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @spambot `and retry!")


@borg.on(admin_cmd(pattern="cur ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@AH_File2Link_Bot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1547434312)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  
@borg.on(admin_cmd(pattern="vcur ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@StreamingLinkBot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1516863073)
            )
            await event.client.forward_messages(chat, reply_message)
            await event.client.forward_messages(chat, reply_message)
            await event.client.forward_messages(chat, reply_message)
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@StreamingLinkBot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  
