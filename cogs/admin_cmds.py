import asyncio
import discord
from typing import Optional
from discord.ext import commands
from discord import app_commands


class admin_cmds(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands cog loaded.")

    # ⚙️ Clears messages from a text channel.
    @app_commands.command(name="clear",description="Clear number of messages in this channel")
    @discord.app_commands.checks.has_role(1232067953675993158)
    async def clear(self, interaction: discord.Interaction, amount: int | None):

        if isinstance(amount, int) and amount is not None:
            await interaction.response.defer(ephemeral=True)
            deleted = await interaction.channel.purge(limit=amount)
            return await interaction.followup.send(f"Cleared {len(deleted)} messages", ephemeral=True)


        embed = discord.Embed(
            title="⚠️ You Have Not Selected a Number of Messages to Clear",
            description="❓ Would you like to clear all messages in this channel?",
        )

        view = ClearMessagesView(interaction)
        view.message = await interaction.response.send_message(embed=embed, view=view)   


async def setup(bot):
    await bot.add_cog(admin_cmds(bot),guilds=[discord.Object(id='1198196659797114941'),discord.Object(id='994251915208691793')])

class ClearMessagesView(discord.ui.View):

    def __init__(self, interaction: discord.Interaction, *, timeout: Optional[float] = 180):
        super().__init__(timeout=timeout)
        self.interaction = interaction

    #Called when the view times out.
    async def on_timeout(self) -> None:
        await self.disable_all_buttons()

    #Disables all buttons.
    async def disable_all_buttons(self, interaction: discord.Interaction = None):
        interaction = interaction or self.interaction

        for child in self.children:
            child.disabled = True

        await interaction.message.edit(view=self)
        self.stop()

    #Prevents users who weren't the command sender from using buttons.
    async def interaction_check(self, interaction: discord.Interaction) -> bool:      

        if interaction.user.id == self.interaction.user.id:
            return True
        else:
            await interaction.response.send_message(
                ":x: This isn't your interaction!", ephemeral=True
            )
            return False

    #Callback method for the yes button.
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, emoji="👍🏻")
    async def yes(self, interaction: discord.Interaction, _: discord.Button):
        await interaction.response.defer()  # manually defer interaction for an increased respond time

        channel_pos = interaction.channel.position
        category = interaction.channel.category
        new_channel = await interaction.channel.clone()

        await new_channel.edit(category=category, position=channel_pos)
        await interaction.channel.delete()

        self.stop()

    #Callback method for the no button.
    @discord.ui.button(label="No", style=discord.ButtonStyle.red, emoji="👎🏻")
    async def no(self, interaction: discord.Interaction, _: discord.Button):
        await interaction.response.send_message("👍🏻 Aborting command.", ephemeral=True)
        await self.disable_all_buttons(interaction)
