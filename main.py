# Modules Import
import discord
import discord.utils
import mysql.connector
import time
import help_utils # Import Other Old Files
from nekobot import NekoBotAsync
import admin_utils # Import Other Old Files
import security_utils # Import Other Old Files
import psutil
from io import BytesIO
from random import choice
import gif_utils # Import Other Old Files
import fun_utils # Import Other Old Files
import info_utils # Import Other Old Files
import anime_utils # Import Other Old Files
import economy # Import Other Old Files
import requests
import os
import random, datetime, asyncio, tasks
from discord.ext import commands, ipc
from discord_slash import SlashCommand, ButtonStyle
from discord_slash.utils.manage_components import *
import PIL
from PIL import Image, ImageChops, ImageDraw, ImageFont
import PIL.ImageOps
intents = discord.Intents.default()
intents.members = True

# All Commands with Prefix are not updated and not used at this point
# Ohh and im sorry if my code is not very sort 
# If in the code you see cursor.execute or cursor.fetchone(),... it's to get info from database so replace to your database or remove the part :3

default_prefixes = ':3'

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
      cursor.execute(f"SELECT * FROM `Prefixes` WHERE `ID` = '{message.guild.id}'")
      value4 = cursor.fetchone()
      if value4 is None:
        return default_prefixes
      else:
        cursor.execute(f"SELECT `PREFIX` FROM `Prefixes` WHERE `ID` = '{message.guild.id}'")
        result = cursor.fetchall()
        for row in result:
              pref = row["PREFIX"]
        return pref
    else:
      return default_prefixes

Client = discord.Client()
bot = commands.Bot(command_prefix=determine_prefix, intents=intents) # Prefix Init
slash = SlashCommand(bot, sync_commands=True) # Slash Commmands Init

mydb = mysql.connector.connect(  # Used to connect database
      host="X",
      user="X",
      password="X",
      database="X"
)

cursor = mydb.cursor(dictionary=True) # Define Cursor Variable
print("MySQL Database Connected") # Used by me to see at the launch if Database Connected


# ---------------- Events ---------------- #


# On Guild Join
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        description=
        "Hi, Im Nayo, a Multipurpose Bot based on Anime Theme with a lot's of Fun and Cool Commands... ✿>ω<\n» My default prefix is `/` (Temporarily Slash Commands Only)\n» For the list of commands type `/help`\n» To have more informations about Nayo, visit the Nayo Documentation : https://docs.nayobot.moe\n» Oh and i was going to forget to tell you that Nayo\nis not finished yet so some commands appear sometimes in the\ncommands list, you can be informed about the upcoming\n maintenance and commands on\nthe support server or on the website :3\n» [Website](https://nayobot.moe)\n» [Documentation](https://docs.nayobot.moe)\n» [Support Server](https://discord.gg/UEVn8KchGJ)\n» [Nayo Status](https://status.watchbot.app/bot/879082395750531093)\nHave Fun !",
        color=0xd0c0e9)
    embed.set_author(
        name="Nayo Discord Bot",
        icon_url="https://imgur.com/0SLdaEN.png"
    )
    embed.set_image(url="https://nayobot.moe/hello.png")
    channel = bot.get_channel(904378061221416960)
    if guild.system_channel is not None:
        await guild.system_channel.send(embed=embed)
    else:
        await guild.owner.send(embed=embed)
    await channel.send(f"Nayo added to `{guild.name}`")
   
# On Guild Remove
@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(904378061221416960)
    await channel.send(f"Nayo remove from `{guild.name}`")


# --------------- Welcome Event (Link to /welcome_enable and /welcome_disable) --------------- #
@bot.event
async def on_member_join(member):
      cursor.execute(f"SELECT * FROM `Welcome` WHERE `ID` = '{member.guild.id}'")
      value4 = cursor.fetchone()
      if value4 is not None:
          cursor.execute(f"SELECT `CHANNEL` from `Welcome` where `ID` = '{member.guild.id}'")
          rows2 = cursor.fetchall()
          for row in rows2:
                channel_id = row["CHANNEL"]
          def circle(pfp,size = (215,215)):
            pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
            bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(pfp.size, Image.ANTIALIAS)
            mask = ImageChops.darker(mask, pfp.split()[-1])
            pfp.putalpha(mask)
            return pfp
          name = str(member)
          text = "Welcome :"
          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          pfp = circle(pfp,(215,215))
          base = Image.open("Imgs/BaseWF.png").convert("RGBA")
          draw = ImageDraw.Draw(base)
          font = ImageFont.truetype("Fonts/Discord.ttf", 35)
          font2 = ImageFont.truetype("Fonts/Discord.ttf", 25)
          draw.text((290,140),name,font = font)
          draw.text((290,110),text,font = font2)
          base.paste(pfp,(55,38),pfp)
          base.save("Imgs/welc.png")
          await bot.get_channel(int(channel_id)).send(file = discord.File("Imgs/welc.png"))

# --------------- Farewell Event (Link to /farewell_enable and /farewell_disable) --------------- #
@bot.event
async def on_member_remove(member):
      cursor.execute(f"SELECT * FROM `Farewell` WHERE `ID` = '{member.guild.id}'")
      value4 = cursor.fetchone()
      if value4 is not None:
          cursor.execute(f"SELECT `CHANNEL` from `Farewell` where `ID` = '{member.guild.id}'")
          rows2 = cursor.fetchall()
          for row in rows2:
                channel_id = row["CHANNEL"]
          def circle(pfp,size = (215,215)):
            pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
            bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(pfp.size, Image.ANTIALIAS)
            mask = ImageChops.darker(mask, pfp.split()[-1])
            pfp.putalpha(mask)
            return pfp
          name = str(member)
          text = "Good Bye :"
          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          pfp = circle(pfp,(215,215))
          base = Image.open("Imgs/BaseWF.png").convert("RGBA")
          draw = ImageDraw.Draw(base)
          font = ImageFont.truetype("Fonts/Discord.ttf", 35)
          font2 = ImageFont.truetype("Fonts/Discord.ttf", 25)
          draw.text((290,140),name,font = font)
          draw.text((290,110),text,font = font2)
          base.paste(pfp,(55,38),pfp)
          base.save('Imgs/fare.png')
          await bot.get_channel(int(channel_id)).send(file = discord.File("Imgs/fare.png"))


# ---------------- Genshin Impact Commands ---------------- #


# Search Genshin Impact Characters Informations
@slash.slash(name="genshin_characters", description="Search for Character Info of Genshin Impact 🔍")
async def gic(ctx, character):
  liste = ["albedo","aloy","amber","arataki-itto","ayaka","barbara","beidou","bennett","chongyun","diluc","diona","eula","fischl","ganyu","gorou","hu-tao","jean","kaeya","kazuha","keqing","klee","kokomi","lisa","mona","ningguang","noelle","qiqi","raiden","razor","rosaria","sara","sayu","shenhe","sucrose","tartaglia","thoma","traveler-anemo","traveler-electro","traveler-geo","venti","xiangling","xiao","xingqiu","xinyan","yanfei","yoimiya","yun-jin","zhongli"]
  if character in liste:
    if character == liste[0]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/80/Albedo_carte.jpg/revision/latest?cb=20201224083058&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[1]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity) 
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/e3/Aloy_carte.jpg/revision/latest?cb=20211127202741&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[2]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://kill-the-game.com/wp-content/uploads/2020/09/carte-du-personnage-amber-genshin-impact.jpg")
      await ctx.send(embed=embed)
    if character == liste[3]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://pbs.twimg.com/media/FBaI8AFUcAM1I8g.jpg:large")
      await ctx.send(embed=embed)
    if character == liste[4]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/7/78/Kamisato_Ayaka_carte.jpg/revision/latest?cb=20210615140943&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[5]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/c/c6/Barbara_carte.jpg/revision/latest?cb=20201224083101&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[6]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/3/33/Beidou_carte.jpg/revision/latest?cb=20201224083112&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[7]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/c/c4/Bennett_carte.jpg/revision/latest?cb=20201224083113&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[8]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/85/Chongyun_carte.jpg/revision/latest?cb=20201224083115&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[9]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/0/05/Diluc_carte.jpg/revision/latest?cb=20201224083124&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[10]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/1/1c/Diona_carte.jpg/revision/latest?cb=20201224083125&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[11]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/1/1e/Eula_carte.jpg/revision/latest?cb=20210724114553&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[12]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/84/Fischl_carte.jpg/revision/latest?cb=20201224083126&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[13]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/e7/Ganyu_carte.jpg/revision/latest?cb=20210112200818&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[14]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://conseilsjeuxmobile.com/wp-content/uploads/2021/12/Guide-Genshin-Impact-Gorou-meilleures-armes-artefacts-et-materiaux-requis.jpg")
      await ctx.send(embed=embed)
    if character == liste[15]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/d/d1/Hu_Tao_carte.jpg/revision/latest?cb=20210304101014&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[16]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/2/2e/Jean_carte.jpg/revision/latest?cb=20201224083137&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[17]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/a/a8/Kaeya_carte.jpg/revision/latest?cb=20201224083138&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[18]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/2/28/Kaedehara_Kazuha_carte.jpg/revision/latest?cb=20210615140951&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[19]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/e7/Keqing_carte.jpg/revision/latest?cb=20201224083139&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[20]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/ee/Klee_carte.jpg/revision/latest?cb=20201224083146&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[21]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/ed/Sangonomiya_Kokomi_carte.jpg/revision/latest?cb=20210722173149&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[22]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/7/70/Lisa_carte.jpg/revision/latest/top-crop/width/360/height/450?cb=20201224083154&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[23]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/4/4e/Mona_carte.jpg/revision/latest?cb=20201224083155&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[24]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/7/7a/Ningguang_carte.jpg/revision/latest?cb=20201224083156&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[25]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/e/e6/No%C3%ABlle_carte.jpg/revision/latest?cb=20201224083202&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[26]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/2/24/Qiqi_carte.jpg/revision/latest?cb=20201224083203&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[27]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/a/aa/Shogun_Raiden_carte.jpg/revision/latest/top-crop/width/360/height/450?cb=20210722175218&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[28]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/d/df/Razor_carte.jpg/revision/latest?cb=20201224083205&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[29]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://www.breakflip.com/uploads/60689f518fa2c-Character_Rosaria_Card.png")
      await ctx.send(embed=embed)
    if character == liste[30]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/9/96/Kujou_Sara_carte.jpg/revision/latest?cb=20210722181029&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[31]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/7/7c/Sayu_carte.jpg/revision/latest?cb=20210615151328&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[32]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/82/Shenhe_carte.jpg/revision/latest?cb=20211201181432&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[33]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/6/67/Sucrose_carte.jpg/revision/latest?cb=20201224083216&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[34]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/3/37/Tartaglia_carte.jpg/revision/latest?cb=20201224083217&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[35]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/c/cf/Thomas_carte.jpg/revision/latest?cb=20210908155940&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[36]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      await ctx.send(embed=embed)
    if character == liste[37]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      await ctx.send(embed=embed)
    if character == liste[38]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      await ctx.send(embed=embed)
    if character == liste[39]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/f/f5/Venti_carte.jpg/revision/latest?cb=20201224083218&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[40]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/2/2f/Xiangling_carte.jpg/revision/latest?cb=20201224083224&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[41]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/d/df/Xiao_carte.jpg/revision/latest?cb=20210209115623&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[42]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/0/0f/Xingqiu_carte.jpg/revision/latest?cb=20201224084128&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[43]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://www.breakflip.com/uploads/603a9977caba3-Character_Xinyan_Card.jpg")
      await ctx.send(embed=embed)
    if character == liste[44]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/8f/Yanfei_carte.jpg/revision/latest/top-crop/width/360/height/450?cb=20210724120441&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[45]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/4/41/Yoimiya_carte.jpg/revision/latest?cb=20210615140850&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[46]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/8a/Yun_Jin_carte.jpg/revision/latest?cb=20211201182812&path-prefix=fr")
      await ctx.send(embed=embed)
    if character == liste[47]:
      charact = requests.get(f"https://api.genshin.dev/characters/{character}")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/b/bb/Zhongli_carte.jpg/revision/latest?cb=20201224083250&path-prefix=fr")
      await ctx.send(embed=embed)
  else:
    rs = ["raiden shogun","shogun raiden","shogun","ei"]
    yj = ["yunjin",'Yunjin']
    ai = ["itto","arataki itto","itto arataki","arataki"]
    th = ["thomas","Thomas"]
    liste2 = ["thomas","Thomas","itto","arataki itto","itto arataki","arataki","yunjin",'Yunjin',"raiden shogun","shogun raiden","shogun","ei","albedo","aloy","amber","arataki-itto","ayaka","barbara","beidou","bennett","chongyun","diluc","diona","eula","fischl","ganyu","gorou","hu-tao","jean","kaeya","kazuha","keqing","klee","kokomi","lisa","mona","ningguang","noelle","qiqi","raiden","razor","rosaria","sara","sayu","shenhe","sucrose","tartaglia","thoma","traveler-anemo","traveler-electro","traveler-geo","venti","xiangling","xiao","xingqiu","xinyan","yanfei","yoimiya","yun-jin","zhongli"]
    if character in rs:
      charact = requests.get(f"https://api.genshin.dev/characters/raiden")
      choice = charact.json()
      name = choice['name']
      desc = choice['description']
      vision = choice['vision']
      affiliation = choice['affiliation']
      rarity = choice['rarity']
      conste = choice['constellation']
      birthday = choice['birthday']
      weapon = choice['weapon']
      city = choice['nation']
      embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
      embed.add_field(name="⭐ Rarity",value=rarity)
      embed.add_field(name="👀 Vision",value=vision)
      embed.add_field(name="🔫 Weapon",value=weapon)
      embed.add_field(name="🎂 Birthday",value=birthday)
      embed.add_field(name="📋 Affiliation",value=affiliation)
      embed.add_field(name="✨ Constellation",value=conste)
      embed.add_field(name="📍 Nation",value=city)
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/a/aa/Shogun_Raiden_carte.jpg/revision/latest/top-crop/width/360/height/450?cb=20210722175218&path-prefix=fr")
      await ctx.send(embed=embed)
    if character in yj:
        charact = requests.get(f"https://api.genshin.dev/characters/yun-jin")
        choice = charact.json()
        name = choice['name']
        desc = choice['description']
        vision = choice['vision']
        affiliation = choice['affiliation']
        rarity = choice['rarity']
        conste = choice['constellation']
        birthday = choice['birthday']
        weapon = choice['weapon']
        city = choice['nation']
        embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
        embed.add_field(name="⭐ Rarity",value=rarity)
        embed.add_field(name="👀 Vision",value=vision)
        embed.add_field(name="🔫 Weapon",value=weapon)
        embed.add_field(name="🎂 Birthday",value=birthday)
        embed.add_field(name="📋 Affiliation",value=affiliation)
        embed.add_field(name="✨ Constellation",value=conste)
        embed.add_field(name="📍 Nation",value=city)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/8/8a/Yun_Jin_carte.jpg/revision/latest?cb=20211201182812&path-prefix=fr")
        await ctx.send(embed=embed)
    if character in ai:
          charact = requests.get(f"https://api.genshin.dev/characters/arataki-itto")
          choice = charact.json()
          name = choice['name']
          desc = choice['description']
          vision = choice['vision']
          affiliation = choice['affiliation']
          rarity = choice['rarity']
          conste = choice['constellation']
          birthday = choice['birthday']
          weapon = choice['weapon']
          city = choice['nation']
          embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
          embed.add_field(name="⭐ Rarity",value=rarity)
          embed.add_field(name="👀 Vision",value=vision)
          embed.add_field(name="🔫 Weapon",value=weapon)
          embed.add_field(name="🎂 Birthday",value=birthday)
          embed.add_field(name="📋 Affiliation",value=affiliation)
          embed.add_field(name="✨ Constellation",value=conste)
          embed.add_field(name="📍 Nation",value=city)
          embed.set_thumbnail(url="https://pbs.twimg.com/media/FBaI8AFUcAM1I8g.jpg:large")
          await ctx.send(embed=embed)
    if character in th:
            charact = requests.get(f"https://api.genshin.dev/characters/thoma")
            choice = charact.json()
            name = choice['name']
            desc = choice['description']
            vision = choice['vision']
            affiliation = choice['affiliation']
            rarity = choice['rarity']
            conste = choice['constellation']
            birthday = choice['birthday']
            weapon = choice['weapon']
            city = choice['nation']
            embed = discord.Embed(title=name,description=desc,color=0xd0c0e9)
            embed.add_field(name="⭐ Rarity",value=rarity)
            embed.add_field(name="👀 Vision",value=vision)
            embed.add_field(name="🔫 Weapon",value=weapon)
            embed.add_field(name="🎂 Birthday",value=birthday)
            embed.add_field(name="📋 Affiliation",value=affiliation)
            embed.add_field(name="✨ Constellation",value=conste)
            embed.add_field(name="📍 Nation",value=city)
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/genshinimpact/images/c/cf/Thomas_carte.jpg/revision/latest?cb=20210908155940&path-prefix=fr")
            await ctx.send(embed=embed)
    if character not in liste2:
            await ctx.send("❌ Character Not Found (Please Search with English Character Name)")

