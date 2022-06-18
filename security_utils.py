# Anime Commands
import discord
import discord.utils
import random
import datetime
import youtube_dl
import os
from discord import voice_client
from discord import FFmpegPCMAudio
import asyncio
import discord_voice
from discord.ext import commands

class secure(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

 
  # THIS COG IS IN DEV TO BE UPDATED
  # Old Security Commands, Only Captcha Commands don't work


  @commands.command(aliase="captcha enable")
  async def captcha_enable(self, ctx):
    guild = ctx.guild
    value = discord.utils.get(ctx.guild.roles, name="Unverified")
    value2 = discord.utils.get(ctx.guild.channels, name="🔑・verification")
    if value is None:
      overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False)
      }
      perms = discord.Permissions(view_channel=False)
      await guild.create_role(name="Unverified", permissions=perms)
      if value2 is None:
        overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        value: discord.PermissionOverwrite(view_channel=True)
        }
        await ctx.guild.create_text_channel('🔑・verification')
        db[f"Captcha-{ctx.guild.id}"] = f"Enabled"
        await ctx.send("✅ Captcha Enabled")
      else:
        db[f"Captcha-{ctx.guild.id}"] = f"Enabled"
        await ctx.send("✅ Captcha Enabled")
    else:
      if value2 is None:
        guild = ctx.message.guild
        await guild.create_text_channel("🔑・verification")
        db[f"Captcha-{ctx.guild.id}"] = f"Enabled"
      else:
        await ctx.value2.set_permissions(ctx.guild.defaul_role, value, send_messages=True)
        db[f"Captcha-{ctx.guild.id}"] = f"Enabled"
        await ctx.send("✅ Captcha Enabled")

  @commands.command(aliase="captcha disable")
  async def captcha_disable(self, ctx):
    value = db.get(f"Captcha-{ctx.guild.id}")
    if value is None:
      await ctx.send("You have to enable captcha before disable it")
    else:
      del db[f"Captcha-{ctx.guild.id}"]
      await ctx.send("✅ Captcha Disabled")

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def antispam(self, ctx):
    value = db.get(f"Spam-{ctx.guild.id}")
    if value is None:
      await ctx.send("Command Temporarily Desactivate")
      #db[f"Spam-{ctx.guild.id}"] = "0"
      #await ctx.send("✅ Anti Spam Set")
    else:
      await ctx.send("Command Temporarily Desactivate")

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def antilink(self, ctx):
    value = db.get(f"Link-{ctx.guild.id}")
    if value is None:
      db[f"Link-{ctx.guild.id}"] = "0"
      await ctx.send("✅ Anti Link Set")
    else:
      await ctx.send("Anti Link already set")

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def reset_antilink(self, ctx):
    value = db.get(f"Link-{ctx.guild.id}")
    if value is None:
      await ctx.send("No Antilink set")
    else:
      del db[f"Link-{ctx.guild.id}"]
      await ctx.send("✅ Anti Link Reset")

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def reset_antispam(self, ctx):
    value = db.get(f"Spam-{ctx.guild.id}")
    if value is None:
      await ctx.send("No AntiSpam set")
    else:
      del db[f"Spam-{ctx.guild.id}"]
      await ctx.send("✅ Anti Spam Reset")

 
  # -------------------- Music Commands ------------------------ #


  @commands.command()
  async def join(self,ctx):
    voice_channel = ctx.author.voice.channel
    if ctx.author.voice is None:
      await ctx.send("Enter in a voice channel before type `join`")
    if ctx.voice_client is None:
      print("Ok1")
      await ctx.voice_client.move_to(voice_channel)
      await ctx.send(f"Connected to {voice_channel}")
    else:
      print("Ok2")
      await ctx.voice_channel.connect()
      await ctx.send(f"Connected to {voice_channel}")

  @commands.command()
  async def stop(self,ctx):
    await ctx.voice_client.stop()
    await ctx.send("Song Stop")
  
  @commands.command()
  async def leave(self,ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("Channel Leave")
  
  @commands.command()
  async def pause(self,ctx):
      await ctx.voice_client.pause()
      await ctx.send("Song Paused")

  @commands.command()
  async def resume(self,ctx):
      await ctx.voice_client.resume()
      await ctx.send("Song Resume")

  @commands.command()
  async def play(self,ctx, url):
      if ctx.author.voice is None:
        await ctx.send("Enter in a voice channel and type `:3join` before play music")
      value = db.get(f"Url-{ctx.author.id}")
      if value is None:
        db[f"Url-{ctx.author.id}"] = f"{url}"
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url,download = False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          vc.play(source)
          await ctx.send("Now Playing")
      else:
        del db[f"Url-{ctx.author.id}"]
        db[f"Url-{ctx.author.id}"] = f"{url}"
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url,download = False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          vc.play(source)
          await ctx.send("Now Playing")

  @commands.command()
  async def queue1(self, ctx, url):
    value = db.get(f"Queue{ctx.author.id}")
    if value is not None:
      await ctx.send("A song is already in queue")
    else:
      db[f"Queue{ctx.author.id}"] = f"{url}"
      await ctx.send("Song in queue")

  @commands.command()
  async def reset_queue(self, ctx):
    value = db.get(f"Queue{ctx.author.id}")
    if value is not None:
      del db[f"Queue{ctx.author.id}"]
      await ctx.send("Queue Reset")
    else:
      await ctx.send("No song in queue")
		
  @commands.command()
  async def loop(self, ctx):
    url = db.get(f"Url-{ctx.author.id}")
    if url is not None:
      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
      YDL_OPTIONS = {'format':'bestaudio'}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url,download = False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
        vc.play(source)
        await ctx.send("Now Playing")
    else:
      await ctx.send("No Sound Played Recently")

  @commands.command()
  async def yourbored(self, ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info("https://www.youtube.com/watch?v=VBlFHuCzPgY",download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)
      await ctx.send("Now Playing YourBored :3")

  @commands.command()
  async def radio(self,ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    vc = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("http://stream.radioparadise.com",**FFMPEG_OPTIONS)
    vc.play(source)
    await ctx.send("Now Playing Radio")

  @commands.command()
  async def rock(self,ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    vc = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("http://stream.radioparadise.com/rock-320",**FFMPEG_OPTIONS)
    vc.play(source)
    await ctx.send("Now Playing Rock Radio")
 
  @commands.command()
  async def world(self,ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    vc = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("https://stream.radioparadise.com/world-etc-320",**FFMPEG_OPTIONS)
    vc.play(source)
    await ctx.send("Now Playing World Radio")

  @commands.command()
  async def mellow(self,ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    vc = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("https://stream.radioparadise.com/mellow-320",**FFMPEG_OPTIONS)
    vc.play(source)
    await ctx.send("Now Playing Mellow Radio")

  @commands.command()
  async def nrj(self,ctx):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    vc = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("https://scdn.nrjaudio.fm/fr/30001/mp3_128.mp3?cdn_path=audio_lbs10&access_token=74ca70b405b2441491f7efb558ab4f0c",**FFMPEG_OPTIONS)
    vc.play(source)
    await ctx.send("Now Playing NRJ")

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def purge(self, ctx):
    await ctx.channel.purge(limit=10000)
    embed = discord.Embed(title=f"{ctx.channel.name} Purged Successfully", description=f"Carried-out by {ctx.author.name}\nThis message is deleted in 10 seconds", color=0xd0c0e9)
    embed.set_thumbnail(url="https://i.ibb.co/f1DKR81/clipart1795386.png")
    await ctx.send(embed=embed, delete_after=10)

  @play.error
  async def play_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "❗You need to paste a Youtube Url"
        )


  @commands.command()
  async def verif(self, ctx):
    guild = ctx.guild
    value2 = discord.utils.get(ctx.guild.channels, name="🔑・verification")
    value = discord.utils.get(ctx.guild.roles, name="Unverified")
    if value is None:
        overwrites = {
          ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True)
        }
        perms = discord.Permissions(view_channel=False)
        await guild.create_role(name="Unverified", permissions=perms)
        if value2 is None:
          channels = ctx.guild.channels
          for channel in channels:
            if isinstance(channel, discord.TextChannel):
              await channel.set_permissions(value, send_messages=False)
          overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=True),
            value: discord.PermissionOverwrite(view_channel=False)
          }
          await ctx.guild.create_text_channel('🔑・verification')
          for value2 in channels:
            if isinstance(channel, discord.TextChannel):
              await channel.set_permissions(value, send_messages=True)
          db[f"Captcha-{ctx.guild.id}"] = f"Enabled"
    else:
      pass