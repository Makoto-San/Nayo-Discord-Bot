import discord
import discord.utils
import random
import asyncio
import re
import PIL
import datetime
import tasks
from random import choice
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw, ImageFont
import PIL.ImageOps
 
class eco(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  # THIS COG IS IN DEV TO BE UPDATED
  # This commands are old commands that work with my old database :

  @commands.command()
  @commands.cooldown(1, 60*60*24, commands.cooldowns.BucketType.user)
  async def tickets(self, ctx):
    value = int(db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset"))
    if value is None:
      await ctx.send("You have to create a Bank Account, use >bank")
    else:
      if value == 0:
        value += 10
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 1:
        value += 9
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 2:
        value += 8
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 3:
        value += 7
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 4:
        value += 6
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 5:
        value += 5
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 6:
        value += 4
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 7:
        value += 3
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 8:
        value += 2
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")
      if value == 9:
        value += 1
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        await ctx.send("Nayo Daily Tickets Recharged 🎟️")

  @tickets.error
  async def tickets_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      connvert = str(datetime.timedelta(seconds=666))
      msg = '🎟️ You already recharged your tickets... come back in {:.2f}s (24h)'.format(error.retry_after)
      await ctx.send(msg)


  @commands.command()
  async def bank(self, ctx):
    value = db.get(f"{ctx.guild.id}-{ctx.author.id}")
    value2 = db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset")
    if value is None:
      if value2 is None:
        db[f"{ctx.guild.id}-{ctx.author.id}"] = "0"
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = "10"
        await ctx.send(f"🏦 **Bank Account Created for {ctx.author.mention}**")
    else:
      await ctx.send("You already have a Bank Account 🏦")


  @commands.command()
  async def wallet(self, ctx):
    value = db.get(f"{ctx.guild.id}-{ctx.author.id}")
    value2 = db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset")
    if value is not None:
      if value2 is not None:
        embed = discord.Embed(title="Wallet 💰", description=f"Your Nayo Coins : `{value}` 🪙\nYour Nayo Daily Tickets : `{value2}` 🎟️", color=0xd0c0e9)
        await ctx.send(embed=embed)
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @commands.command()
  async def hunt(self, ctx):
    liste = ["Boar 🐗","Unicorn 🦄","Stag 🦌","Beef 🐂","Rat 🐁","Rat 🐁","Rabbit 🐇"]
    number_coins = int(db.get(f"{ctx.guild.id}-{ctx.author.id}"))
    value = int(db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset"))
    if value is not None:
      if number_coins is not None:
        if value > 0:
          value -= 1
          del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
          db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
          choice = random.choice(liste)
          if choice == "Boar 🐗":
            number_coins += 6
            coins = 6
            del db[f"{ctx.guild.id}-{ctx.author.id}"]
            db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
            embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
            await ctx.send(embed=embed)
          if choice == "Unicorn 🦄":
      	    number_coins += 10
      	    coins = 10
      	    del db[f"{ctx.guild.id}-{ctx.author.id}"]
      	    db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
      	    embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
      	    await ctx.send(embed=embed)
          if choice == "Stag 🦌":
            number_coins += 5
            coins = 5
            del db[f"{ctx.guild.id}-{ctx.author.id}"]
            db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
            embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
            await ctx.send(embed=embed)
          if choice == "Beef 🐂":
      	    number_coins += 3
      	    coins = 3
      	    del db[f"{ctx.guild.id}-{ctx.author.id}"]
      	    db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
      	    embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
      	    await ctx.send(embed=embed)
          if choice == "Rabbit 🐇":
      	    number_coins += 3
      	    coins = 3
      	    del db[f"{ctx.guild.id}-{ctx.author.id}"]
      	    db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
      	    embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
      	    await ctx.send(embed=embed)
          if choice == "Rat 🐁":
      	    number_coins += 2
      	    coins = 2
      	    del db[f"{ctx.guild.id}-{ctx.author.id}"]
      	    db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
      	    embed = discord.Embed(title="Hunt 🏹", description=f"You caught a {choice}\nYou earn `{coins}` Coins 🪙", color=0xd0c0e9)
      	    await ctx.send(embed=embed)
        else:
          await ctx.send("❌ Nayo Tickets Insufficient")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @hunt.error
  async def hunt_error(self, ctx, error):
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'Wait {:.2f}s (30m) to Hunt something 🏹'.format(error.retry_after)
      await ctx.send(msg)

  @commands.command()
  async def coins(self, ctx):
    value = int(db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset"))
    if value is not None:
      if value > 0:
        value -= 1
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        number_coins = int(db[f"{ctx.guild.id}-{ctx.author.id}"])
        number_coins += 5
        del db[f"{ctx.guild.id}-{ctx.author.id}"]
        db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
        embed = discord.Embed(description="You earn 5 Coins 🪙", color=0xd0c0e9)
        await ctx.send(embed=embed)
      else:
        await ctx.send("❌ Nayo Tickets Insufficient")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @commands.command()
  async def fishing(self, ctx):
    value = int(db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset"))
    if value is not None:
      if value > 0:
        value -= 1
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        number_coins = int(db[f"{ctx.guild.id}-{ctx.author.id}"])
        prizelist = ["Blow Fish 🐡","Tropical Fish 🐠","Fish 🐟","Fish 🐟","Octopus 🐙","Whale 🐳","Fish 🐟"]
        prize = random.choice(prizelist)
        if prize == "Blow Fish 🐡":
          number_coins += 8
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title=f"You find a {prize}", description="You earn 8 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
        if prize == "Tropical Fish 🐠":
          number_coins += 9
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title=f"You find a {prize}", description="You earn 9 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
        if prize == "Fish 🐟":
          number_coins += 4
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title=f"You find a {prize}", description="You earn 4 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
        if prize == "Octopus 🐙":
          number_coins += 10
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title=f"You find a {prize}", description="You earn 10 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
        if prize == "Whale 🐳":
          number_coins += 12
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title=f"You find a {prize}", description="You earn 12 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
      else:
        await ctx.send("❌ Nayo Tickets Insufficient")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @commands.command()
  async def slotmachine(self, ctx):
    value = int(db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset"))
    if value is not None:
      if value > 0:
        value -= 1
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"] = f"{value}"
        number_coins = int(db[f"{ctx.guild.id}-{ctx.author.id}"])
        liste = ["1","2","3","4","5","6","7","8","9"]
        liste2 = ["1","2","3","4","5","6","7","8","9"]
        liste3 = ["1","2","3","4","5","6","7","8","9"]
        choice = random.choice(liste)
        choice2 = random.choice(liste2)
        choice3 = random.choice(liste3)
        if choice == choice2 == choice3:
          number_coins += 30
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
          embed = discord.Embed(title="Slot Machine 🎰", description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn 20 Coins 🪙", color=0xd0c0e9)
          await ctx.send(embed=embed)
        else:
          if choice == choice2 or choice == choice3 or choice2 == choice3:
            number_coins += 7
            del db[f"{ctx.guild.id}-{ctx.author.id}"]
            db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
            embed = discord.Embed(title="Slot Machine 🎰", description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn 7 Coins 🪙", color=0xd0c0e9)
            await ctx.send(embed=embed)
          else:
            number_coins += 1
            del db[f"{ctx.guild.id}-{ctx.author.id}"]
            db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins}"
            embed3 = discord.Embed(title="Slot Machine 🎰",     description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn 1 Coins 🪙", color=0xd0c0e9)
            await ctx.send(embed=embed3)
      else:
        await ctx.send("❌ Nayo Tickets Insufficient")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @commands.command()
  async def reset(self, ctx):
    value1 = db.get(f"{ctx.guild.id}-{ctx.author.id}")
    value2 = db.get(f"{ctx.guild.id}-{ctx.author.id}-DailyReset")
    if value1 is not None:
      if value2 is not None:
        del db[f"{ctx.guild.id}-{ctx.author.id}"]
        del db[f"{ctx.guild.id}-{ctx.author.id}-DailyReset"]
        await ctx.send(f"**Bank Account Reset**\nType `bank` to recreate a bank account")
    else:
      await ctx.send("You don't have a Bank Account")

  @coins.error
  async def earn_error(self, ctx, error):
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Wait {:.2f}s (1h) to earn Coins 🪙'.format(error.retry_after)
        await ctx.send(msg)

  @fishing.error
  async def fish_error(self, ctx, error):
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Wait {:.2f}s (2h) to Fishing 🎣'.format(error.retry_after)
        await ctx.send(msg)

  @slotmachine.error
  async def slot_error(self, ctx, error):
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Wait {:.2f}s (5m) to play Slot Machine 🎰'.format(error.retry_after)
        await ctx.send(msg)

  @commands.command()
  async def exchange(self, ctx):
    number_coins = db.get(f"{ctx.guild.id}-{ctx.author.id}")
    if number_coins is not None:
      number_coins2 = int(db.get(f"{ctx.guild.id}-{ctx.author.id}"))
      a = ["Premium","premium"]
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      embed = discord.Embed(title="💰 Premium Account", description="Get access to more anime gif commands with exchange your coins\nCost : **1000 🪙**\nTo buy it type : **premium**", color=0xd0c0e9)
      embed.set_thumbnail(url="https://i.ibb.co/F4f5y48/Png-Item-3782851.png")
      await ctx.send(embed=embed)
      rep = await self.bot.wait_for('message', check=check)
      if rep.content in a:
        if number_coins2 >= 1000:
          number_coins2 -= 1000
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins2}"
          db[f"Pat-{ctx.author.id}"] = "AccesAuthorized"
          await ctx.send("Congratulations ! Now you have a **Premium Account** !")
        else:
          await ctx.send("You don't have the amount of coins necessary, you can earn coins with `coins`, `fishing` and more...")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")

  @commands.command()
  async def give(self, ctx, member: discord.Member):
    number_coins = db.get(f"{ctx.guild.id}-{ctx.author.id}")
    if number_coins is not None:
      number_coins2 = int(db.get(f"{ctx.guild.id}-{ctx.author.id}"))
      a = ["Premium","premium"]
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      embed = discord.Embed(title="💰 Premium Account", description="Get access to more anime gif commands with exchange your coins\nCost : **1000 🪙**\nTo buy it type : **premium**", color=0xd0c0e9)
      embed.set_thumbnail(url="https://i.ibb.co/F4f5y48/Png-Item-3782851.png")
      await ctx.send(embed=embed)
      rep = await self.bot.wait_for('message', check=check)
      if rep.content in a:
        if number_coins2 >= 1000:
          number_coins2 -= 1000
          del db[f"{ctx.guild.id}-{ctx.author.id}"]
          db[f"{ctx.guild.id}-{ctx.author.id}"] = f"{number_coins2}"
          db[f"Pat-{member.id}"] = "AccesAuthorized"
          await ctx.send(f"Congratulations ! Now {member.mention} have a **Premium Account** !")
        else:
          await ctx.send("You don't have the amount of coins necessary, you can earn coins with `coins`, `fishing` and more...")
    else:
      await ctx.send("You have to create a Bank Account, `bank` to create it")