# Search Genshin Impact Artifacts Informations
@slash.slash(name="genshin_artifacts", description="Search for Artifacts Info of Genshin Impact 🔍")
async def gia(ctx, artifact_set):
  liste = ["adventurer","archaic-petra","berserker","blizzard-strayer","bloodstained-chivalry","brave-heart","crimson-witch-of-flames","defender-s-will","emblem-of-severed-fate","gambler","glacier-and-snowfield","gladiator-s-finale","heart-of-depth","husk-of-opulent-dreams","instructor","lavawalker","lucky-dog","maiden-beloved","martial-artist","noblesse-oblige","ocean-hued-clam","pale-flame","prayers-for-destiny","prayers-for-illumination","prayers-for-wisdom","prayers-to-springtime","prayers-to-the-firmament","resolution-of-sojourner","retracing-bolide","scholar","shimenawa-s-reminiscence","tenacity-of-the-millelith","the-exile","thundering-fury","thundersoother","tiny-miracle","traveling-doctor","viridescent-venerer","wanderer-s-troupe"]
  if artifact_set in liste:
    arti = requests.get(f"https://api.genshin.dev/artifacts/{artifact_set}")
    choice = arti.json()
    info = choice['name']
    info2 = choice['max_rarity']
    info3 = choice['2-piece_bonus']
    info4 = choice['4-piece_bonus']
    embed = discord.Embed(title=info,color=0xd0c0e9)
    embed.add_field(name="⭐ Max Rarity",value=info2,inline=False)
    embed.add_field(name="2️⃣ 2 Pieces Bonus",value=info3,inline=False)
    embed.add_field(name="4️⃣ 4 Pieces Bonus",value=info4,inline=False)
    embed.set_thumbnail(url="https://www.dexerto.com/wp-content/uploads/2022/01/07/Genshin-Impact-artifact-change-update-2.5.jpg")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❌ Set Not Found (Please Search with English Set Name)")

# Search Genshin Impact Weapons Informations
@slash.slash(name="genshin_weapons", description="Search for Weapons Info of Genshin Impact 🔍")
async def giw(ctx, weapon):
  liste = ["alley-hunter","amber-catalyst","amenoma-kageuchi","amos-bow","apprentice-s-notes","aquila-favonia","beginner-s-protector","black-tassel","blackcliff-amulet","blackcliff-longsword","blackcliff-pole","blackcliff-slasher","blackcliff-warbow","bloodtainted-greatsword","compound-bow","cool-steel","crescent-pike","dark-iron-sword","deathmatch","debate-club","dodoco-tales","dragon-s-bane","dragonspine-spear","dull-blade","ebony-bow","elegy-for-the-end","emerald-orb","engulfing-lightning","everlasting-moonglow","eye-of-perception","favonius-codex","favonius-greatsword","favonius-lance","favonius-sword","favonius-warbow","ferrous-shadow","festering-desire","fillet-blade","freedom-sworn","frostbearer","hakushin-ring","halberd","hamayumi","harbinger-of-dawn","hunter-s-bow","iron-point","iron-sting","katsuragikiri-nagamasa","kitain-cross-spear","lion-s-roar","lithic-blade","lithic-spear","lost-prayer-to-the-sacred-winds","luxurious-sea-lord","magic-guide","mappa-mare","memory-of-dust","messenger","mistsplitter-reforged","mitternachts-waltz","old-merc-s-pal","otherworldly-story","pocket-grimoire","predator","primordial-jade-cutter","primordial-jade-winged-spear","prototype-archaic","prototype-crescent","prototype-grudge","prototype-malice","prototype-rancour","quartz","rainslasher","raven-bow","recurve-bow","royal-bow","royal-greatsword","royal-grimoire","royal-longsword","royal-spear","rust","sacrificial-bow","sacrificial-fragments","sacrificial-greatsword","sacrificial-sword","seasoned-hunter-s-bow","serpent-spine","sharpshooter-s-oath","silver-sword","skyrider-greatsword","skyrider-sword","skyward-atlas","skyward-blade","skyward-harp","skyward-pride","skyward-spine","slingshot","snow-tombed-starsilver","solar-pearl","song-of-broken-pines","staff-of-homa","summit-shaper","sword-of-descension","the-alley-flash","the-bell","the-black-sword","the-catch","the-flute","the-stringless","the-unforged","the-viridescent-hunt","the-widsith","thrilling-tales-of-dragon-slayers","thundering-pulse","traveler-s-handy-sword","twin-nephrite","vortex-vanquisher","waster-greatsword","white-iron-greatsword","white-tassel","whiteblind","windblume-ode","wine-and-song","wolf-s-gravestone"]
  if weapon in liste:
    arti = requests.get(f"https://api.genshin.dev/weapons/{weapon}")
    choice = arti.json()
    info = choice['name']
    info2 = choice['type']
    info3 = choice['rarity']
    info4 = choice['baseAttack']
    info5 = choice['location']
    info6 = choice['subStat']
    embed = discord.Embed(title=info,color=0xd0c0e9)
    embed.add_field(name="⭐ Rarity",value=info3,inline=False)
    embed.add_field(name="🔎 Type",value=info2,inline=False)
    embed.add_field(name="💣 Base Attack",value=info4,inline=False)
    embed.add_field(name="🗺️ Location",value=info5,inline=False)
    embed.add_field(name="📊 Sub Stat",value=info6,inline=False)
    embed.set_thumbnail(url="https://www.unpause.asia/wp-content/uploads/Genshin-Impact-miHoyo-open-world-RPG-role-playing-ps4-pc-ios-android-best-weapons-list-ranked-tiered-1240x698.jpg")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❌ Weapon Not Found (Please Search with English Weapon Name)")


# Old Commands That is put here for the future :

#@slash.slash(name="image_triggered", description="Display a Triggered Poster 🔍")
#async def triggered(ctx, member: discord.Member=None):
    #if member == None:
      #member = ctx.author

    #tri = Image.open("Imgs/Triggered.png")
    #tri2 = tri.resize((1050,230))
    #asset = member.avatar_url
    #data = BytesIO(await asset.read())
    #pfp = Image.open(data)
    #pfp = pfp.resize((1024,1024))
    #pfp.paste(tri2, (0,800))
    #pfp.save("Imgs/triggered2.png")
    #file = discord.File("Imgs/triggered2.png")
    #embed = discord.Embed(description=f"{member.mention} is TRIGGERED 🤯", color=0xd0c0e9)
    #embed.set_image(url="attachment://triggered2.png")
    #embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    #await ctx.send(file=file, embed=embed)       

# Reset Farewell Event (Desactivate it)       
@bot.command()
@commands.has_permissions(manage_messages=True)
async def reset_farewell(ctx):
    cursor.execute(f"SELECT * FROM `Welcome` WHERE `ID` = '{ctx.guild.id}'")
    result = cursor.fectone()
    if result is None:
        await ctx.send("❌ The Welcoming System Is Not Enabled")
    if result is not None:
        await ctx.send("✅ Welcome Message Reset")


# ---------------- Waifu Commands ---------------- #


# Command Not Finished :
    
