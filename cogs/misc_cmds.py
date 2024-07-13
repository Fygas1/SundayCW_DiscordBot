import discord
from discord.ext import commands
from discord import app_commands

class misc_cmds(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help') #Disable the help command

    @commands.Cog.listener()
    async def on_ready(self):
        print("Misc commands cog loaded.")

    # Sync
    @commands.command()
    async def sync(self,ctx) -> None:
        fmt=await ctx.bot.tree.sync()
        await ctx.send(f'Synced {len(fmt)} commands.')
        return

    # Ping command
    @app_commands.command(name="ping",description="Check ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.bot.latency * 1000)} ms')

    @app_commands.command(name="helpp", description="Get help information")
    async def helpp(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help", description="This is a help message with some text.", color=discord.Color.blue())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(misc_cmds(bot))