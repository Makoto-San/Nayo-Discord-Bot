import discord
import discord.utils
from discord.ext import commands

class help(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  # THIS COG IS IN DEV TO BE UPDATED
  # Old Help Command that work but i don't use it

  # Affiche la liste des Commands
  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(
        title="🕹️ Important Links 🕹️️",
        description=
        f"**Commands List** : https://nayobot.moe/commands\n**Support Website** : https://www.patreon.com/nayobot\n**Website** : https://nayobot.moe",
        colour=0xd0c0e9)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)