#@slash.slash(name="slot_machine", description="Play Slot Machine 🎰")
@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def coinss(ctx):
   cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}'")
   value = cursor.fetchone()
   if value is not None:
        cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}'")
        result = cursor.fetchall()
        for num in result:
              number_coins = num["COINS"]
        liste = ["0","1","2","3","4","5","6","7","8","9"]
        liste2 = ["0","1","2","3","4","5","6","7","8","9"]
        liste3 = ["0","1","2","3","4","5","6","7","8","9"]
        choice = random.choice(liste)
        choice2 = random.choice(liste2)
        choice3 = random.choice(liste3)
        if choice == choice2 == choice3:
          coinss = int(number_coins) + 20
          cursor.execute(f"UPDATE `Economy` SET `COINS`='{coinss}' WHERE `ID` = '{ctx.author.id}'")
          mydb.commit()
          embed = discord.Embed(title="Slot Machine 🎰", description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn `20` Cukeni 💴", color=0xd0c0e9)
          embed.set_thumbnail(url="https://i.pinimg.com/originals/5e/91/b2/5e91b2ad35dd6e24387a17ff96f35599.jpg")
          await ctx.send(embed=embed)
        else:
          if choice == choice2 or choice == choice3 or choice2 == choice3:
            coinss = int(number_coins) + 7
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{coinss}' WHERE `ID` = '{ctx.author.id}'")
            mydb.commit()
            embed = discord.Embed(title="Slot Machine 🎰", description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn `7` Cukeni 💴", color=0xd0c0e9)
            embed.set_thumbnail(url="https://i.pinimg.com/originals/5e/91/b2/5e91b2ad35dd6e24387a17ff96f35599.jpg")
            await ctx.send(embed=embed)
          else:
            coinss = int(number_coins) + 2
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{coinss}' WHERE `ID` = '{ctx.author.id}'")
            mydb.commit()
            embed3 = discord.Embed(title="Slot Machine 🎰",     description=f"Result  :  **{choice} {choice2} {choice3}**\nYou earn `2` Cukeni 💴", color=0xd0c0e9)
            embed3.set_thumbnail(url="https://i.pinimg.com/originals/5e/91/b2/5e91b2ad35dd6e24387a17ff96f35599.jpg")
            await ctx.send(embed=embed3)
        
@coinss.error
async def coinss_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(description="Next Game <t:{}:R>".format(int(time.time() + error.retry_after)), color=0xd0c0e9)
        await ctx.send(embed=embed)
    else:
        raise error

# Command Not Finished :

#@slash.slash(name="bank", description="Create a Nayo Bank Account 🏦")
@bot.command()
async def bankk(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is not None:
        embed2 = discord.Embed(description=f"❌ Bank Account Already Exist {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is None:
        cursor.execute(f"INSERT INTO `Economy`(`ID`, `COINS`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `EconomyGem`(`ID`, `GEMS`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu2`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu3`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu4.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu5.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        cursor.execute(f"INSERT INTO `Waifu6.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
        mydb.commit()
        embed = discord.Embed(description=f"🏦 Bank Account Created {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed)

# Command Not Finished :

#@slash.slash(name="wallet", description="Display your Bank Wallet 👛")
@bot.command()
async def wallett(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
        cursor.execute(f"SELECT `COINS` from `Economy` where `ID` = '{ctx.author.id}{ctx.guild.id}'")
        rows = cursor.fetchall()
        for row in rows:
            val = row["COINS"]
        cursor.execute(f"SELECT `GEMS` from `EconomyGem` where `ID` = '{ctx.author.id}{ctx.guild.id}'")
        rows2 = cursor.fetchall()
        for row2 in rows2:
            val2 = row2["GEMS"]
        embed = discord.Embed(title="💰 Wallet", description=f"💴 Cukeni Amount : `{val}`\n💎 Gems Amount : `{val2}`", color=0xd0c0e9)
        await ctx.send(embed=embed)
        
# Command Not Finished :

#@slash.slash(name="bank_delete", description="Delete your Bank Account 💸")
@bot.command()
async def delete_account(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
        cursor.execute(f"DELETE FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu2` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu4.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu5.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        cursor.execute(f"DELETE FROM `Waifu6.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        mydb.commit()
        embed = discord.Embed(description=f"🏦 Bank Account Deleted {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed)

# Command Not Finished :

#@slash.slash(name="waifu", description="Roll a random Waifu and get random amount of Cukeni 💴")
@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def waifu(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
        waifu = requests.get("https://api.waifu.im/random")
        choice = waifu.json()
        img = choice['images'][0]['url']
        walist = ["Rikini Yoritsugu","Miki Munetsuna","Agatsuka Ennorobei","Hashida Shadasu","Okataki Nobutora","Takasuchi Norikio","Azube Shatsuzan","Isesano Montamoru","Osashima Kyukoji","Yumine Gegawa","Fuwari Mihomiju","Kagagita Rurikari","Okiken Chihomi","Kiribaru Fuminuye","Yoshiya Umenomi","Iwamano Hohori","Tatsurano Nikari","Sasu Kiyoko","Yasubi Nokemi","Inamachi Sawatomi","Oshiziwa Asuno","Masaga Kasume","Haritsami Tsumeko","Ohataka Suzumachi","Yamawara Itori","Horikono Sayokura","Mosu Irari","Marukawa Rukeno","Wawa Asarime","Wanaba Haniwara","Okisho Kukino","Motosato Aho","Wayama Ureniko","Hagishita Ayayumi","Tatenagi Kiyokumi","Fuchimaru Kasuchiko","Dosano Kuho","Hokura Kochisu","Okubashi Mitsumachi","Arakita Maritsuki","Kodakuro Raruri","Tahabashi Haiyoko","Suzukawa Tene","Konishige Yumichiko","Kobakura Tanirari","Kurikite Asatori","Yadashima Umeko","Mogai Honami","Isosho Itsuyumi","Sakazato Kiyomiko"]
        coinslist = ["8","5","2","10","9","14","13","7","11"]
        wa = random.choice(walist)
        coin = random.choice(coinslist)
        cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
        result = cursor.fetchall()
        for row in result:
            total = row["COINS"]
        to = int(total) + int(coin)
        value = random.randrange(101)
        if value < 10:
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
                tota = rows["GEMS"]
                tot = int(tota) + 10
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{to}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{tot}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            embed = discord.Embed(title=wa, description=f"You meet `{wa}`\nShe give you `{coin}` Cukeni 💴\nBonus + `10` Gems 💎", color=0xd0c0e9)
            embed.set_image(url=img)
            await ctx.send(embed=embed)
        else:
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{to}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            embed2 = discord.Embed(title=wa, description=f"You meet `{wa}`\nShe give you `{coin}` Cukeni 💴", color=0xd0c0e9)
            embed2.set_image(url=img)
            await ctx.send(embed=embed2)

# Command Not Finished :          
            
#@slash.slash(name="waifu_collection", description="See your Waifu ✿>ω<")
@bot.command()
async def collection(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
      cursor.execute(f"SELECT * FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
      results2 = cursor.fetchone()
      if results2 is None:
                    cursor.execute(f"INSERT INTO `Waifu3`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
                    mydb.commit()
                    cursor.execute(f"INSERT INTO `Waifu4.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
                    mydb.commit()
                    cursor.execute(f"INSERT INTO `Waifu5.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
                    mydb.commit()
                    cursor.execute(f"INSERT INTO `Waifu6.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','0')")
                    mydb.commit()
                    def circle(pfp,size = (215,215)):
                             pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
                             bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
                             mask = Image.new('L', bigsize, 0)
                             draw = ImageDraw.Draw(mask) 
                             draw.ellipse((0, 0) + bigsize, fill=255)
                             mask = mask.resize(pfp.size, Image.ANTIALIAS)
                             mask = ImageChops.darker(mask, pfp.split()[-1])
                             pfp.putalpha(mask)
                             return pfp
                    author = ctx.author
                    text = "Waifu Shop"
                    pfp = author.avatar_url_as(size=256)
                    data = BytesIO(await pfp.read())
                    pfp = Image.open(data).convert("RGBA")
                    pfp = circle(pfp,(380,380))
                    base = Image.open("Imgs/shop_blur.png").convert("RGBA")
                    draw = ImageDraw.Draw(base)
                    base.paste(pfp,(70,385),pfp)
                    font = ImageFont.truetype("Fonts/Discord.ttf", 35)
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result1 = cursor.fetchall()
                    for row1 in result1:
                      number1 = row1["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu2` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result2 = cursor.fetchall()
                    for row2 in result2:
                      number2 = row2["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result3 = cursor.fetchall()
                    for row3 in result3:
                      number3 = row3["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu4.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result4 = cursor.fetchall()
                    for row4 in result4:
                      number4 = row4["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu5.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result5 = cursor.fetchall()
                    for row5 in result5:
                      number5 = row5["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu6.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result6 = cursor.fetchall()
                    for row6 in result6:
                      number6 = row6["NUMBER"]
                    draw.text((700,245),number1,font = font, fill="pink")
                    draw.text((1200, 245), number2, font=font, fill="pink")
                    draw.text((1700, 245), number3, font=font, fill="pink")
                    draw.text((700, 770), number4, font=font, fill="pink")
                    draw.text((1200, 770), number5, font=font, fill="pink")
                    draw.text((1700, 770), number6, font=font, fill="pink")
                    base.save("Imgs/membershop.png")
                    file = discord.File("Imgs/membershop.png")
                    embed = discord.Embed(description=f"Waifu Collection of {ctx.author.mention} 🃏", color=0xd0c0e9)
                    embed.set_image(url="attachment://Imgs/membershop.png")
                    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
                    await ctx.send(file=file, embed=embed)
      if results2 is not None:
                    def circle(pfp,size = (215,215)):
                             pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
                             bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
                             mask = Image.new('L', bigsize, 0)
                             draw = ImageDraw.Draw(mask) 
                             draw.ellipse((0, 0) + bigsize, fill=255)
                             mask = mask.resize(pfp.size, Image.ANTIALIAS)
                             mask = ImageChops.darker(mask, pfp.split()[-1])
                             pfp.putalpha(mask)
                             return pfp
                    author = ctx.author
                    text = "Waifu Shop"
                    pfp = author.avatar_url_as(size=256)
                    data = BytesIO(await pfp.read())
                    pfp = Image.open(data).convert("RGBA")
                    pfp = circle(pfp,(380,380))
                    base = Image.open("Imgs/shop_blur.png").convert("RGBA")
                    draw = ImageDraw.Draw(base)
                    base.paste(pfp,(70,385),pfp)
                    font = ImageFont.truetype("Fonts/Discord.ttf", 100)
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result1 = cursor.fetchall()
                    for row1 in result1:
                      number1 = row1["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu2` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result2 = cursor.fetchall()
                    for row2 in result2:
                      number2 = row2["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result3 = cursor.fetchall()
                    for row3 in result3:
                      number3 = row3["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu4.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result4 = cursor.fetchall()
                    for row4 in result4:
                      number4 = row4["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu5.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result5 = cursor.fetchall()
                    for row5 in result5:
                      number5 = row5["NUMBER"]
                    cursor.execute(f"SELECT `NUMBER` FROM `Waifu6.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                    result6 = cursor.fetchall()
                    for row6 in result6:
                      number6 = row6["NUMBER"]
                    draw.text((700,245),number1,font = font, fill="pink")
                    draw.text((1200, 245), number2, font=font, fill="pink")
                    draw.text((1700, 245), number3, font=font, fill="pink")
                    draw.text((700, 770), number4, font=font, fill="pink")
                    draw.text((1200, 770), number5, font=font, fill="pink")
                    draw.text((1700, 770), number6, font=font, fill="pink")
                    base.save("Imgs/membershop.png")
                    file = discord.File("Imgs/membershop.png")
                    embed = discord.Embed(description=f"Waifu Collection of {ctx.author.mention} 🃏", color=0xd0c0e9)
                    embed.set_image(url="attachment://Imgs/membershop.png")
                    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
                    await ctx.send(file=file, embed=embed)

# Command Not Finished :

#@slash.slash(name="waifu_all", description="Discover the Waifu Available ✿>ω<")
@bot.command()
async def all(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
                    def circle(pfp,size = (215,215)):
                             pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
                             bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
                             mask = Image.new('L', bigsize, 0)
                             draw = ImageDraw.Draw(mask) 
                             draw.ellipse((0, 0) + bigsize, fill=255)
                             mask = mask.resize(pfp.size, Image.ANTIALIAS)
                             mask = ImageChops.darker(mask, pfp.split()[-1])
                             pfp.putalpha(mask)
                             return pfp
                    author = ctx.author
                    text = "Waifu Shop"
                    pfp = author.avatar_url_as(size=256)
                    data = BytesIO(await pfp.read())
                    pfp = Image.open(data).convert("RGBA")
                    pfp = circle(pfp,(380,380))
                    base = Image.open("Imgs/shop.png").convert("RGBA")
                    draw = ImageDraw.Draw(base)
                    base.paste(pfp,(70,385),pfp)
                    base.save("Imgs/membershop.png")
                    file = discord.File("Imgs/membershop.png")
                    embed = discord.Embed(description=f"All The Waifu Available", color=0xd0c0e9)
                    embed.set_image(url="attachment://Imgs/membershop.png")
                    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
                    await ctx.send(file=file, embed=embed)

# Command Not Finished :

#@slash.slash(name="waifu_give", description="Give Cukeni to Members ✿>ω<")
@bot.command()
async def givec(ctx, member: discord.Member, amount):
  cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{member.id}{ctx.guild.id}'")
  results = cursor.fetchone()
  if results is None:
    embed2 = discord.Embed(description=f"❌ {member.mention} Doesn't have a Bank Account {ctx.author.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed2)
  if results is not None:
    amount2 = int(amount)
    if amount2 < 1:
      await ctx.send('<:Fumino:974383095665016924> You can\'t give negative amount')
    else:
      cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{member.id}{ctx.guild.id}'")
      result = cursor.fetchall()
      for rows in result:
        total1 = rows["COINS"]
        total2 = int(total1) + amount2
      cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{member.id}{ctx.guild.id}'")
      mydb.commit()
      await ctx.send(f'<:raiden:976892921158729768> Cukeni Amount Added to {member.mention}')

# Command Not Finished :

#@slash.slash(name="waifu_shop", description="Buy Waifu and Collect Them ✿>ω<")
@bot.command()
async def buy(ctx):
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
    results = cursor.fetchone()
    if results is None:
        embed2 = discord.Embed(description=f"❌ Bank Account Not Found {ctx.author.mention}", color=0xd0c0e9)
        await ctx.send(embed=embed2)
    if results is not None:
        embed = discord.Embed(title="Waifu Shop 🛒", description="To buy a Waifu send the name of the Waifu after this message\nThe Waifu will be added automatically to your collection ;3\nThis week : `Bonus + 2 Gems 💎 per Waifu`", color=0xd0c0e9)
        embed.add_field(name="<:AmeriInako:975336275953467392> Ameri Inako", value="Cost : `1000` Cukeni 💴")
        embed.add_field(name="<:InazakiAisago:975335472786186260> Inazaki Aisago", value="Cost : `950` Cukeni 💴")
        embed.add_field(name="<:MizutsukiNineko:975335426774683688> Mizutsuki Nineko", value="Cost : `600` Cukeni 💴")
        embed.add_field(name="<:NishidaMameko:975336308576768060> Nishida Mameko", value="Cost : `500` Cukeni 💴")
        embed.add_field(name="<:HigameHarahira:975335451462340608> Higame Harahira", value="Cost : `400` Cukeni 💴")
        embed.add_field(name="<:TatsunagiMarehi:975336288691580981> Tatsunagi Marehi", value="Cost : `300` Cukeni 💴")
        embed.set_footer(text=f"{ctx.author.name}")
        await ctx.send(embed=embed)
        a = ["Ameri Inako","ameri inako","ameri","Ameri","inako","Inako"]
        b = ["Inazaki Aisago","inazaki aisago","inazaki","Inazaki","Aisago","aisago"]
        c = ["Mizutsuki Nineko","mizutsuki nineko","mizutsuki","Mizutsuki","Nineko","nineko"]
        d = ["Nishida Maneko","nishida maneko","nishida","Nishida","maneko","Maneko"]
        e = ["Higame Harahira","higame harahira","higame","Higame","harahira","Harahira"]
        f = ["Tatsunagi Marehi","tatsunagi marehi","tatsunagi","Tatsunagi","Marehi","marehi"]
        g = ["Ameri Inako","ameri inako","ameri","Ameri","inako","Inako","Inazaki Aisago","inazaki aisago","inazaki","Inazaki","Aisago","aisago","Mizutsuki Nineko","mizutsuki nineko","mizutsuki","Mizutsuki","Nineko","nineko","Nishida Maneko","nishida maneko","nishida","Nishida","maneko","Maneko","Higame Harahira","higame harahira","higame","Higame","harahira","Harahira","Tatsunagi Marehi","tatsunagi marehi","tatsunagi","Tatsunagi","Marehi","marehi"]
        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel
        message = await bot.wait_for('message', check=check)
        if message.content not in g:
            await ctx.send('<:Fumino:974383095665016924> Your Waifu  isn\'t on the Shop')
        if message.content in a:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
                tota = rows["COINS"]
                tot = int(tota)
            if tot >= 1000:
              cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resulttt = cursor.fetchall()
              for rowss in resulttt:
                total1 = rowss["COINS"]
                total2 = int(total1) - 1000
              cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultt = cursor.fetchall()
              for rows in resultt:
                total3 = rows["GEMS"]
                total4 = int(total3) + 2
              cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu5.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchone()
              if resultttt is not None:
                cursor.execute(f"SELECT `NUMBER` FROM `Waifu5.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                resultttt = cursor.fetchall()
                for rowsss in resultttt:
                  total5 = rowsss["NUMBER"]
                  total6 = int(total5) + 1
                cursor.execute(f"UPDATE `Waifu5.1` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
                mydb.commit()
                await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
              if resultttt is None:
                cursor.execute(f"INSERT INTO `Waifu5.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
                mydb.commit()
                await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            else:
              await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        if message.content in b:
          cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
          resultt = cursor.fetchall()
          for rows in resultt:
            tota = rows["COINS"]
            tot = int(tota)
          if tot >= 950:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resulttt = cursor.fetchall()
            for rowss in resulttt:
              total1 = rowss["COINS"]
              total2 = int(total1) - 950
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
              total3 = rows["GEMS"]
              total4 = int(total3) + 2
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `NUMBER` FROM `Waifu6.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultttt = cursor.fetchone()
            if resultttt is not None:
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu6.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchall()
              for rowsss in resultttt:
                total5 = rowsss["NUMBER"]
                total6 = int(total5) + 1
              cursor.execute(f"UPDATE `Waifu6.1` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            if resultttt is None:
              cursor.execute(f"INSERT INTO `Waifu6.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
          else:
            await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        if message.content in c:
          cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
          resultt = cursor.fetchall()
          for rows in resultt:
            tota = rows["COINS"]
            tot = int(tota)
          if tot >= 600:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resulttt = cursor.fetchall()
            for rowss in resulttt:
              total1 = rowss["COINS"]
              total2 = int(total1) - 600
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
              total3 = rows["GEMS"]
              total4 = int(total3) + 2
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `NUMBER` FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultttt = cursor.fetchone()
            if resultttt is not None:
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu3` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchall()
              for rowsss in resultttt:
                total5 = rowsss["NUMBER"]
                total6 = int(total5) + 1
              cursor.execute(f"UPDATE `Waifu3` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            if resultttt is None:
              cursor.execute(f"INSERT INTO `Waifu3`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
          else:
            await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        if message.content in d:
          cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
          resultt = cursor.fetchall()
          for rows in resultt:
            tota = rows["COINS"]
            tot = int(tota)
          if tot >= 500:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resulttt = cursor.fetchall()
            for rowss in resulttt:
              total1 = rowss["COINS"]
              total2 = int(total1) - 500
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
              total3 = rows["GEMS"]
              total4 = int(total3) + 2
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `NUMBER` FROM `Waifu4.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultttt = cursor.fetchone()
            if resultttt is not None:
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu4.1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchall()
              for rowsss in resultttt:
                total5 = rowsss["NUMBER"]
                total6 = int(total5) + 1
              cursor.execute(f"UPDATE `Waifu4.1` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            if resultttt is None:
              cursor.execute(f"INSERT INTO `Waifu4.1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
          else:
            await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        if message.content in e:
          cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
          resultt = cursor.fetchall()
          for rows in resultt:
            tota = rows["COINS"]
            tot = int(tota)
          if tot >= 400:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resulttt = cursor.fetchall()
            for rowss in resulttt:
              total1 = rowss["COINS"]
              total2 = int(total1) - 400
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
              total3 = rows["GEMS"]
              total4 = int(total3) + 2
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `NUMBER` FROM `Waifu2` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultttt = cursor.fetchone()
            if resultttt is not None:
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu2` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchall()
              for rowsss in resultttt:
                total5 = rowsss["NUMBER"]
                total6 = int(total5) + 1
              cursor.execute(f"UPDATE `Waifu2` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            if resultttt is None:
              cursor.execute(f"INSERT INTO `Waifu2`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
          else:
            await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        if message.content in f:
          cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
          resultt = cursor.fetchall()
          for rows in resultt:
            tota = rows["COINS"]
            tot = int(tota)
          if tot >= 300:
            cursor.execute(f"SELECT `COINS` FROM `Economy` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resulttt = cursor.fetchall()
            for rowss in resulttt:
              total1 = rowss["COINS"]
              total2 = int(total1) - 300
            cursor.execute(f"UPDATE `Economy` SET `COINS`='{total2}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `GEMS` FROM `EconomyGem` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultt = cursor.fetchall()
            for rows in resultt:
              total3 = rows["GEMS"]
              total4 = int(total3) + 2
            cursor.execute(f"UPDATE `EconomyGem` SET `GEMS`='{total4}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            mydb.commit()
            cursor.execute(f"SELECT `NUMBER` FROM `Waifu1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
            resultttt = cursor.fetchone()
            if resultttt is not None:
              cursor.execute(f"SELECT `NUMBER` FROM `Waifu1` WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              resultttt = cursor.fetchall()
              for rowsss in resultttt:
                total5 = rowsss["NUMBER"]
                total6 = int(total5) + 1
              cursor.execute(f"UPDATE `Waifu1` SET `NUMBER`='{total6}' WHERE `ID` = '{ctx.author.id}{ctx.guild.id}'")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
            if resultttt is None:
              cursor.execute(f"INSERT INTO `Waifu1`(`ID`, `NUMBER`) VALUES ('{ctx.author.id}{ctx.guild.id}','1')")
              mydb.commit()
              await ctx.send("<:raiden:976892921158729768> Successful Transaction !")
          else:
            await ctx.send(f"<:NagatoroSteal:974383095992168458> Are you seriously trying to steal Waifu ?")
        
@waifu.error
async def waifu_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(description="Next Waifu <t:{}:R> ✿>ω<".format(int(time.time() + error.retry_after)), color=0xd0c0e9)
        await ctx.send(embed=embed)
    else:
        raise error

# Old Command :

@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_guild=True)
async def setprefix(ctx, prefixe):
  a = ["@","@here","@everyone"]
  if prefixe in a:
    await ctx.send("❌ Mentions Are Not Allowed")
  else:
    if len(prefixe) > 5:
        await ctx.send("❌ Please Enter a Shorter Prefix")
    else:
        cursor.execute(f"SELECT * FROM `Prefixes` WHERE `ID` = '{ctx.guild.id}'")
        value4 = cursor.fetchone()
        if value4 is None:
            cursor.execute(f"INSERT INTO `Prefixes`(`ID`, `PREFIX`) VALUES ('{ctx.guild.id}','{prefixe}')")
            mydb.commit()
            embed = discord.Embed(title="✅ Prefix Set Successfully", description=f"New prefix : `{prefixe}`\n(Effective only on this server)", color=0xd0c0e9)
            embed.set_thumbnail(url="https://c.tenor.com/tLl0Bru9EdwAAAAC/thumbs-up-good-job.gif")
            await ctx.send(embed=embed)
        else:
            cursor.execute(f"UPDATE `Prefixes` SET `PREFIX`='{prefixe}' WHERE `ID` = {ctx.guild.id}")
            mydb.commit()
            embed2 = discord.Embed(title="✅ Prefix Set Successfully", description=f"New prefix : `{prefixe}`\n(Effective only on this server)", color=0xd0c0e9)
            embed2.set_thumbnail(url="https://c.tenor.com/tLl0Bru9EdwAAAAC/thumbs-up-good-job.gif")
            await ctx.send(embed=embed2)

		
# ---------------- Admin and Modo Commands ---------------- #

@slash.slash(name="lock", description="Lock a Channel 🔒")
async def lock(ctx, channel: discord.TextChannel=None):
  if ctx.author.guild_permissions.manage_channels:
    channel = channel or ctx.channel
    embed = discord.Embed(title=f"{channel} Locked 🔒", description="Use /unlock to make it public", color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="category", description="Create a category 🖊️")
async def category(ctx, category_name):
  if ctx.author.guild_permissions.manage_channels:
    guild = ctx.guild
    await ctx.guild.create_category(category_name)
    embed = discord.Embed(title="Category Created", description = f"**Name** : {category_name}", color = 0xd0c0e9)
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="warn", description="Warn a member ⚠️")
async def warn(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_guild:
        val = f"{member.id}-{ctx.guild.id}"
        cursor.execute(f"SELECT * FROM `Warn` WHERE `ID` = '{val}'")
        value = cursor.fetchone()
        if value is not None:
            cursor.execute(f"SELECT `WARNS` FROM `Warn` WHERE `ID` = '{val}'")
            result = cursor.fetchall()
            for rows in result:
                res = rows["WARNS"]
            tot = int(res) + 1
            cursor.execute(f"UPDATE `Warn` SET `WARNS`='{tot}' WHERE `ID` = '{val}'")
            mydb.commit()
            embed = discord.Embed(title="Member Warn 🔨", description=f"{member.mention} has been warn\nHe receive a warn private message", color=0xd0c0e9)
            embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(title=f"{ctx.guild.name} Warn ⚠️", description=f"You receive a warn from **{ctx.guild.name}**\nFor a bad attitude in this server\nPlease keep a good behavior !", color=0xd0c0e9)
            embed2.set_thumbnail(url="https://i.ibb.co/HYhhSPf/Warning-PNG-Free-Image.png")
            await member.send(embed=embed2)
        if value is None:
            cursor.execute(f"INSERT INTO `Warn`(`ID`, `WARNS`) VALUES ('{val}','1')")
            mydb.commit()
            embed = discord.Embed(title="Member Warn 🔨", description=f"{member.mention} has been warn\nHe receive a warn private message", color=0xd0c0e9)
            embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(title=f"{ctx.guild.name} Warn ⚠️", description=f"You receive a warn from **{ctx.guild.name}**\nFor a bad attitude in this server\nPlease keep a good behavior !", color=0xd0c0e9)
            embed2.set_thumbnail(url="https://i.ibb.co/HYhhSPf/Warning-PNG-Free-Image.png")
            await member.send(embed=embed2)
    else:
        await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="nickname", description="Set a nickname of change it 🔁")
async def nickname(ctx, member: discord.Member, *, nick):
  if ctx.author.guild_permissions.manage_nicknames:
    await member.edit(nick=nick)
    embed = discord.Embed(title="🔁 Changed Nickname", description=f'New Nickname for : {member.mention}', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="roles_create", description="Create a custom role 🎭")
async def role(ctx, *, role_name):
  if ctx.author.guild_permissions.manage_guild:
    guild = ctx.guild
    await guild.create_role(name=f"{role_name}")
    embed = discord.Embed(title="Created Role", description=f'Role : **{role_name}**', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="roles_delete", description="Delete a specified role 🎭")
async def deleterole(ctx, role_name):
  if ctx.author.guild_permissions.manage_guild:
    role = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role.delete()
    embed = discord.Embed(title="Delete Role", description=f'Role : **{role_name}**', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="roles_display", description="Display the roles of the server 🎭")
async def showroles(ctx):
  if ctx.author.guild_permissions.manage_guild:
    guild = ctx.guild
    roles = [role for role in guild.roles if role != ctx.guild.default_role]
    roles = roles[::-1]
    embed = discord.Embed(title=f"📝 Roles of {ctx.guild.name}", description=f" ".join([role.mention + '\n' for role in roles]), color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/kaRCm9ELxKgAAAAC/menhera-chan-chibi.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="channel_text", description="Create a voice channel with a custom name 🔊")
async def textchannel(ctx, *, channel_name):
  if ctx.author.guild_permissions.manage_channels:
    guild = ctx.guild
    await guild.create_text_channel(channel_name)
    embed = discord.Embed(title="Textual Channel Created", description = f"**Name** : {channel_name}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="channel_voice", description="Create a voice channel with a custom name 🔊")
async def voicechannel(ctx, *, channel_name):
  if ctx.author.guild_permissions.manage_channels:
    guild = ctx.guild
    await guild.create_voice_channel(channel_name)
    embed = discord.Embed(title="Voice Channel Created", description = f"**Name** : {channel_name}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="unmute", description="Unmute a Member 🔊")
async def unmute(ctx, member: discord.Member, *, reason="No Reason"):
  if ctx.author.guild_permissions.manage_guild:
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role, reason=reason)
    embed = discord.Embed(title="Member Unmute  ⚖️",
                          description=f"Member : {member.mention}",
                          color=0xd0c0e9)
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="mute", description="Mute a Member 🔇")
async def mute(ctx, member: discord.Member, reason="No Reason"):
  if ctx.author.guild_permissions.manage_guild:
    if discord.utils.get(ctx.guild.roles, name="Muted"):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        embed = discord.Embed(title="Member Muted  ⚖️",
                              description=f"Member : {member.mention}",
                              color=0xd0c0e9)
        await ctx.send(embed=embed)
    else:
        await ctx.guild.create_role(name="Muted")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        embed = discord.Embed(title="Member Muted  ⚖️",
                              description=f"Member : {member.mention}",
                              color=0xd0c0e9)
        await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="category_delete", description="Delete a category 🗑️")
async def delcategory(ctx, category: discord.CategoryChannel):
  if ctx.author.guild_permissions.manage_guild:
    delcategory = category
    channels = delcategory.channels

    for channel in channels:
        try:
            await channel.delete()
        except AttributeError:
            pass
    await delcategory.delete()
    embed = discord.Embed(title="Category Deleted", description = f"**Name** : {category}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="warnings_list", description="Display the warns or a member ⚠️")
async def warnlist(ctx, member: discord.Member):
  val = f"{member.id}-{ctx.guild.id}"
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Warn` WHERE `ID` = '{val}'")
    value = cursor.fetchone()
    if value is not None:
      cursor.execute(f"SELECT `WARNS` FROM `Warn` WHERE `ID` = '{val}'")
      result = cursor.fetchall()
      for rows in result:
             res = rows["WARNS"]
      tot = int(res)
      embed = discord.Embed(title=f"{ctx.guild.name} Warns 📋", description=f"{member.mention} has actually `{tot}` warn(s)", color=0xd0c0e9)
      await ctx.send(embed=embed)
    if value is None:
      await ctx.send(f"{member.mention} don't have any warn actually")
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="warnings_clear", description="Reset the warns of a member ⚠️")
async def resetwarnings(ctx, member: discord.Member):
  val = f"{member.id}-{ctx.guild.id}"
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Warn` WHERE `ID` = '{val}'")
    value = cursor.fetchone()
    if value is not None:
      cursor.execute(f"DELETE FROM `Warn` WHERE `ID` = '{val}'")
      mydb.commit()
      await ctx.send(f"The warnings of {member.mention} have been reset")
    else:
      await ctx.send(f"{member.name} don't have warns actually")
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="channel_delete", description="Delete a channel 🗑️")
async def deletechannel(ctx, channel: discord.TextChannel):
  if ctx.author.guild_permissions.manage_channels:
    guild = ctx.guild
    if not channel:
      await ctx.send(f"{channel} don't exist")
    else:
      await channel.delete()
      embed = discord.Embed(title="Channel Deleted", description = f"**Name** : {channel}", color = 0xd0c0e9)
      embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
      await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="clearall", description="Delete all the messages on the channel 🗑️")
async def clearall(ctx):
  if ctx.author.guild_permissions.manage_messages:
    messages = await ctx.channel.history().flatten()
    for message in messages:
        await message.delete()
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="clear", description="Delete a amount of messages on the channel 🗑️")
async def clear(ctx, number: int):
  if ctx.author.guild_permissions.manage_messages:
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for message in messages:
      await message.delete()
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="logs", description="Create a channel and send on it who use a Nayo Command 📦")
async def logs(ctx):
  if ctx.author.guild_permissions.manage_messages:
    guild = ctx.guild
    channel = discord.utils.get(guild.text_channels, name='📦・nayo-logs')
    if channel is None:
      overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        guild.me: discord.PermissionOverwrite(view_channel=False)
      }
      await guild.create_text_channel("📦・nayo-logs", overwrites=overwrites)
    else:
      await ctx.send("#📦・nayo-logs already exists")
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="unlock", description="Unlock a channel locked 🔓")
async def unlock(ctx, channel: discord.TextChannel=None):
  if ctx.author.guild_permissions.manage_channels:
    channel = channel or ctx.channel
    embed = discord.Embed(title=f"{channel} Unlocked 🔓", description="Use /lock to make it private", color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="kick", description="Kick a member 👉")
async def kick(ctx, user: discord.User, *reason):
  if ctx.author.guild_permissions.kick_members:    
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="Member Kick 🔨", description=f"Member : {user.mention}\nReason : {reason}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="slowmode", description="Enable Slow Mode 🛌")
async def slowmode(ctx, time: int):
  if ctx.author.guild_permissions.manage_channels:
    await ctx.channel.edit(slowmode_delay=time)
    await ctx.send(
        f"Slow mode activated for this channel, delay : **{time}** seconds\nTo desactivate slowmode use `/slowmode_stop`"
    )
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="slowmode_stop", description="Stop Slow Mode 🛑")
async def stopsm(ctx):
  if ctx.author.guild_permissions.ban_members:
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send(f"Slow Mode Disabled")
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="ban", description="Ban a member 🔨")
async def ban(ctx, member: discord.Member, *, reason="No Reason"):
  if ctx.author.guild_permissions.ban_members:
    reason = " ".join(reason)
    await ctx.guild.ban(member, reason=reason)
    embed = discord.Embed(title="Member Ban 🔨", description=f"Member : {member.mention}\nReason : {reason}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="purge", description="Purge a channel ♻️")
async def purgee(ctx):
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send("Channel Purging...")
    await ctx.channel.purge(limit=10000)
    embed = discord.Embed(title=f"{ctx.channel.name} Purged Successfully", description=f"Carried-out by {ctx.author.name}\nThis message is deleted in 10 seconds", color=0xd0c0e9)
    embed.set_thumbnail(url="https://i.ibb.co/f1DKR81/clipart1795386.png")
    await ctx.send(embed=embed, delete_after=10)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="", description="Clone a channel 👥")
async def clone(ctx, channel: discord.TextChannel):
  if ctx.author.guild_permissions.manage_channels:
    guild = ctx.guild
    await guild.create_text_channel(channel)

@slash.slash(name="welcome_enable", description="Set a welcome image for new members 👋")
async def welcome_enable(ctx, channel: discord.TextChannel):
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Welcome` WHERE `ID` = '{ctx.guild.id}'")
    value = cursor.fetchone()
    if value is None:
        cursor.execute(f"INSERT INTO `Welcome`(`ID`, `CHANNEL`) VALUES ('{ctx.guild.id}','{channel.id}')")
        mydb.commit()
        embed = discord.Embed(title="Welcome Image Set 📷", description="The welcoming system is enabled\nUse /welcome_disable to disable it", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)
    if value is not None:
        await ctx.send("❌ Farewell System Already Activated")
  else:
      await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="farewell_enable", description="Set a farewell image for members who left 👋")
async def farewell_enable(ctx, channel: discord.TextChannel):
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Farewell` WHERE `ID` = '{ctx.guild.id}'")
    value = cursor.fetchone()
    if value is None:
        cursor.execute(f"INSERT INTO `Farewell`(`ID`, `CHANNEL`) VALUES ('{ctx.guild.id}', '{channel.id}')")
        mydb.commit()
        embed = discord.Embed(title="Farewell Image Set 📷", description="The farewelling system is enabled\nUse /farewell_disable to disable it", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)
    if value is not None:
        await ctx.send("❌ Farewell System Already Activated")
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

						 
@slash.slash(name="farewell_disable", description="Delete the farewell image 🗑️")
async def welcome_disable(ctx):
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Farewell` WHERE `ID` = '{ctx.guild.id}'")
    value = cursor.fetchone()
    if value is None:
        await ctx.send("❌ Farewell System Not Enabled")
    if value is not None:
        cursor.execute(f"DELETE FROM `Farewell` WHERE `ID` = '{ctx.guild.id}'")
        mydb.commit()
        embed = discord.Embed(title="Farewelling System Disabled 🛑", description="The farewelling system is disabled\nUse /farewell_enable to enable it", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


@slash.slash(name="welcome_disable", description="Delete the welcome image 🗑️")
async def farewell_disable(ctx):
  if ctx.author.guild_permissions.manage_guild:
    cursor.execute(f"SELECT * FROM `Welcome` WHERE `ID` = '{ctx.guild.id}'")
    value = cursor.fetchone()
    if value is None:
        await ctx.send("❌ Welcome System Not Enabled")
    if value is not None:
        cursor.execute(f"DELETE FROM `Welcome` WHERE `ID` = '{ctx.guild.id}'")
        mydb.commit()
        embed = discord.Embed(title="Welcoming System Disabled 🛑", description="The welcoming system is disabled\nUse /welcome_enable to enable it", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")

@slash.slash(name="unban", description="Unban a member banned ⚒️")
async def unban(ctx, *, member):
  if ctx.author.guild_permissions.ban_members:
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
		
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        embed = discord.Embed(title="Member UnBan 🔨", description=f"Member : {user.mention}", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)
  else:
    await ctx.send("❗You Don't Have The Permissions Required")


# ---------------- Informations Commands ---------------- #
    

@slash.slash(name="nayo", description="Display Nayo Main Informations ⚙️")
async def nayo(ctx):
    value = bot.latency * 1000
    embed = discord.Embed(title = 'ℹ️ Nayo Informations', description = f'See Nayo Informations\n🏠 **Guilds** : `{str(len(bot.guilds))}`\n📶 **Latency** : `{value}Ms`\n🖥️ **CPU Usage** : `{psutil.cpu_percent()}%`\n🗄️ **Memory Usage** : `{psutil.virtual_memory().percent}%`\n💾 **Available Memory** : `{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%`', color=0xd0c0e9)
    await ctx.send(embed=embed)
    
@slash.slash(name="server_owner", description="Display the server owner 👑")
async def srvo(ctx):
    cowner = str(ctx.guild.owner)
    embed = discord.Embed(description=f"**{cowner}** is the owner of **{ctx.guild.name}** 👑",color=0xd0c0e9)
    await ctx.send(embed=embed)
    
@slash.slash(name="server_info", description="Display the server informations 📱")
async def srvi(ctx):    
    channel = ctx.channel
    created = ctx.guild.created_at.strftime("%H : %M, %A\n%B %Y")
    botnumber = [bot.mention for bot in ctx.guild.members if bot.bot]
    cowner = str(ctx.guild.owner)
    embed = discord.Embed(title=f"{ctx.guild.name}", colour=0xd0c0e9)
    embed.add_field(name=f"👑 Owner", value=f"`{cowner}`", inline=False)
    embed.add_field(name="🆔 Guild Id", value=f"`{ctx.guild.id}`", inline = False)
    embed.add_field(
        name="✏️ Created At",
        value=f"`{ctx.guild.created_at.__format__('%d %B %Y at %H:%M:%S')}`", inline=False)
    embed.add_field(name="📝 Description", value=f"`{ctx.guild.description}`", inline=False)
    embed.add_field(name="✅ Verification Level",
                    value=f"`{str(ctx.guild.verification_level)}`", inline=False)
    embed.add_field(name="📜 Number of Roles",
                    value=f"`{len(ctx.guild.roles)}`",
                    inline=False)
    embed.add_field(name="👥 Members", value=f"`{ctx.guild.member_count}`", inline=False)
    embed.add_field(name="📜 Number of Channels",
                    value=f"`{len(ctx.guild.channels)}`",
                    inline=False)
    embed.add_field(name="⌨️ Textuals Channels",
                    value=f"`{len(ctx.guild.text_channels)}`",
                    inline=False)
    embed.add_field(name="🎤 Voice Channels",
                    value=f"`{len(ctx.guild.voice_channels)}`",
                    inline=False)
    embed.add_field(name="🤖 Bots", value=(', '.join(botnumber)))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@slash.slash(name="privacy", description="Display the privacy policy of Nayo 🖥️")
async def privacy(ctx):
  embed = discord.Embed(title="Privacy Policy", description="What Nayo storing on his Database ?", color = 0xd0c0e9)
  embed.add_field(name="🆔 User ID", value="We're storing your User ID on Nayo Database, your ID is only use for the economy system on servers", inline=False)
  embed.add_field(name="🆔 Server ID", value="We're storing Server ID on Nayo Database, only for the economy, the level system and for commands that require to saved a informations on the server", inline=False)
  embed.add_field(name="🍪 Website Cookies", value="No Cookies are stored at this time", inline=False)
  embed.add_field(name="💬 Messages Storing", value="We don't storing any messages for the moment on Nayo Database (Maybe Later)", inline=False)
  embed.add_field(name="🕹️ Commands Storing", value="We don't storing a list of what commands do you use and when on Nayo Database but the owner of the server can activate `logs` command to know who use a Nayo Command", inline=False)
  embed.set_thumbnail(url="https://imgur.com/aHvi2yk.png")
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@slash.slash(name="ping", description="See the latence of Nayo 🏓")
async def ping(ctx):
    value = bot.latency * 1000
    if value >= 100 and value <= 300:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Moderately Stable`', color=0xFFA500)
      await ctx.send(embed=embed)
    if value < 100:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Stable`', color=0x008000)
      await ctx.send(embed=embed)
    if value > 300:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Bad`', color=0xFF0000)
      await ctx.send(embed=embed)

# Search Custom Image with unsplash website
@slash.slash(name="image_search", description="Search any image you want 📷")
async def search(ctx, image):
      embed = discord.Embed(
          title = f'📷 Random Image for : `{image}`',
          color = 0xd0c0e9)
      embed.set_image(url='https://source.unsplash.com/1920x1080/?{}'.format(image))            
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

@slash.slash(name="help", description="Send The Commands List Link and Other Links 🖇️")
async def help2(ctx):
    embed = discord.Embed(
        title="🕹️ Important Links 🕹️️",
        description=
        f"**Commands List** : https://nayobot.moe/commands\n**Panel** : https://nayobot.moe/dashboard\n**Documentation** : https://docs.nayobot.moe\n**Support Nayo** : https://nayobot.moe/premium\n**FAQ** : https://docs.nayobot.moe#content-faq\n**Nayo API** : https://docs.nayobot.moe#content-nayo-api",
        colour=0xd0c0e9)
    await ctx.send(embed=embed)

@slash.slash(name="embed", description="Send a custom embed 💬")
async def embed(ctx, channel: discord.TextChannel, title, description=None, image=None, thumbnail=None, footer=None):
  if ctx.author.guild_permissions.manage_guild:
    if description == None:
      if image == None:
        if thumbnail == None:
          if footer == None:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
        else:
          if footer == None:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
      else:
        if thumbnail == None:
          if footer == None:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_footer(text=footer)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
        else:
          if footer == None:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_image(url=image)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
    else:
      if image == None:
        if thumbnail == None:
          if footer == None:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
        else:
          if footer == None:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
      else:
        if thumbnail == None:
          if footer == None:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_footer(text=footer)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
        else:
          if footer == None:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_image(url=image)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")
          else:
            embed=discord.Embed(title=title, description=description, color=0xd0c0e9)
            embed.set_thumbnail(url=thumbnail)
            embed.set_image(url=image)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
            await ctx.send("✅ Embed Sent")

# Create a profile image that display your informations
@slash.slash(name="profile", description="Display your Profile Informations 🖥️")
async def profile(ctx, member : discord.Member=None):
    if not member:
        member = ctx.author
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = {member.id}")
    results = cursor.fetchone()
    if results is not None:
          def circle(pfp,size = (215,215)):
            pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
            bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(pfp.size, Image.ANTIALIAS)
            mask = ImageChops.darker(mask, pfp.split()[-1])
            pfp.putalpha(mask)
            return pfp

          name, nick, Id, status = str(member), member.display_name, str(member.id), str(member.top_role)

          created_at = member.created_at.strftime("%H : %M, %A\n%B %Y")
          joined_at = member.joined_at.strftime("%H : %M,  %A\n%B %Y")
          base = Image.open("Imgs/base2.png").convert("RGBA")
          background = Image.open("Imgs/NayoBack.png").convert("RGBA")

          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          name = f"{name[:16]}" if len(name)>16 else name
          nick = f"Alias - {nick[:17]}.." if len(nick)>17 else f"Alias - {nick}"
          value = cursor.execute(f"SELECT `COINS` from `Economy` where `ID` = '{ctx.author.id}'")
          rows = cursor.fetchall()
          for row in rows:
            val = row["COINS"]
          draw = ImageDraw.Draw(base)
          pfp = circle(pfp,(215,215))
          font = ImageFont.truetype("Fonts/nunito-regular.ttf", 38)
          akafont = ImageFont.truetype("Fonts/nunito-regular.ttf",30)
          subfont = ImageFont.truetype("Fonts/nunito-regular.ttf",25)

          draw.text((280,240),name,font = font)
          draw.text((270,315),nick,font = akafont)
          draw.text((60,490),Id,font = subfont)
          draw.text((230,625),val,font = subfont)
          draw.text((405,490),status,font = subfont)
          draw.text((65,770),created_at,font = subfont)
          draw.text((405,770),joined_at,font = subfont)
          base.paste(pfp,(56,158),pfp)

          background.paste(base,(0,0),base)

          with BytesIO() as a:
            background.save(a, "PNG")
            a.seek(0)
            await ctx.send(file = discord.File(a, "profile.png"))
    if results is None:
          def circle(pfp,size = (215,215)):
            pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
            bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(pfp.size, Image.ANTIALIAS)
            mask = ImageChops.darker(mask, pfp.split()[-1])
            pfp.putalpha(mask)
            return pfp

          name, nick, Id, status = str(member), member.display_name, str(member.id), str(member.top_role)

          created_at = member.created_at.strftime("%H : %M, %A\n%B %Y")
          joined_at = member.joined_at.strftime("%H : %M,  %A\n%B %Y")
          base = Image.open("Imgs/base1.png").convert("RGBA")
          background = Image.open("Imgs/NayoBack.png").convert("RGBA")

          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          name = f"{name[:16]}" if len(name)>16 else name
          nick = f"Alias - {nick[:17]}.." if len(nick)>17 else f"Alias - {nick}"

          draw = ImageDraw.Draw(base)
          pfp = circle(pfp,(215,215))
          font = ImageFont.truetype("Fonts/nunito-regular.ttf", 38)
          akafont = ImageFont.truetype("Fonts/nunito-regular.ttf",30)
          subfont = ImageFont.truetype("Fonts/nunito-regular.ttf",25)

          draw.text((280,240),name,font = font)
          draw.text((270,315),nick,font = akafont)
          draw.text((60,490),Id,font = subfont)
          draw.text((405,490),status,font = subfont)
          draw.text((65,770),created_at,font = subfont)
          draw.text((405,770),joined_at,font = subfont)
          base.paste(pfp,(56,158),pfp)

          background.paste(base,(0,0),base)

          with BytesIO() as a:
            background.save(a, "PNG")
            a.seek(0)
            await ctx.send(file = discord.File(a, "profile.png"))

# Display your pfp
@slash.slash(name="icon", description="Display your pfp 🖥️")
async def iconn(ctx, member : discord.Member=None):
  if member is None:
    member = ctx.author
    embed = discord.Embed(description=f"[Image Link]({member.avatar_url})", color=0xd0c0e9)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(description=f"[Image Link]({member.avatar_url})", color=0xd0c0e9)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


# ---------------- Anime Commands ---------------- #

	
@slash.slash(name="anime_quiz", description="Guess the name of an anime with clues 🥇")
async def quizanime(ctx):
    anime = ["Kimetsu","Learn","Darling  in the Franxx","No Game No Life","Attack on Titans","Boruto","HunterxHunter","My Hero Academia","One Punch Man","Nagatoro"]
    choice = random.choice(anime)
    if choice == "Kimetsu":
      embed = discord.Embed(description="It is the Taisho Period in Japan. Tanjiro, a kindhearted boy who sells charcoal for a living, finds his family slaughtered by a demon. To make matters worse, his younger sister Nezuko, the sole survivor, has been transformed into a demon herself. Though devastated by this grim reality, Tanjiro resolves to become a “demon slayer” so that he can turn his sister back into a human, and kill the demon that massacred his family", color=0xd0c0e9)
      embed.set_image(url="https://c.tenor.com/PtE9Ut4GMuEAAAAC/kimetsu-no-yaiba-demon-slayer.gif")
      await ctx.send(embed=embed)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      dss = ["Demon Slayer","demon slayer","Demon slayer","kimetsu no yaiba","demon Slayer"]
      if response.content not in dss:
        embed3 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Demon Slayer`", color=0xd0c0e9)
        await ctx.send(embed=embed3)
      else:
        embed200 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Demon Slayer`", color=0xd0c0e9)
        embed200.set_image(url="https://img.anili.st/media/87216")
        await ctx.send(embed=embed200)
    if choice == "Learn":
      embed4 = discord.Embed(description="Nariyuki Yuiga is in his last and most painful year of high school. In order to gain the special VIP recommendation which would grant him a full scholarship to college, he must now tutor his classmates as they struggle to prepare for entrance exams. Among his pupils are the sleeping beauty of the literary forest, Fumino Furuhashi, and the Thumbelina supercomputer, Rizu Ogata–two of the most beautiful super-geniuses at the school! While these two were thought to be academically flawless, it turns out that they’re completely clueless outside of their pet subjects…!?", color=0xd0c0e9)
      embed4.set_image(url="https://c.tenor.com/z8OuZjDDLQwAAAAC/bokuben-we-never-learn.gif")
      await ctx.send(embed=embed4)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      ds = ["we never learn","We never learn","We Never Learn","We Never learn","we Never learn"]
      if response.content in ds:
        embed12 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `We Never Learn`", color=0xd0c0e9)
        embed12.set_image(url="https://img.anili.st/media/98235")
        await ctx.send(embed=embed12)
      else:
        embed3 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `We Never Learn`", color=0xd0c0e9)
        await ctx.send(embed=embed3)
    if choice == "Darling  in the Franxx":
      embed4 = discord.Embed(description="The distant future: Humanity established the mobile fort city, Plantation, upon the ruined wasteland. Within the city were pilot quarters, Mistilteinn, otherwise known as the “Birdcage.” That is where the children live... Their only mission in life was the fight. Their enemies are the mysterious giant organisms known as Kyoryu. The children operate robots known as FRANXX in order to face these still unseen enemies. Among them was a boy who was once called a child prodigy: Code number 016, Hiro. One day, a mysterious girl called Zero Two appears in front of Hiro. I’ve found you, my Darling", color=0xd0c0e9)
      embed4.set_image(url="https://c.tenor.com/b5n-kjWGi4sAAAAC/darling-in-the-franxx.gif")
      await ctx.send(embed=embed4)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      df = ["Darling in the franxx","darling in the franxx","darling in the franx","Darling in the Franxx","Darling in the Franx","Darling in the franx"]
      if response.content in df:
        embed5 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Darling in the Franxx`", color=0xd0c0e9)
        embed5.set_image(url="https://img.anili.st/media/100937")
        await ctx.send(embed=embed5)
      else:
        embed6 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Darling in the Franxx`", color=0xd0c0e9)
        await ctx.send(embed=embed6)
    if choice == "Attack on Titans":
      embed7 = discord.Embed(description="Centuries ago, mankind was slaughtered to near extinction by monstrous humanoid creatures called titans, forcing humans to hide in fear behind enormous concentric walls. What makes these giants truly terrifying is that their taste for human flesh is not born out of hunger but what appears to be out of pleasure. To ensure their survival, the remnants of humanity began living within defensive barriers, resulting in one hundred years without a single titan encounter. However, that fragile calm is soon shattered when a colossal titan manages to breach the supposedly impregnable outer wall, reigniting the fight for survival against the man-eating abominations", color=0xd0c0e9)
      embed7.set_image(url="https://giffiles.alphacoders.com/114/114711.gif")
      await ctx.send(embed=embed7)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      at = ["Attack on Titans","Attack on titans","Attack des Titans","attack des titans","attack on titans","attaque des titans","Attaque des Titans","attack on Titans"]
      if response.content in at:
        embed8 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Attack on Titans`", color=0xd0c0e9)
        embed8.set_image(url="https://img.anili.st/media/16498")
        await ctx.send(embed=embed8)
      else:
        embed9 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Attack on Titans`", color=0xd0c0e9)
        await ctx.send(embed=embed9)
    if choice == "No Game No Life":
      embed7 = discord.Embed(description="Surreal comedy that follows Sora and Shiro, shut-in NEET siblings and the online gamer duo behind the legendary username Kuuhaku. They view the real world as just another lousy game; however, a strange e-mail challenging them to a chess match changes everything—the brother and sister are plunged into an otherworldly realm where they meet Tet, the God of Games.", color=0xd0c0e9)
      embed7.set_image(url="http://ekladata.com/QVUSphDuvikLmYFilfgr26n_NAg.gif")
      await ctx.send(embed=embed7)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      ng = ["No Game No Life","no game no life","No game no life","no Game no Life","No game No life"]
      if response.content in ng:
        embed8 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `No Game No Life`", color=0xd0c0e9)
        embed8.set_image(url="https://img.anili.st/media/19815")
        await ctx.send(embed=embed8)
      else:
        embed9 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `No Game No Life`", color=0xd0c0e9)
        await ctx.send(embed=embed9)
    if choice == "Naruto":
      embed89 = discord.Embed(description="Surreal comedy that follows Sora and Shiro, shut-in NEET siblings and the online gamer duo behind the legendary username Kuuhaku. They view the real world as just another lousy game; however, a strange e-mail challenging them to a chess match changes everything—the brother and sister are plunged into an otherworldly realm where they meet Tet, the God of Games.", color=0xd0c0e9)
      embed89.set_image(url="http://ekladata.com/QVUSphDuvikLmYFilfgr26n_NAg.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["Naruto","naruto"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `No Game No Life`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/19815")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `No Game No Life`", color=0xd0c0e9)
        await ctx.send(embed=embed94)
    if choice == "Boruto":
      embed89 = discord.Embed(description="Naruto was a young shinobi with an incorrigible knack for mischief. He achieved his dream to become the greatest ninja in the village and his face sits atop the Hokage monument. But this is not his story... A new generation of ninja are ready to take the stage, led by Naruto's own son", color=0xd0c0e9)
      embed89.set_image(url="https://giffiles.alphacoders.com/126/126071.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["Boruto","boruto","Boruto next generations","boruto next generations"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Boruto`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/87178")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Boruto`", color=0xd0c0e9)
        await ctx.send(embed=embed94)
    if choice == "HunterxHunter":
      embed89 = discord.Embed(description="Nen: the hidden source of energy and potential that runs through everyone, and gives those that master it a source of great power. Inside Nen is the potential for limitless light and limitless darkness. The Hunter Association has arisen to control access to it. Hunters come in many shapes and forms, and with many different appetites - but all of them have learned to master Nen, and use it to chase wealth, power, and their dreams", color=0xd0c0e9)
      embed89.set_image(url="https://64.media.tumblr.com/6215c8dbd16882a0c21812c80eb671e5/02929089901ae47b-d5/s500x750/e29612972b573cc34157d312b79c618546cbd084.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["Hunter x Hunter","hunter x hunter","hunterxhunter","HunterxHunter"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Hunter x Hunter`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/11061")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Boruto`", color=0xd0c0e9)
        await ctx.send(embed=embed94)
    if choice == "My Hero Academia":
      embed89 = discord.Embed(description="What would the world be like if 80 percent of the population manifested extraordinary superpowers called “Quirks” at age four? Heroes and villains would be battling it out everywhere! Becoming a hero would mean learning to use your power, but where would you go to study? U.A. High's Hero Program of course! But what would you do if you were one of the 20 percent who were born Quirkless ?", color=0xd0c0e9)
      embed89.set_image(url="https://i.pinimg.com/originals/47/96/bd/4796bdf3dd72c63b5fb4edc738f3a703.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["my hero academia","My hero academia","My Hero Academia","Boku no hero academia"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `My Hero Academia`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/21459")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `My Hero Academia`", color=0xd0c0e9)
        await ctx.send(embed=embed94)
    if choice == "Nagatoro":
      embed89 = discord.Embed(description="A girl in a lower grade just made me cry! One day, Senpai visits the library after school and becomes the target of a super sadistic junior ! She's annoying yet adorable. It's painful, but you still want to be by her side. This is a story about an extremely sadistic and temperamental girl and you'll feel something awaken inside of you.", color=0xd0c0e9)
      embed89.set_image(url="https://c.tenor.com/eFRCrniJ2-EAAAAd/nagatoro-hayase-nagatoro.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["Nagatoro","nagatoro","nagatoro san","Nagatoro san"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `Nagatoro`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/100664")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `Nagatoro`", color=0xd0c0e9)
        await ctx.send(embed=embed94)
    if choice == "One Punch Man":
      embed89 = discord.Embed(description="The seemingly ordinary and unimpressive Saitama has a rather unique hobby: being a hero. In order to pursue his childhood dream, he trained relentlessly for three years—and lost all of his hair in the process. Now, Saitama is incredibly powerful, so much so that no enemy is able to defeat him in battle. In fact, all it takes to defeat evildoers with just one punch has led to an unexpected problem—he is no longer able to enjoy the thrill of battling and has become quite bored.", color=0xd0c0e9)
      embed89.set_image(url="https://giffiles.alphacoders.com/128/12887.gif")
      await ctx.send(embed=embed89)
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      response = await bot.wait_for('message', check=check)
      nr = ["One-Punch Man","one punch man","One punch man","One Punch Man"]
      if response.content in nr:
        embed84 = discord.Embed(title="Congratulations 🎉", description=f"You find the name of this anime : `One Punch Man`", color=0xd0c0e9)
        embed84.set_image(url="https://img.anili.st/media/21087")
        await ctx.send(embed=embed84)
      else:
        embed94 = discord.Embed(title="Game Over ❌", description=f"Your response : `{response.content}`\nThe correct answer : `One Punch Man`", color=0xd0c0e9)
        await ctx.send(embed=embed94)

@slash.slash(name="anime_search", description="Search Anime Informations 🌐")
async def anime_search(ctx, name):
    animelink = f"https://kitsu.io/api/edge/anime?filter[text]={name}"
    response = requests.get(animelink)
    resp = response.json()
    if resp['meta']['count'] != 0:
        name = resp['data'][0]['attributes']['canonicalTitle']
        jap = resp['data'][0]['attributes']['titles']['ja_jp']
        creat = resp['data'][0]['attributes']['createdAt']
        desc = resp['data'][0]['attributes']['description']
        sub = resp['data'][0]['attributes']['subtype']
        stat = resp['data'][0]['attributes']['status']
        dur = resp['data'][0]['attributes']['totalLength']
        durep = resp['data'][0]['attributes']['episodeLength']
        age = resp['data'][0]['attributes']['ageRatingGuide']
        num = resp['data'][0]['attributes']['episodeCount']
        img2 = resp['data'][0]['attributes']['coverImage']
        rat = resp['data'][0]['attributes']['popularityRank']
        if img2:
            img = resp['data'][0]['attributes']['coverImage']['original']
            embed = discord.Embed(title=name + " / " + jap, description=desc + f"\n\n🗓️ Release Date : `{creat}`\n🖥️ Type : `{sub}`\n🔍 Status : `{stat}`\n⌛ Duration : `{dur} Minutes`\n⏲ Episode Duration : `{durep} Minutes`\n🔞 Age Rating : `{age}`\n🔢 Episodes : `{num}`\n⭐ Community Rating : `#{rat}`", color=0xd0c0e9)
            embed.set_image(url=img)
            await ctx.send(embed=embed)
        else:
            embed2 = discord.Embed(title=name + " / " + jap, description=desc + f"\n\n🗓️ Release Date : `{creat}`\n🖥️ Type : `{sub}`\n🔍 Status : `{stat}`\n⌛ Duration : `{dur} Minutes`\n⏲ Episode Duration : `{durep} Minutes`\n🔞 Age Rating : `{age}`\n🔢 Episodes : `{num}`\n⭐ Community Rating : `#{rat}`", color=0xd0c0e9)
            await ctx.send(embed=embed2)
    else:
        embed3 = discord.Embed(description="❌ No Anime Found", color=0xd0c0e9)
        await ctx.send(embed=embed3)


# ---------------- Fun Commands ---------------- #

# Create a Wanted Poster of You
@slash.slash(name="image_wanted", description="Display a Wanted Poster 🔍")
async def wanted(ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author

    wanted = Image.open("Imgs/Wanted.jpg")
    asset = member.avatar_url
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((300,300))
    wanted.paste(pfp, (80,220))
    wanted.save("Imgs/wanted2.jpg")
    file = discord.File("Imgs/wanted2.jpg")
    embed = discord.Embed(description=f"{member.mention} is WANTED 🔍", color=0xd0c0e9)
    embed.set_image(url="attachment://wanted2.jpg")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file = file, embed=embed)

# Invert your pfp
@slash.slash(name="image_invert", description="Invert you pfp 🪛")
async def invert(ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    image = member.avatar_url
    data = BytesIO(await image.read())
    pfp = Image.open(data)
    inverted_image = PIL.ImageOps.invert(pfp)
    inverted_image.save('Imgs/inverted.png')
    file = discord.File("Imgs/inverted.png")
    embed = discord.Embed(color=0xd0c0e9)
    embed.set_image(url="attachment://Imgs/inverted.png")
    await ctx.send(file=file, embed=embed)

# Create a UA Card of You :3
@slash.slash(name="uacard", description="Display your My Hero Academia Card 🦸‍♂️")
async def uacard(ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    image = member.avatar_url
    data = BytesIO(await image.read())
    pfp = Image.open(data)
    pfp = pfp.resize((190,190))
    grade1 = ["Year 1, Class 1-A","Year 1, Class 2-A","Year 2, Class 1-B","Year 1, Class 2-A","Year 2, Class 1-A"]
    grade = random.choice(grade1)
    name = str(member)
    quirk1 = ["None","One For All","Zero Gravity","Transform","Half-Cold Half-Hot","Creation","Invisibility","Frog","Explosion"]
    idm = member.created_at.strftime("%A %B %Y")
    quirk = random.choice(quirk1)
    ua = Image.open("Imgs/ua.png")
    draw = ImageDraw.Draw(ua)
    ua.paste(pfp, (50,145))
    font2 = ImageFont.truetype("Fonts/Discord.ttf", 20)
    draw.text((318,208),name,font = font2, fill=(0,0,0))
    draw.text((318,245),idm,font = font2, fill=(0,0,0))
    draw.text((318,140),grade,font = font2, fill=(0,0,0))
    draw.text((318,275),quirk,font = font2, fill=(0,0,0))
    ua.save("Imgs/uacard.png")
    file = discord.File("Imgs/uacard.png")
    embed = discord.Embed(description=f"{member.mention}, here your UA Card 💳",color=0xd0c0e9)
    embed.set_image(url="attachment://uacard.png")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file=file, embed=embed)

# Create a Yu-Gi-Oh Card of You
@slash.slash(name="yugioh", description="Display you on a Yu-Gi-Oh Card ⭐")
async def yugioh(ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author

    tri = Image.open("Imgs/YuGiOh.png")
    asset = member.avatar_url
    name = str(member)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((503,503))
    tri.paste(pfp, (100,210))
    draw = ImageDraw.Draw(tri)
    atk = "5000"
    defe = "5000"
    dis = ["Discord Warrior","Discord Dragon","Discord Master"]
    dis2 = random.choice(dis)
    desc = f"The legendary {dis2} who became the owner\nof the biggest discord server. You are invincible and\npowerful, nothing stops you in your quest"
    font2 = ImageFont.truetype("Fonts/light.ttf", 50)
    font = ImageFont.truetype("Fonts/light.ttf", 30)
    draw.text((70,58),name,font = font2)
    draw.text((72,770),dis2,font = font)
    draw.text((70,810),desc,font = font)
    draw.text((440,930),atk,font = font)
    draw.text((580,930),defe,font = font)
    tri.save("Imgs/yugioh2.png")
    file = discord.File("Imgs/yugioh2.png")
    embed = discord.Embed(description=f"{member.mention} is a LIMITED EDITION ⭐", color=0xd0c0e9)
    embed.set_image(url="attachment://yugioh2.png")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file=file, embed=embed) 

@slash.slash(name="ratecool", description="Display your cool percentage 😎")
async def ratecool2(ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Cool Rate 😎", description=f"You are cool at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)

@slash.slash(name="rategay", description="Display your gay percentage 🌈")
async def rategay2(ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Gay Rate 🌈", description=f"You are gay at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)

@slash.slash(name="rategeek", description="Display your geek percentage 👾")
async def rategeek2(ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Geek Rate  👾", description=f"You are a geek at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)

@slash.slash(name="headsortails", description="Simulates a heads or tails throw 🪙")
async def headsortails2(ctx):
    liste = ["Heads", "Tails"]
    choix = random.choice(liste)
    embed = discord.Embed(title=f"🪙 {choix}", description=f"You came across\n**{choix}** this time ", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/514/PNG/512/coin-euro_icon-icons.com_51032.png")
    await ctx.send(embed=embed)

@slash.slash(name="ratelove", description="Display the percentage of love enter two member 💕")
async def ratelove2(ctx, member: discord.Member, p2: discord.Member):
    value = random.randrange(101)
    if value > 50 and value < 90:
      embed = discord.Embed(title="Love Rate ❤️", description=f"{member.mention} and {p2.mention}\nYou have **{value}%** of love 💕\nLove is in the air !", color=0xd0c0e9)
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)
    if value < 30:
      embed = discord.Embed(title="Love Rate ❤️", description=f"{member.mention} and {p2.mention}\nYou have **{value}%** of love 💕\nDamn, that doesn't seem to work !", color=0xd0c0e9)
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)
    if value < 50 and value > 30:
      embed = discord.Embed(title="Love Rate ❤️", description=f"{member.mention} and {p2.mention}\nYou have **{value}%** of love 💕\nAlmost ! Do not be discouraged", color=0xd0c0e9)
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)
    if value > 90:
      embed = discord.Embed(title="Love Rate ❤️", description=f"{member.mention} and {p2.mention}\nYou have **{value}%** of love 💕\nThat's it ! You were meant to be together 😘", color=0xd0c0e9)
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)


# ---------------- Old Commands ---------------- #


# Slow Mode
@bot.command()
@commands.has_permissions(manage_guild=True)
async def slowmode(ctx, time: int):
    await ctx.channel.edit(slowmode_delay=time)
    await ctx.send(
        f"Slow mode activated for this channel, delay : **{time}** seconds\nTo desactivate slowmode tipe `>stopsm`"
    )


# Stop Slow Mode
@bot.command()
@commands.has_permissions(manage_guild=True)
async def stopsm(ctx):
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send(f"Slow mode disabled for this channel")

# On Ready Event
@bot.event
async def on_ready():
  bot.loop.create_task(status_task())
  print("Nayo is Ready")
  print(f"Connected to : {str(len(bot.guilds))} Guilds")

async def status_task():
    while True:
        members = 0
        for guild in bot.guilds:
          members += guild.member_count - 1
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="" + str(len(bot.guilds)) + " servers ❀ /help"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} Users ❀ /help"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nayobot.moe ❀ /help"))
        await asyncio.sleep(10)


# Erase Base Help Command
bot.remove_command('help')


# ---------------- Errors Response ---------------- #


@bot.event
async def on_command_error(ctx, error):
	
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "<:KomiStare:974383095769858078> Weird..., it seems that this command does not exist..."
        )
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "<:KomiStare:974383095769858078> An argument is missing in the command performed (You probably need to mention a user or a channel) :3"
        )
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "<:KomiStare:974383095769858078> You do not have permission to perform this command :3"
        )
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(
            "<:KomiStare:974383095769858078> Weird... it looks like you can't do this command here... :3"
        )
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(
            "<:KomiStare:974383095769858078> Oops... it looks like I don't have the required permissions... :3"
        )


# ------------------ Old Admin Command ------------------- #


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, reason="No Reason"):
    if discord.utils.get(ctx.guild.roles, name="Muted"):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await ctx.message.add_reaction("✅")
        await member.add_roles(role)
        embed = discord.Embed(title="Member Muted  ⚖️",
                              description=f"Member : {member.mention}",
                              color=0xd0c0e9)
        await ctx.send(embed=embed)
    else:
        await ctx.guild.create_role(name="Muted")
        await ctx.message.add_reaction("✅")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        embed = discord.Embed(title="Member Muted  ⚖️",
                              description=f"Member : {member.mention}",
                              color=0xd0c0e9)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason="No Reason"):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role, reason=reason)
    await ctx.message.add_reaction("✅")
    embed = discord.Embed(title="Member Unmute  ⚖️",
                          description=f"Member : {member.mention}",
                          color=0xd0c0e9)
    await ctx.send(embed=embed)


@bot.command()
async def privacy(ctx):
  embed = discord.Embed(title="Privacy Policy", description="What Nayo storing on his Database ?", color = 0xd0c0e9)
  embed.add_field(name="🆔 User ID", value="We're storing your User ID on Nayo Database, your ID is only use for the economy system on servers", inline=False)
  embed.add_field(name="🆔 Server ID", value="We're storing Server ID on Nayo Database, only for the economy, the level system and for commands that require to saved a informations on the server", inline=False)
  embed.add_field(name="🍪 Website Cookies", value="We're storing cookies on Nayo Website but is only used by Google", inline=False)
  embed.add_field(name="💬 Messages Storing", value="We don't storing any messages for the moment on Nayo Database (Maybe Later)", inline=False)
  embed.add_field(name="🕹️ Commands Storing", value="We don't storing a list of what commands do you use and when on Nayo Database but the owner of the server can activate `logs` command to know who use a Nayo Command", inline=False)
  embed.set_thumbnail(url="https://imgur.com/aHvi2yk.png")
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)


# ---------------- Anime Gif Commands ---------------- #


@slash.slash(name="bang_random", description="Bang a member 🔫")
async def bang_random(ctx):
    r = requests.get("https://nayobot.moe/api/bang")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** bangs **{user.mention}** 🔥",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="eightball", description="Play 8 Ball 🎱")
async def eightballl(ctx, *, question):
    liste = ["Maybe, it's work","Hmm, i think No","Probably","Sure","Absolutely not","Yes","No","Perhaps","I cannot predict now","Of course","It's a big No","Negative","Positive","As i see it's a Yes","I predict that's a No","Hmm, i don't know","Hmm that's a Yes and a No"]
    choice = random.choice(liste)
    embed = discord.Embed(title="🎱 Magic 8 Ball", description=f"Question : **{question}**\nAnswer : **{choice}**", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://i.ibb.co/nbHvbPD/png-transparent-magic-8-ball-eight-ball-billiards-billiard-balls-ball-sphere-sports-pool.png")
    await ctx.send(embed=embed)


@slash.slash(name="shocked", description="Send a Shocked Anime Gif 😱")
async def shocked(ctx):
    animeshocked = requests.get("https://nayobot.moe/api/shocked")
    choice = animeshocked.json()
    Img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** is shocked 😱",
                          color=0xd0c0e9)
    embed.set_image(url=Img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)

@slash.slash(name="angry", description="Send a Angry Anime Gif 😡")
async def angry(ctx):
    r = requests.get("https://nayobot.moe/api/angry")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** is angry 😡",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="die", description="Send a Die Anime Gif ☠️")
async def die(ctx):
    r = requests.get("https://nayobot.moe/api/die")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** dies 😵",
                          color=0xd0c0e9)
    embed.set_image(url=die)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)

@slash.slash(name="blush", description="Send a Blush Anime Gif 😳")
async def blush(ctx):
    r = requests.get("https://nayobot.moe/api/blush")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** blushs 😳",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
	

@slash.slash(name="wink", description="Send a Wink Anime Gif 😉")
async def wink(ctx, user):
    r = requests.get("https://nayobot.moe/api/wink")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** winks at **{user}** 😉",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="dab", description="Send a Dab Anime Gif 😎")
async def dab(ctx):
    animeschoked = [
    "https://c.tenor.com/C5riNZAzrksAAAAC/dab-anime.gif",
    "https://c.tenor.com/cbOd_mc2DvIAAAAC/chika-fujiwara-dance.gif",
    "https://c.tenor.com/q045q-y_NdQAAAAC/ini-miney-ace-attorney.gif",
    "https://c.tenor.com/w5Oop53gtA8AAAAC/dab-dabbing.gif","https://c.tenor.com/hLF5hGCWoXAAAAAC/dab-megumin.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** dabs 😎",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="happy", description="Send a Happy Anime Gif 😀")
async def happy(ctx):
    r = requests.get("https://nayobot.moe/api/happy")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** is happy 😀",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="sexy", description="Send a Sexy Anime Gif 😉")
async def sexy(ctx):
    animesexy = [
    "https://c.tenor.com/059DZ7RMjXkAAAAC/conejita-dance.gif",
    "https://c.tenor.com/AKwhCmqXhj4AAAAM/hot-anime-sexy.gif",
    "https://c.tenor.com/BGTXuJ-Q8uMAAAAC/free-anime.gif",
    "https://c.tenor.com/cL7b2RYjAfAAAAAC/hot-love.gif",
    "https://c.tenor.com/0HEJfhGviloAAAAd/ice-cream-anime.gif",
    "https://c.tenor.com/qhTqWQWtphsAAAAC/my-hero-academia-boku-no-hero-academia.gif",
    "https://c.tenor.com/0DBeShO2pAQAAAAC/gnam-anime.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}**", color=0xd0c0e9)
    embed.set_image(url=random.choice(animesexy))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="cry", description="Send a Cry Anime Gif 😭")
async def cry(ctx):
    r = requests.get("https://nayobot.moe/api/cry")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** is crying 😭", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="hello", description="Send a Hello Anime Gif 👋")
async def hello(ctx, user):
    animesalut = [
    "https://c.tenor.com/Ch4VFEjuI7IAAAAC/anime-boy.gif",
    "https://c.tenor.com/S6Kxbixp1yUAAAAC/gakkou-gurashi-hello.gif",
    "https://c.tenor.com/n1szpPp19d0AAAAC/yuigahama-yahallo.gif",
    "https://c.tenor.com/thNxDWlG1EcAAAAd/killua-zoldyck-anime.gif"]
    choice = random.choice(animesalut)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** say hello to **{user}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=choice)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="kiss", description="Send a Kiss Anime Gif 😘")
async def kiss(ctx, user):
    r = requests.get("https://nayobot.moe/api/kiss")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** kiss **{user}** 😘",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="kiss_random", description="Send a Kiss Anime Gif to a random member 😘")
async def kiss_random(ctx):
    r = requests.get("https://nayobot.moe/api/kiss")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** kiss **{user.mention}** 😘",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="hug", description="Send a Hug Anime Gif 🤗")
async def hug(ctx, user):
    r = requests.get("https://nayobot.moe/api/hug")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** hugs **{user}** 🤗",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="dance", description="Send a Dance Anime Gif 💃")
async def dance(ctx):
    r = requests.get("https://nayobot.moe/api/dance")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** dance 💃",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="dance_random", description="Send a Dance Anime Gif to a random member 💃")
async def dance_random(ctx):
    r = requests.get("https://nayobot.moe/api/dance")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** do a dance to **{user.mention}** 💃",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)



@slash.slash(name="laugh", description="Send a Laugh Anime Gif 😂")
async def laugh(ctx, user):
    r = requests.get("https://nayobot.moe/api/laugh")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** laughs at **{user}** 😂",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="poke", description="Send a Poke Anime Gif 👉")
async def poke(ctx, user):
    r = requests.get("https://nayobot.moe/api/poke")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** pokes **{user}** 👉",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="laugh_random", description="Send a Laugh Anime Gif to a random member 😂")
async def laugh_random(ctx):
    r = requests.get("https://nayobot.moe/api/laugh")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** laughs at **{user.mention}** 😂",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="hello_random", description="Send a Hello Anime Gif to a random member 👋")
async def hello_random(ctx):
    animesalut = [
    "https://c.tenor.com/Ch4VFEjuI7IAAAAC/anime-boy.gif",
    "https://c.tenor.com/S6Kxbixp1yUAAAAC/gakkou-gurashi-hello.gif",
    "https://c.tenor.com/n1szpPp19d0AAAAC/yuigahama-yahallo.gif",
    "https://c.tenor.com/thNxDWlG1EcAAAAd/killua-zoldyck-anime.gif"]
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** say hello to **{user.mention}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animesalut))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="hug_random", description="Send a Hug Anime Gif to a random member 🤗")
async def hug_random(ctx):
    r = requests.get("https://nayobot.moe/api/hug")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** hugs **{user.mention}** 🤗",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="slap_random", description="Send a Slap Anime Gif to a random member 👋")
async def slap_random(ctx):
    r = requests.get("https://nayobot.moe/api/slap")
    choicee = r.json()
    img = choicee['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** slaps **{user.mention}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="slap", description="Send a Slap Anime Gif 👋")
async def slap(ctx, user):
    r = requests.get("https://nayobot.moe/api/slap")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** slaps **{user}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="eat", description="Send a Eat Anime Gif 🍴")
async def eat(ctx, user):
    animeeat = [
    "https://c.tenor.com/6xtxPu0luFcAAAAd/kimetsu-no-yaiba-movie-mugen-ressha-hen-kyojuro-rengoku.gif",
    "https://c.tenor.com/p5DGewKTyQAAAAAC/loli-dragon.gif",
    "https://c.tenor.com/RjF1evJJiSsAAAAC/anime-darlinginthefranxx.gif",
    "https://c.tenor.com/9Vc1AlpPJEkAAAAd/noragami.gif",
    "https://c.tenor.com/jUtHGd3o7xUAAAAC/oui-eat.gif"]

    embed = discord.Embed(
        description=f"**{ctx.author.name}** eats {user}🍴",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animeeat))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="eat_random", description="Send a Eat Anime Gif to a random member 🍴")
