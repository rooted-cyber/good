"""
`Credits` @amnd33p
Modified by @mrconfused
"""
import io
import traceback
from datetime import datetime
from selenium import webdriver

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd
from fridaybot import CHROME_DRIVER, CMD_HELP, GOOGLE_CHROME_BIN
from fridaybot.utils import edit_or_reply, sudo_cmd



import requests
from selenium import webdriver


@bot.on(admin_cmd(pattern="ss (.*)"))
@bot.on(sudo_cmd(pattern="ss (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.GOOGLE_CHROME is None:
        await edit_or_reply(event, "Need to install Google Chrome. Module Stopping.")
        return
    catevent = await edit_or_reply(event, "`Processing ...`")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.GOOGLE_CHROME
        await event.edit("`Starting Google Chrome BIN`")
        driver = webdriver.Chrome(chrome_options=chrome_options)
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


