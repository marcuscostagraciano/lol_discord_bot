from discord import Message, File

from os import remove as rm
from typing import Final, NoReturn

from . import get_screenshot

role_abbreviation: Final[dict] = {
    "T": "TOP",
    "J": "JUNGLE",
    "JG": "JUNGLE",
    "M": "MID",
    "A": "ADC",
    "S": "SUPPORT",
    "SUP": "SUPPORT",
}


async def get_reponse(*, BOT_COMMAND: str, msg: Message,
                      user_msg: str) -> NoReturn:
    user_msg: str = user_msg[len(BOT_COMMAND):]
    # user_input: list[str] = user_msg.upper().split(" ")

    match user_input := user_msg.upper().split(" "):
        case ["?"] | ["?", *_]:
            await msg.channel.send(f"Use {BOT_COMMAND} [nome do campeao] [lane]")

        case [str(), str()]:
            try:
                champ_name: str = user_input[0]
                role: str = user_input[1]

                if role in role_abbreviation:
                    role = role_abbreviation[role]

                filename: str = f"{champ_name} {role}.png"

                get_screenshot.get_screenshoot(champ_name, role)
                await msg.channel.send(f"<@{msg.author.id}>, here's the build for " +
                                       f"{champ_name} {role}:",
                                       file=File(filename))
                rm(filename)
            except Exception as e:
                print(e)
                await msg.channel.send(f"[<@{msg.author.id}>]: {e}")

        case _:
            await msg.channel.send(
                f"Desculpe, [<@{msg.author.id}>], mas não entendi sua mensagem\n" +
                f"Use {BOT_COMMAND} ? para saber mais"
                )