async def eat_random(ctx):
    animeeat = [
    "https://c.tenor.com/6xtxPu0luFcAAAAd/kimetsu-no-yaiba-movie-mugen-ressha-hen-kyojuro-rengoku.gif",
    "https://c.tenor.com/p5DGewKTyQAAAAAC/loli-dragon.gif",
    "https://c.tenor.com/RjF1evJJiSsAAAAC/anime-darlinginthefranxx.gif",
    "https://c.tenor.com/9Vc1AlpPJEkAAAAd/noragami.gif",
    "https://c.tenor.com/jUtHGd3o7xUAAAAC/oui-eat.gif"]
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** eats {user.mention}🍴",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animeeat))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="kill_random", description="Send a Kill Anime Gif to a random member 💀")
async def kill_random(ctx):
    r = requests.get("https://nayobot.moe/api/kill")
    choice = r.json()
    img = choice['Img']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** killed **{user.mention}** 💀",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="kill", description="Send a Kill Anime Gif 💀")
async def kill(ctx, user):
    r = requests.get("https://nayobot.moe/api/kill")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** killed **{user}** 💀",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


@slash.slash(name="bang", description="Send a Bang Anime Gif 🔥")
async def bang(ctx, user):
    r = requests.get("https://nayobot.moe/api/bang")
    choice = r.json()
    img = choice['Img']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** bangs **{user}** 🔥",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)

