from discord import Message

from typing import NoReturn

from .get_screenshot import get_screenshoot


async def wiki_handler(msg: Message, champ_name: str,
                       *opts: list[str]) -> NoReturn:
    ...
