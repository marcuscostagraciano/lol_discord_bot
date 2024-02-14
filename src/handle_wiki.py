from discord import File, Message

import logging
from os import remove as rm
from typing import Final, NoReturn

# from .get_screenshots import get_wiki

CLASS_ABBREVIATION: Final[dict] = {
    "P": "skill_innate",
    "PASSIVA": "skill_innate",
    "Q": "skill_q",
    "W": "skill_w",
    "E": "skill_e",
    "R": "skill_r",
    "U": "skill_r",
    "ULT": "skill_r",
}


async def wiki_handler(msg: Message, champ_name: str,
                       opts: list[str]) -> None | NoReturn:
    raise NotImplementedError("WIP (maybe someday)")

    champ_name = champ_name.lower().capitalize()
    link: str = f"https://leagueoflegends.fandom.com/wiki/{champ_name}/LoL"

    logging.info(f"Getting the wiki for: {champ_name} {opts}")

    try:
        for opt in opts:
            logging.debug(f"Wiki for: {champ_name}\n" +
                          f"{link=}")

            filename: str = f"{champ_name} {opt}.png"

            get_wiki(link, filename, CLASS_ABBREVIATION[opt])
            await msg.channel.send(
                f"<@{msg.author.id}>, here's the wiki for " +
                f"{filename}:",
                file=File(filename))
            rm(filename)

    except Exception as e:
        raise e