@slash.slash(name="pat", description="Send a Pat Anime Gif 🥺 (Need Premium Bank Account)")
async def pat(ctx, user):
      r = requests.get("https://nayobot.moe/api/pat")
      choice = r.json()
      img = choice['Img']
      embed = discord.Embed(
        description=f"**{ctx.author.name}** pats **{user}** 🥺",
        color=0xd0c0e9)
      embed.set_image(url=img)
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
      await ctx.send(embed=embed)


@slash.slash(name="disgusted", description="Send a Disgusted Anime Gif 🤮 (Need Premium Bank Account)")
async def disgusted(ctx):
      r = requests.get("https://nayobot.moe/api/disgusted")
      choice = r.json()
      img = choice['Img']
      embed = discord.Embed(
        description=f"**{ctx.author.name}** is disgusted 🤮",
        color=0xd0c0e9)
      embed.set_image(url=img)
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
      await ctx.send(embed=embed)

@slash.slash(name="meme", description="Send a Meme Anime Gif 🤣")
async def meme(ctx):
    meme = ["https://c.tenor.com/btMXU0Gmb_gAAAAC/yeet.gif","https://c.tenor.com/Cbm8FdN4tbAAAAAC/sailor-moon-suit-old-man.gif","https://c.tenor.com/6NEZpt9dEpkAAAAC/anime-dark.gif","https://c.tenor.com/D6ZdzLuQN_kAAAAC/chunibyo.gif","https://c.tenor.com/NZ81KxrwImQAAAAd/anime-nezuko.gif","https://c.tenor.com/oqmSdq-jzdIAAAAC/pug.gif","https://c.tenor.com/9_J-Hk_7SZ8AAAAC/wifi-down.gif","https://c.tenor.com/TdqhucWI5sEAAAAC/meme.gif","https://c.tenor.com/-m1mRsuTe-oAAAAC/anime-smash.gif","https://c.tenor.com/cWHJLNx-NmYAAAAC/life-kick.gif","https://c.tenor.com/BW0Y6l-U_7UAAAAC/anime-anime-opening.gif"]
    choice = random.choice(meme)
    embed = discord.Embed(
        description=f"**Random Anime Meme** 🤣\n[Click Here if the image does not appear]({choice})",
        color=0xd0c0e9)
    embed.set_image(url=choice)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)


