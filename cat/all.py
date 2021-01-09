import asyncio
from datetime import datetime


@bot.on(admin_cmd(pattern="at$"))
@bot.on(sudo_cmd(pattern="at$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "     **✦҈͜͡➳ Rootedcyber ( Maruf ) **\n★ __**My**__ __**Group**__ [ROOTEDCYBER](https://t.me/rootedcyber1) \n**★ Join My channel :** [channel](https://t.me/rootedcyberchannel)\n**★ My github :** [Github](https://github.com/rooted-cyber/)\n**★ My Blog :** [link](https://rootedcyber.blogspot.com/)")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("     **✦҈͜͡➳ Rootedcyber ( Maruf ) **\n★ {ms} microseconds \n★ __**My**__ __**Master**__ [{DEFAULTUSER}](tg://user?id={ghanta}) \n Type **.help** to see userbot menu!\n`{}`".format(ms))




CMD_HELP.update(
    {
        "ping": "**Plugin :** `Info plugin`\
    \n\n  •  **Syntax :** `.at`\
    \n  •  **Function : **__Shows many info\
    \n\n  •  **Syntax : **`.fping`\
    \n  •  **Function : **__Shows the server ping with extra animation__\
    "
    }
)
