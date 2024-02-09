from discord import Message, File

from os import remove as rm
from typing import Final, NoReturn

from . import get_screenshot

role_abbreviation: Final[dict] = {
    "T": "TOP",
    "J": "JUNGLE",
    "M": "MID",
    "A": "ADC",
    "S": "SUPPORT"
}


async def get_reponse(*, BOT_COMMAND: str, msg: Message,
                      user_msg: str) -> NoReturn:
    user_msg: str = user_msg[len(BOT_COMMAND) + 1:]
    user_input: list[str] = user_msg.upper().split(" ")

    match user_input[0]:
        case "?":
            await msg.channel.send("Use !LOLKO {nome do campeao} {lane}")
        case _:
            champ_name: str = user_input[0]
            role: str = user_input[1]

            if role in role_abbreviation:
                role = role_abbreviation[role]

            filename: str = f"{champ_name} {role}.png"

            try:
                get_screenshot.get_screenshoot(champ_name, role)
                await msg.channel.send(f"<@{msg.author.id}>, here's the build for " +
                                       f"{champ_name} {role}:",
                                       file=File(filename))
                rm(filename)
            except Exception as e:
                print(e)
