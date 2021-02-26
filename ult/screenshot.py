"""
`Credits` @amnd33p
"""
import io
import traceback
from datetime import datetime

import requests
from selenium import webdriver
from validators.url import url
#from wolf.events import admin_cmd
#from wolf import CMD_HELP
#from wolf import bot as borg
#from wolf.wolfbot.heroku_var import Config
from webdriver_manager.chrome import ChromeDriverManager

import asyncio
import os
from re import match

import aiofiles
from selenium import webdriver
#from wolf import bot as wolfs
#from wolf.wolfbot.heroku_var import Config
#from wolf.utils import admin_cmd
#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@ultroid_cmd(
    pattern="stt",
)
#@bot.on(admin_cmd(pattern="ss (.*)"))
#@bot.on(sudo_cmd(pattern="ss (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        returni
    if Config.TEMP_DOWNLOAD_DIRECTORY is None:
        await event.edit("Need to install Google Chrome. Module Stopping.")
        return
    catevent = await event.edit("`Processing ...`")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.binary_location = Config.TEMP_DOWNLOAD_DIRECTORY
        await event.edit("`Starting Google Chrome BIN`")
        #driver = webdriver.Chrome(chrome_options=chrome_options)
        driver = webdriver.Chrome((ChromeDriverManager().install()),chrome_options=chrome_options)
        input_str = event.pattern_match.group(1)
        inputstr = input_str
        caturl = url(inputstr)
        if not caturl:
            inputstr = "http://" + input_str
            caturl = url(inputstr)
        if not caturl:
            await catevent.edit("`The given input is not supported url`")
            return
        driver.get(inputstr)
        await catevent.edit("`Calculating Page Dimensions`")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await catevent.edit("`Stoppping Chrome Bin`")
        driver.close()
        message_id = None
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        end = datetime.now()
        ms = (end - start).seconds
        hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
        await catevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = input_str + ".PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=hmm,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await catevent.edit(f"`{traceback.format_exc()}`")


