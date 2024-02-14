from discord import File, Message

import logging
from os import remove as rm
from typing import Final, NoReturn

from .get_screenshots import get_build

ROLE_ABBREVIATION: Final[dict] = {
    "T": "TOP",
    "J": "JUNGLE",
    "JG": "JUNGLE",
    "M": "MID",
    "A": "ADC",
    "BOT": "ADC",
    "B": "ADC",
    "S": "SUPPORT",
    "SUP": "SUPPORT",
}


async def build_handler(*, msg: Message,
                        champ_name: str, role: str) -> None | NoReturn:
    if role in ROLE_ABBREVIATION:
        role = ROLE_ABBREVIATION[role]

    logging.info(f"Getting the build for: {champ_name} {role}")

    link = f"https://blitz.gg/lol/champions/{champ_name}/build/?&role={role}"
    HTML_CLASS_BUILD: Final[str] = "⚡58417267"

    try:
        filename: str = f"{champ_name} {role}.png"

        get_build(link, filename, HTML_CLASS_BUILD)
        await msg.channel.send(f"<@{msg.author.id}>, here's the build for " +
                               f"{filename}:",
                               file=File(filename))
        rm(filename)

    except Exception as e:
        raise e
