import random
import re
import time
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, lionub, lionversion

from ..Config import Config
from ..funcs.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time, lionalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"


@lionub.lion_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✨ "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "✮ HI MASTER I AM ALIVE LION-Z... ✮"
    LION_IMG = gvarstatus("ALIVE_PIC")
    if LION_IMG:
        LION = [x for x in LION_IMG.split()]
        A_IMG = list(LION)
        PIC = random.choice(A_IMG)
        lion_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        lion_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
        lion_caption += f"┣⧼•**{EMOJI} Owner:** {mention}\n"
        lion_caption += f"┣⧼•**{EMOJI} Database :** `{check_sgnirts}`\n"
        lion_caption += f"┣⧼•**{EMOJI} Telethon :** `{version.__version__}\n`"
        lion_caption += f"┣⧼•**{EMOJI} Lion-Z  :** `{lionversion}`\n"
        lion_caption += f"┣⧼•**{EMOJI} Python  :** `{python_version()}\n`"
        lion_caption += f"┣⧼•**{EMOJI} Uptime :** `{uptime}\n`"
        lion_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=lion_caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Owner:** {mention}\n"
            f"**{EMOJI} Lion-Z :** `{lionversion}`\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon :** `{version.__version__}\n`"
            f"**{EMOJI} Python :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`",
        )


@lionub.lion_cmd(
    pattern="lionz$",
    command=("lionz", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}lionz",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ♦️ "
    lion_caption = f"**Lion-Z is Up and Running**\n"
    lion_caption += f"**{EMOJI} Telethon :** `{version.__version__}\n`"
    lion_caption += f"**{EMOJI} Lion-Z :** `{lionversion}`\n"
    lion_caption += f"**{EMOJI} Python :** `{python_version()}\n`"
    lion_caption += f"**{EMOJI} Owner:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, lion_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@lionub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await lionalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
