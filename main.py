from discord import Client, Message, Intents
from dotenv import load_dotenv

import os
from typing import Final


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")


def main() -> None:
    print(TOKEN)


if __name__ == "__main__":
    main()
