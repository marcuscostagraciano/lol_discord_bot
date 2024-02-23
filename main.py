# Installed modules
from dotenv import load_dotenv
from discord import Client, Message, Intents

# Built-ins
import json
import logging
import logging.config
from os import getenv
from typing import Final, NoReturn

from src.responses import get_response


logger = logging.getLogger('discord_bot')

CONFIG_FILE: Final[str] = r"config.json"

with open(CONFIG_FILE) as log_config_file:
    log_config = json.load(log_config_file)

logging.config.dictConfig(log_config)

load_dotenv()
TOKEN: Final[str] = getenv("DISCORD_TOKEN")
BOT_COMMAND: Final[str] = getenv("BOT_COMMAND")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# When the bot is ready, logs it
@client.event
async def on_ready() -> None:
    logger.info(f"{client.user} is alive!")


async def send_message(msg: Message, user_msg: str) -> None | NoReturn:
    try:
        await get_response(BOT_COMMAND, msg, user_msg)
    except Exception as e:
        await msg.channel.send(f"[<@{msg.author.id}>]: {e}")


# Activates every message
@client.event
async def on_message(msg: Message) -> None:
    # Prevents the bot from answering itself
    if msg.author == client.user:
        return

    # Logs and send responses only if the message start with the bot command
    # OR the bot is mentioned
    if msg.content.startswith(BOT_COMMAND) or client.user.mentioned_in(msg):
        username: str = str(msg.author)
        user_msg: str = msg.content
        channel: str = str(msg.channel)

        logger.info(f"[{channel}] {username}: '{user_msg}'")
        await send_message(msg, user_msg)


def main() -> None:
    client.run(token=TOKEN, log_level=logging.WARNING)


if __name__ == "__main__":
    main()
