from discord import File, Message

from typing import Final, NoReturn
from os import remove as rm

from .get_screenshot import get_screenshoot

role_abbreviation: Final[dict] = {
    "T": "TOP",
    "J": "JUNGLE",
    "JG": "JUNGLE",
    "M": "MID",
    "A": "ADC",
    "S": "SUPPORT",
    "SUP": "SUPPORT",
}


async def build_handler(*, msg: Message,
                        champ_name: str, role: str) -> NoReturn:
    if role in role_abbreviation:
        role = role_abbreviation[role]

    link = f"https://blitz.gg/lol/champions/{champ_name}/build/?&role={role}"
    HTML_CLASS_BUILD: Final[str] = "⚡58417267"

    try:
        filename: str = f"{champ_name} {role}.png"

        get_screenshoot("build", link, filename, HTML_CLASS_BUILD)
        await msg.channel.send(f"<@{msg.author.id}>, here's the build for " +
                               f"{champ_name} {role}:",
                               file=File(filename))
        rm(filename)
    except Exception as e:
        raise e
