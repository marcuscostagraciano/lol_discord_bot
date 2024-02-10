from discord import File, Message

from os import remove as rm
from typing import Final, NoReturn

from .get_screenshot import get_screenshoot

CLASS_ABBREVIATION: Final[dict] = {
    "P": "skill skill_innate",
    "PASSIVA": "skill skill_innate",
    "Q": "skill skill_q",
    "W": "skill skill_w",
    "E": "skill skill_e",
    "R": "skill skill_r",
    "U": "skill skill_r",
    "ULT": "skill skill_r",
}


async def wiki_handler(msg: Message, champ_name: str,
                       opts: list[str]) -> NoReturn:
    raise NotImplementedError("WIP\n" +
                              f"passed args: {champ_name=}\n{opts=}")

    champ_name = champ_name.lower().capitalize()
    link: str = f"https://leagueoflegends.fandom.com/wiki/{champ_name}/LoL"

    try:
        for opt in opts:
            filename: str = f"{champ_name} {opt}.png"
            print(f"{link=}")
            print(f"{filename=}")
            print(f"{CLASS_ABBREVIATION[opt]=}")

            get_screenshoot(link, filename, CLASS_ABBREVIATION[opt])
            await msg.channel.send(f"<@{msg.author.id}>, here's the wiki for " + # NOQA
                                   f"{filename}:",
                                   file=File(filename))
            rm(filename)

    except Exception as e:
        raise e
