from telethon import events
@bot.on(events.NewMessage(outgoing=True, incoming=False))
async def hi(event):
  text = event.text
  for a in range(1):
    await bot.send_file(event.chat_id, text)

