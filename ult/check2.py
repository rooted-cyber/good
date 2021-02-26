# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}meaning <word>`
    Get the meaning of the word.

• `{i}synonym <word>`
    Get all synonyms.

• `{i}antonym <word>`
    Get all antonyms.

• `{i}ud <word>`
    Fetch word defenition from urbandictionary.
"""

import asyncurban
from PyDictionary import PyDictionary

from . import *

dictionary = PyDictionary()


@ultroid_cmd(
    pattern="check",
)
async def mean(event):
	  	  await event.edit("[hello](https://google.com)")
	  	  await event.reply("[Github](https://github.com/rooted-cyber/)\n[Group](https://t.me/rootedcyber1)")




