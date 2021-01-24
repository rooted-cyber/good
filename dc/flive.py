"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
# Ported from black lightning
import os
import time

from userbot import ALIVE_NAME, Lastupdate
#from userbot.plugins import currentversion
from userbot.utils import admin_cmd, sudo_cmd

FRI_IMAGE = os.environ.get("FRI_IMAGE", None)
if FRI_IMAGE is None:
    FRI_IMG = "https://telegra.ph/file/1b59b48817b6b2dde6f11.jpg"
else:
    FRI_IMG = FRI_IMAGE


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

pm_caption = "➥ **ROOTEDCYBER bot is:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.19.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += f"➥ **Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `2.20.2`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](https://github.com/KeinShin/Black-Lightning/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [rooted-cyber@Github](GitHub.com/rooted-mcyber)\n"
pm_caption += "➥ **Github** : [rooted-cyber](https://github.com/rooted-cyber/)\n"
pm_caption += "➥ **Channel :** [Channel](https://t.me/rootedcyberchannel)\n"
pm_caption += "➥ **Group :** [Group](https://t.me/rootedcyber1)\n"
pm_caption += "➥ **Check status by `.status`**\n"
pm_caption += "➥ **Check plugin info `.in <plugin name> or .plinfo <plugin name>`**\n\n"
pm_caption += "         ➥ **ALIVE LIST**\n"
pm_caption += "➥ **Dark cobra alive :** `.dclive`\n"
pm_caption += "➥ **catuserbot alive :** `.clive`\n"
pm_caption += "➥ **jarvis alive :** `.arlive`\n"
pm_caption += "➥ **javes 3.0 alive :** `.jlive`\n\n"

pm_caption += (
    "[🇮🇳 Deploy userbot 🇮🇳](https://github.com/rooted-cyber/My_Userbot)"
)


@borg.on(admin_cmd(pattern=r"flive"))
@borg.on(sudo_cmd(pattern=r"flive", allow_sudo=True))
async def friday(falive):
    await falive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(falive.chat_id, FRI_IMG, caption=pm_caption)
    await falive.delete()
