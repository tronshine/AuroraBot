import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from config import settings

load_dotenv()

token = "MTAxMzkzMzU1Nzg1MDMyMDk2Ng.G71O61.VxMcA7EypAS7AxOLS8SviVAZEZh5RAxsh00FYY"

client = commands.Bot(
    command_prefix=settings["PREFIX"],
    case_insensitive=True,
    intents=nextcord.Intents.all(),
    activity=nextcord.Game(name=f"You cute! /help")
)

# REWRITE all database to one connect at bot init and working with cursors

# ADD recursive method of cogs loading

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[: -3]}")
            print(f"cogs.{filename[: -3]} loaded")
    client.run(token, reconnect=True)
