"""
Created by @Jisan7509
modified by  @mrconfused
Userbot plugin for CatUserbot
"""
#ported by Sh1vam For javes
#Bug fixed by Sh1vam
import emoji
from pyfile import *

#from ub import CMD_HELP
#from ub import bot as borg

#from ub.utils import 
#from ub.helpers import fonts as emojify


@ultroid_cmd(pattern="eem(?: |$)(.*)")

async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(
             "What am I Supposed to do with this , Give me a text. "
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)


@ultroid_cmd(pattern="cmoji(?: |$)(.*)")

async def itachi(event):
    ars = event.text
    args = ars[7:]
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(
             "What am I Supposed to do with this , Give me a text. "
        )
        return
    try:
         arg,emoji = args.split(";")
    except:
        arg = args
        emoji = "😺"
    '''if not char_is_emoji(emoji):
        arg = args
        emoji = "😺"'''
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await event.edit(result)


'''def char_is_emoji(character):
    return character in emoji.UNICODE_EMOJI'''