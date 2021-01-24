import platform
import sys
#from telethon import version
from userbot import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID)
#from userbot.events import javes05, rekcah05 
import os
import asyncio
from telethon import events
import heroku3
#FULL_SUDO = os.environ.get("FULL_SUDO", None)
from var import Var
#rksu = Var.SUDO_USERS
DEFAULTUSER = "rootedcyber"
from datetime import datetime
from userbot import CMD_HELP, ALIVE_NAME
#client2 = client3 = None


@bot.on(events.NewMessage(outgoing=True, pattern='.jlive'))
async def alive(alive):
    await alive.edit(""
                    f"**ALIVE_S_MMSG**\n\n"                     
                    f" °  `JAVES NAME `: **MARUF**\n"
                    f" °  `User:` ** @{DEFAULTUSER} **\n"
                    f" °  `Telethon`: ** 1.19.0**\n"
                    f" °  `Python` : **3.8.5**\n"                                                                                     
                    f" °  `Os:` **Kali GNU/Linux Rolling x86_64**\n"                                       
                    f" °  `Heroku:` **Userbot**\n"
                    f" °  `LogChat:` **bot**\n"
                    f" °  `Sudo:` **Disable**\n"           
                    f" °  `SpamProtect:` **yes**\n"       
                    f" °  `Uptime:` **Not Available**\n"
                    f" °  `Github` : [rooted-cyber](https://github.com/rooted-cyber/)\n"
                    f" °  `Channel` : [Channel](https://t.me/rootedcyberchannel)\n"
                    f" °  `Group` : [Group](https://t.me/rootedcyber1)\n"
                    f" °  `Check status by` **.status**\n"
                    f" °  `Check plugin info` **.in <plugin name> or .plinfo <plugin name>**\n\n")



