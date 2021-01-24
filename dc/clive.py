import time
#from platform import python_version

#from telethon import version

from userbot import ALIVE_NAME
from userbot import Lastupdate

from userbot.utils import sudo_cmd, admin_cmd

DEFAULTUSER = ALIVE_NAME
CAT_IMG = Config.ALIVE_PHOTTO
CUSTOM_ALIVE_TEXT = "✮ MY BOT IS RUNNING SUCCESSFULLY ✮"
EMOJI = "  ✥ "


@bot.on(admin_cmd(outgoing=True, pattern="clive$"))
@bot.on(sudo_cmd(pattern="calive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    #reply_to_id = await reply_id(alive)
    #uptime = await catdef.get_readable_time((time.time() - StartTime))
    #check_sgnirts = check_data_base_heal_th()
    #uptime = get_readable_time((time.time() - Lastupdate))
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        cat_caption += f"**{EMOJI} Database :** `Functioning Normally`\n"
        cat_caption += f"**{EMOJI} Telethon version :** `1.19.0`\n"
        cat_caption += f"**{EMOJI} Catuserbot Version :** `2.10.1`\n"
        cat_caption += f"**{EMOJI} Python Version :** `3.9.1`\n"
        cat_caption += f"**{EMOJI} Uptime :** `Not Available`\n"
        cat_caption += f"**{EMOJI} Master:** {DEFAULTUSER}\n"
        cat_caption += f"**{EMOJI} Github :** [rooted-cyber](https://github.com/rooted-cyber/)\n"
        cat_caption += f"**{EMOJI} Channel :** [Channel](https://t.me/rootedcyberchannel)\n"
        cat_caption += f"**{EMOJI} Group :** [Group](https://t.me/rootedcyber1)\n"
        cat_caption += f"**{EMOJI} Check stats by `.status` {EMOJI}**\n"
        cat_caption += f"**{EMOJI} Check plugin info `.in <plugin name> or .plinfo <plugin name>` {EMOJI}**\n\n"
        cat_caption += f"            **{EMOJI}{EMOJI} ALIVE LIST {EMOJI}{EMOJI}**\n"
        cat_caption += f"**{EMOJI} Dark Cobra alive :** `.dclive`\n"
        cat_caption += f"**{EMOJI} fridayuserbot alive :** `.flive`\n"
        cat_caption += f"**{EMOJI} jarvis alive :** `.arlive`\n"
        cat_caption += f"**{EMOJI} javes 3.0 alive :** `.jlive`\n\n"
        cat_caption += f"**{EMOJI}{EMOJI}** [DEPLOY USERBOT](https://github.com/rooted-cyber/My_Userbot) **{EMOJI}{EMOJI}**\n\n"
        
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** `H`\n"
            f"**{EMOJI} Telethon Version :** `HI`\n`"
            f"**{EMOJI} Catuserbot Version :** `HI`\n"
            f"**{EMOJI} Python Version :** `HI`\n`"
            f"**{EMOJI} Uptime :** `uptime\n`"
            f"**{EMOJI} Master:** HI\n",
        )


