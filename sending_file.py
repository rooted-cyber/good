from telethon import events
@bot.on(events.NewMessage(outgoing=True))
async def filee(event):
  text = event.text
  ab = await event.get_reply_message()
  await bot.send_file(text, ab)
  await event.edit("sent Successfully !!!")


