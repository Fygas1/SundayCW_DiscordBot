import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import openai
import os

class chat_cmds(commands.Cog):    
    
    def __init__(self, bot):
        self.bot = bot
        load_dotenv()
        openai.api_key=os.getenv('OPENAI_API_KEY')
        print("OPEN AI KEY: ", openai.api_key)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Chat GPT commands cog loaded.")

    # Chat command
    @app_commands.command(name="chat",description="Chat with Chat GPT")
    async def chat(interaction: discord.Interaction, *, message: str):
        print("empty for now")


async def setup(bot):
    await bot.add_cog(chat_cmds(bot),guilds=[discord.Object(id='1198196659797114941'),discord.Object(id='994251915208691793')])