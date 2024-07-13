from typing import Final
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), application_id='1256379554159792128')

@bot.event
async def on_ready() -> None:
    print(f"{bot.user} is now running!")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")
    
async def main() -> None:
    await load()
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())