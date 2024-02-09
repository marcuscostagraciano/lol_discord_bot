from discord import Client, Message, Intents
import discord
from dotenv import load_dotenv

import os
from typing import Final

from src import get_reponse

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
BOT_COMMAND: Final[str] = "!LOLKO"

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message(msg: Message, user_msg: str) -> None:
    if user_msg.startswith(BOT_COMMAND):
        user_msg = user_msg[len(BOT_COMMAND) + 1:]

    try:
        response: str = get_reponse(user_msg)
        await msg.channel.send(f"{msg.author}, here's the build for {response}:",
                               file=discord.File(f'{response}.png'))
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f"{client.user} is alive!")


@client.event
async def on_message(msg: Message) -> None:
    if msg.author == client.user:
        return

    username: str = str(msg.author)
    user_msg: str = msg.content
    channel: str = str(msg.channel)

    print(f"[{channel}] {username}: '{user_msg}'")
    await send_message(msg, user_msg)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
