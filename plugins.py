import math
from . import humanbytes
import asyncio
@ultroid_cmd(pattern="sqrt|.sq ?(.*)", outgoing= True,incoming=True)
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any square number !!!")
  return
 await event.reply(str(math.sqrt(int(text))))
 


@ultroid_cmd(pattern="square ?(.*)", outgoing= True,incoming=True)
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any number !!!")
  return
 await event.reply(str(f"{text} X {text} = {int(text)*int(text)}"))


@ultroid_cmd(pattern="cube ?(.*)", outgoing= True,incoming=True)
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter any number !!!")
  return
 await event.reply(str(f"{text} X {text} X {text} = {int(text)*int(text)*int(text)}"))


@ultroid_cmd(pattern="table ?(.*)", outgoing= True,incoming=True)
async def hi(event):
 text = event.pattern_match.group(1)
 if not text:
  await event.edit("Please enter Table no !!!")
  return
 await event.edit(f"Starting Table in {text}")
 await event.reply(str(f""" {text} X 1 = {int(text)*1}
{text} X 2 = {int(text)*2}
{text} X 3 = {int(text)*3}
{text} X 4 = {int(text)*4}
{text} X 5 = {int(text)*5}
{text} X 6 = {int(text)*6}
{text} X 7 = {int(text)*7}
{text} X 8 = {int(text)*8}
{text} X 9 = {int(text)*9}
{text} X 10 = {int(text)*10}
"""))


@ultroid_cmd(pattern="mcopy", outgoing= True, incoming=True)
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Reply any message !")
    return
  abc = ab.text
  await event.edit("processing..")
  await ab.reply(f"reply messages : {abc}")



@ultroid_cmd(pattern="rename ?(.*)",incoming=True,outgoing=True)
async def hi(event):
  text = event.pattern_match.group(1)
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Reply any file or type name !!")
    return
  await event.edit("`processing..`")
  await ab.download_media(text)
  await event.edit("Proccessing Done ✔️")
  await asyncio.sleep(1)
  await event.edit("Now sending file")
  await asyncio.sleep(0.1)
  await bot.send_file(event.chat_id, text)


@ultroid_cmd(pattern="mcount", outgoing= True, incoming=True)
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
   await event.edit("Reply any message !!!")
  abc = ab.text
  await ab.reply(f"Total messages : {len(abc)}")


@ultroid_cmd(pattern="cadmin",incoming=True,outgoing=True)
async def adm(event):
  a = await event.get_reply_message()
  if not a:
   await event.edit("Reply any user !")
   return
  ab = await bot.get_permissions(event.chat_id, a.sender_id)
  if ab.is_admin:
    await a.reply("yes, He is admin")
  else:
    await a.reply("No, He is not admin")



@ultroid_cmd(pattern="mm")
async def _(event):
  a = await bot.get_messages(event.chat_id, 0, from_user="me")
  b = await bot.get_messages(event.chat_id)
  await event.reply(f" Your Total messages = {a.total}\n\n And Total group messages : {b.total}")



@ultroid_cmd(pattern="cs")
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply any file`")
    return
  b = ab.file.size
  a = humanbytes (b)
  await bot.send_message(event.chat_id,f"Your file size = {str(a)}")



@ultroid_cmd(pattern="pd")
async def ppd(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply any message`")
    return
  b = await bot.download_profile_photo(ab.sender_id)
  if not b:
    await event.edit("`This user has no any profile pic`")
    return
  await event.edit("Sending profile pic")
  await asyncio.sleep(2)
  await event.reply(file=b)