# ---------------- 🔞 NSFW Anime Gif Commands ---------------- #

# If you are not into NSFW Things, skip this part



@slash.slash(name="cum", description="Send a Cum Anime Image or Gif 🔞")
async def cumm(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/cum")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"Cum Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

@slash.slash(name="hentai", description="Send a Hentai Anime Image or Gif 🔞")
async def hentaii(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/hentai")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Hentai Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

@slash.slash(name="blowjob", description="Send a BlowJob Anime Image or Gif 🔞")
async def blowjobb(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/blowjob")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"BlowJob Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

@slash.slash(name="pussy", description="Send a Pussy Anime Image or Gif 🔞")
async def pussyy(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/pussy")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Pussy Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")
  

@slash.slash(name="boobs", description="Send a Boobs Anime Image or Gif 🔞")
async def boobss(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/boobs")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Boobs Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

@slash.slash(name="yaoi", description="Send a Yaoi Anime Image or Gif 🔞")
async def yaoii(ctx):
  if ctx.channel.is_nsfw():
    api = NekoBotAsync()
    img = (await api.get_image("yaoi")).message
    await api.close()
    embed = discord.Embed(
      description=f"Yaoi Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

	
@slash.slash(name="lewd", description="Send a Lewd Anime Image or Gif 🔞")
async def lewdd(ctx):
  if ctx.channel.is_nsfw():
      animekiss = requests.get("http://api.nekos.fun:8080/api/lewd")
      choice = animekiss.json()
      img = choice['image']
      embed = discord.Embed(
        description=f"Lewd Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
      embed.set_image(url=img)
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
      await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")

@slash.slash(name="yuri", description="Send a Yuri Anime Image or Gif 🔞")
async def yurii(ctx):
  if ctx.channel.is_nsfw():
    animekiss = requests.get("http://api.nekos.fun:8080/api/lesbian")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"Yuri Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(embed=embed)
  else:
    await ctx.send("⚠️ You can only send NSFW on NSFW Channels")


# ---------------- Cog and Bot Run ------------------ #
		

bot.add_cog(help_utils.help(bot))
bot.add_cog(admin_utils.admin(bot))
bot.add_cog(gif_utils.gif(bot))
bot.add_cog(fun_utils.fun(bot))
bot.add_cog(info_utils.info(bot))
bot.add_cog(anime_utils.anime(bot))
bot.add_cog(economy.eco(bot))
bot.add_cog(security_utils.secure(bot))
bot.run("X") # Insert your TOKEN
