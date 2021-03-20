#from ub.events import *
@bot.on(admin_cmd(pattern="bins",incoming=True))
async def binss(event):
  await event.reply("""
Bins list 
542034xxxxxxxxxx
54271731xxxxxxx
510346001xxxxxxx
554350xxxxxxxxxx
549184271xxxxxx
""")