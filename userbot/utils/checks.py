from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from ..funcs.logger import logging

LOGS = logging.getLogger(__name__)


# Admin checker by uniborg
async def is_admin(lionub, chat_id, userid):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await lionub(GetParticipantRequest(chat_id, userid))
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False
