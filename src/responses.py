from discord import Message

from typing import NoReturn

from .handle_build import build_handler
from .handle_wiki import wiki_handler


async def get_response(*, BOT_COMMAND: str, msg: Message,
                       user_msg: str) -> None | NoReturn:
    user_msg: str = user_msg[len(BOT_COMMAND):]

    match user_input := user_msg.upper().split(" "):
        case ["?"] | ["?", *_]:
            await msg.channel.send(f"Use {BOT_COMMAND} [nome do campeao] [lane]")

        case [("B" | "BUILD"), str(), str()]:
            try:
                await build_handler(msg=msg, champ_name=user_input[1],
                                    role=user_input[2])
            except Exception as e:
                raise e

        case [("W" | "WIKI"), str(), *_]:
            try:
                await wiki_handler(msg=msg, champ_name=user_input[1],
                                   opts=user_input[2:])
            except Exception as e:
                raise e

        case _:
            raise ValueError(
                "Desculpe, mas não entendi sua mensagem\n" +
                f"Use {BOT_COMMAND} ? para saber mais"
                )
