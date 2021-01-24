import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"



@borg.on(admin_cmd(pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    ghanta = borg.uid
    event = await edit_or_reply(event, "__**(★ Kong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"Commands Found in alive:\n★ **Dark Cobra userbot alive :** `.dclive`\n★ **Jarvis userbot alive :** `.arlive`\n★ **Cat userbot alive :** `.clive`\n★ **Friday userbot alive :** `.flive`\n★ **javes 3.0 userbot alive :** `.jlive`\n\n)"
    )


CMD_HELP.update(
    {
        "ping": "__**PLUGIN NAME :** King__\
    \n\n📌** CMD ★** `.pingy`\
    \n**USAGE   ★  **A kind of ping with extra animation\
    \n\n📌** CMD ★** `.king`\
    \n**USAGE   ★  **Shows you the ping speed of server"
    }
)
