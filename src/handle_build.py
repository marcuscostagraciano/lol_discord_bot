from discord import File, Message

from os import remove as rm
from typing import Final, NoReturn

from .get_screenshot import get_screenshoot

ROLE_ABBREVIATION: Final[dict] = {
    "T": "TOP",
    "J": "JUNGLE",
    "JG": "JUNGLE",
    "M": "MID",
    "A": "ADC",
    "BOT": "ADC",
    "S": "SUPPORT",
    "SUP": "SUPPORT",
}


async def build_handler(*, msg: Message,
                        champ_name: str, role: str) -> NoReturn:
    if role in ROLE_ABBREVIATION:
        role = ROLE_ABBREVIATION[role]

    link = f"https://blitz.gg/lol/champions/{champ_name}/build/?&role={role}"
    HTML_CLASS_BUILD: Final[str] = "⚡58417267"

    try:
        filename: str = f"{champ_name} {role}.png"

        get_screenshoot(link, filename, HTML_CLASS_BUILD)
        await msg.channel.send(f"<@{msg.author.id}>, here's the build for " +
                               f"{filename}:",
                               file=File(filename))
        rm(filename)

    except Exception as e:
        raise e
