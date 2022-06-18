import discord
import discord.utils
import random
import requests
from random import choice
from discord.ext import commands

class gif(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  # THIS COG IS IN DEV TO BE UPDATED
  # Old Gif Commands that work but i don't use it

  # Anime Gif
  @commands.command()
  async def bang_random(self, ctx):
    anime = [
    "https://c.tenor.com/Am61DGzxpGoAAAAC/anime-laughing.gif",
    "https://c.tenor.com/WxLl5mre8pYAAAAd/anime-kill.gif",
    "https://c.tenor.com/UQlr7hnljWoAAAAC/bang-anime.gif",
    "https://c.tenor.com/pvcrnmguRUgAAAAC/bang-anime.gif","https://c.tenor.com/iMtcqbBzc5sAAAAC/anime-shooting.gif",
    "https://c.tenor.com/AeOgMT85jokAAAAC/assasination-classrom-gun.gif"]
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** bangs **{user.mention}** 🔥",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(anime))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def shocked(self, ctx):
    animeshocked = [
    "https://c.tenor.com/YFPEZYpnUn0AAAAC/anime-scared.gif",
    "https://c.tenor.com/8q6Jwj0as2wAAAAC/killua-huh.gif",
    "https://c.tenor.com/mYpbBCObcqkAAAAC/dr-stone-senku.gif",
    "https://c.tenor.com/zaA5Pjj5uLEAAAAC/what-anime.gif",
    "https://c.tenor.com/KZQxXNyRXJoAAAAC/anime-girl.gif"]
    animekiss = requests.get("https://nayobot.moe/api/shocked.html")
    print("Very Nice")
    choice = animekiss.json
    print("Nice")
    img = choice['Img']
    embed = discord.Embed(description=f"**{ctx.author.name}** is shocked 😱",
                          color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  async def angry(self, ctx):
    animeschoked = [
    "https://c.tenor.com/-611TwvdxQcAAAAd/anime-zenitsu.gif",
    "https://c.tenor.com/rzDkOlEDun0AAAAC/hayase-nagatoro-nagatoro-angry.gif",
    "https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif",
    "https://c.tenor.com/wtSs_VCHYmEAAAAC/noela-angry.gif","https://c.tenor.com/ikKAd57zDEwAAAAd/anime-mad.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** is angry 😡",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def die(self, ctx):
    animeschoked = [
    "https://c.tenor.com/9Ql_VyYvMZkAAAAC/anime-sleeping.gif",
    "https://c.tenor.com/mV2LIwcx7nEAAAAC/kiznaiver-katsuhira-agata.gif",
    "https://c.tenor.com/fT_gwZ3_Y7EAAAAC/tired-dead.gif",
    "https://c.tenor.com/-FEJjpJsXWgAAAAC/langa-hasegawa.gif","https://c.tenor.com/9mbCMwHre2IAAAAC/another-gore.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** dies 😵",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  async def blush(self, ctx):
    animeschoked = [
    "https://c.tenor.com/T51BLj_Cj8cAAAAC/blush.gif",
    "https://c.tenor.com/d3AEjdxSfawAAAAC/anime-blush.gif",
    "https://c.tenor.com/bOZ6nfLuKHIAAAAC/hachioji-naoto-naoto-blushing.gif",
    "https://c.tenor.com/qYS0n4QWxd4AAAAC/blush-anime.gif","https://c.tenor.com/bEes0xCurvMAAAAC/anime-blush-dizzy.gif","https://c.tenor.com/wLBd6pVxFpwAAAAC/oh-no-red-faced.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** blushs 😳",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)
	

  @commands.command()
  async def wink(self, ctx, user):
    animeschoked = [
    "https://c.tenor.com/0H8pVlaAy-MAAAAC/chika-fujiwara-kaguya-sama-love-is-war.gif",
    "https://c.tenor.com/2pcB6d1KPEwAAAAC/naruto-naruto-shippuden.gif",
    "https://c.tenor.com/qD-4Fe8CjA8AAAAC/power-peace.gif",
    "https://c.tenor.com/ys1djiyO5nYAAAAC/yato-noragami.gif","https://c.tenor.com/TloDypFZSuAAAAAC/taiga-peace.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** winks at **{user}** 😉",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def dab(self, ctx):
    animeschoked = [
    "https://c.tenor.com/C5riNZAzrksAAAAC/dab-anime.gif",
    "https://c.tenor.com/cbOd_mc2DvIAAAAC/chika-fujiwara-dance.gif",
    "https://c.tenor.com/q045q-y_NdQAAAAC/ini-miney-ace-attorney.gif",
    "https://c.tenor.com/w5Oop53gtA8AAAAC/dab-dabbing.gif","https://c.tenor.com/hLF5hGCWoXAAAAAC/dab-megumin.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** dabs 😎",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animeschoked))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def happy(self, ctx):
    animehappy = [
    "https://c.tenor.com/A8Xon5cq5sQAAAAC/bell-cranel-dan-machi.gif",
    "https://c.tenor.com/XCCF7Z8SaCAAAAAC/anime-happy.gif",
    "https://c.tenor.com/no4g6AmZh-kAAAAC/blush-excited.gif",
    "https://c.tenor.com/v3MiwKcqKHAAAAAd/sagiri-izumi-sagiri.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** is happy 😋",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animehappy))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def sexy(self, ctx):
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
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def cry(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/cry")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(description=f"**{ctx.author.name}** is crying 😭", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def hello(self, ctx, user):
    animesalut = [
    "https://c.tenor.com/Ch4VFEjuI7IAAAAC/anime-boy.gif",
    "https://c.tenor.com/S6Kxbixp1yUAAAAC/gakkou-gurashi-hello.gif",
    "https://c.tenor.com/n1szpPp19d0AAAAC/yuigahama-yahallo.gif",
    "https://c.tenor.com/thNxDWlG1EcAAAAd/killua-zoldyck-anime.gif"]
    embed = discord.Embed(
        description=f"**{ctx.author.name}** say hello to **{user}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animesalut))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def kiss(self, ctx, user):
    animekiss = requests.get("http://api.nekos.fun:8080/api/kiss")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** kiss **{user}** 😘",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def kiss_random(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/kiss")
    choice = animekiss.json()
    img = choice['image']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** kiss **{user.mention}** 😘",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def hug(self, ctx, user):
    huglink = requests.get("http://api.nekos.fun:8080/api/hug")
    choice = huglink.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** hugs **{user}** 🤗",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def dance(self, ctx):
    animedance = [
    "https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif",
    "https://c.tenor.com/THPe8NNBFAAAAAAC/anime-naruto.gif",
    "https://c.tenor.com/Lkyf9b8203YAAAAC/dragon-maid-kanna-fite.gif",
    "https://c.tenor.com/ysPVGNGfWBcAAAAC/anime-dance-happy.gif",
    "https://c.tenor.com/R0PPU-xQlHAAAAAC/anime.gif","https://cdn.discordapp.com/attachments/946495223389904946/947950076846800946/dance-anime.gif","https://cdn.discordapp.com/attachments/946495223389904946/947950219537043526/undefined_-_Imgur.gif","https://cdn.discordapp.com/attachments/946495223389904946/947949835514949632/dancing-anime-gif-15.gif"]
    embed = discord.Embed(description=f"**{ctx.author.name}** dance 💃",
                          color=0xd0c0e9)
    embed.set_image(url=random.choice(animedance))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def dance_random(self, ctx):
    animedance = [
    "https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif",
    "https://c.tenor.com/THPe8NNBFAAAAAAC/anime-naruto.gif",
    "https://c.tenor.com/Lkyf9b8203YAAAAC/dragon-maid-kanna-fite.gif",
    "https://c.tenor.com/ysPVGNGfWBcAAAAC/anime-dance-happy.gif",
    "https://c.tenor.com/R0PPU-xQlHAAAAAC/anime.gif"]
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** do a dance to **{user.mention}** 🤗",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animedance))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)



  @commands.command()
  async def laugh(self, ctx, user):
    huglink = requests.get("http://api.nekos.fun:8080/api/laugh")
    choice = huglink.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** laughs at **{user}** 😂",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def poke(self, ctx, user):
    huglink = requests.get("http://api.nekos.fun:8080/api/poke")
    choice = huglink.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** pokes **{user}** 👉",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def laugh_random(self, ctx):
    huglink = requests.get("http://api.nekos.fun:8080/api/laugh")
    choice = huglink.json()
    img = choice['image']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** laughs at **{user.mention}** 😂",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def hello_random(self, ctx):
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
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def hug_random(self, ctx):
    huglink = requests.get("http://api.nekos.fun:8080/api/hug")
    choice = huglink.json()
    img = choice['image']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** hugs **{user.mention}** 🤗",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def slap_random(self, ctx):
    r = requests.get("http://api.nekos.fun:8080/api/slap")
    choice = r.json()
    img = choice['image']
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=
        f"**{ctx.author.name}** slaps **{user.mention}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def slap(self, ctx, user):
    r = requests.get("http://api.nekos.fun:8080/api/slap")
    choice = r.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"**{ctx.author.name}** slaps **{user}** 👋",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def eat(self, ctx, user):
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
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def eat_random(self, ctx):
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
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def kill_random(self, ctx):
    animekill = ["https://tenor.com/view/anime-sabagebu-gif-20780498","https://c.tenor.com/Wq-Un4pZq50AAAAC/giant-scissor.gif",
    "https://c.tenor.com/moYUm6Q6n34AAAAC/anime-sabagebu.gif",
    "https://c.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif",
    "https://c.tenor.com/t-0fYVPgg1YAAAAC/pink-hair-anime.gif",
    "https://c.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif",
    "https://c.tenor.com/wOCOTBGZJyEAAAAC/chikku-neesan-girl-hit-wall.gif"]
    user = choice(ctx.guild.members)
    embed = discord.Embed(
        description=f"**{ctx.author.name}** killed **{user.mention}** 💀",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animekill))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def kill(self, ctx, user):
    animekill = ["https://c.tenor.com/moYUm6Q6n34AAAAC/anime-sabagebu.gif","https://c.tenor.com/Wq-Un4pZq50AAAAC/giant-scissor.gif",
    "https://c.tenor.com/J8dHU1zVoRsAAAAC/anime-sabagebu.gif",
    "https://c.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif",
    "https://c.tenor.com/t-0fYVPgg1YAAAAC/pink-hair-anime.gif",
    "https://c.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif",
    "https://c.tenor.com/wOCOTBGZJyEAAAAC/chikku-neesan-girl-hit-wall.gif"]
    embed = discord.Embed(
        description=f"**{ctx.author.name}** killed **{user}** 💀",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(animekill))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)


  @commands.command()
  async def bang(self, ctx, user):
    anime = [
    "https://c.tenor.com/Am61DGzxpGoAAAAC/anime-laughing.gif",
    "https://c.tenor.com/WxLl5mre8pYAAAAd/anime-kill.gif",
    "https://c.tenor.com/UQlr7hnljWoAAAAC/bang-anime.gif",
    "https://c.tenor.com/pvcrnmguRUgAAAAC/bang-anime.gif",
    "https://c.tenor.com/WvSUs_s7IpkAAAAC/l-lawliet-death-note.gif"]
    embed = discord.Embed(
        description=f"**{ctx.author.name}** bangs **{user}** 🔥",
        color=0xd0c0e9)
    embed.set_image(url=random.choice(anime))
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  async def pat(self, ctx, user):
      animekiss = requests.get("http://api.nekos.fun:8080/api/pat")
      choice = animekiss.json()
      img = choice['image']
      embed = discord.Embed(
        description=f"**{ctx.author.name}** pats **{user}** 🥺",
        color=0xd0c0e9)
      embed.set_image(url=random.choice(anime))
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
      await ctx.send(embed=embed)


  @commands.command()
  async def disgusted(self, ctx):
      anime = [
      "https://c.tenor.com/3ku_QVMm70cAAAAC/bad-joke-tomioka.gif",
      "https://c.tenor.com/hQzWeTw4IpcAAAAC/sip-anime.gif",
      "hhttps://c.tenor.com/p3OYL7KvphQAAAAC/demon-slayer-tanjiro.gif",
      "https://c.tenor.com/UrxDAmsiBPcAAAAC/disgusted-no.gif",
      "https://c.tenor.com/6-PsJPfkwSoAAAAC/maika-blend-s.gif"]
      embed = discord.Embed(
        description=f"**{ctx.author.name}** is disgusted 🤮",
        color=0xd0c0e9)
      embed.set_image(url=random.choice(anime))
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
      await ctx.send(embed=embed)

  @commands.command()
  async def meme(self, ctx):
    meme = ["https://c.tenor.com/btMXU0Gmb_gAAAAC/yeet.gif","https://c.tenor.com/Cbm8FdN4tbAAAAAC/sailor-moon-suit-old-man.gif","https://c.tenor.com/6NEZpt9dEpkAAAAC/anime-dark.gif","https://c.tenor.com/D6ZdzLuQN_kAAAAC/chunibyo.gif","https://c.tenor.com/NZ81KxrwImQAAAAd/anime-nezuko.gif","https://c.tenor.com/oqmSdq-jzdIAAAAC/pug.gif","https://c.tenor.com/9_J-Hk_7SZ8AAAAC/wifi-down.gif","https://c.tenor.com/TdqhucWI5sEAAAAC/meme.gif","https://c.tenor.com/-m1mRsuTe-oAAAAC/anime-smash.gif","https://c.tenor.com/cWHJLNx-NmYAAAAC/life-kick.gif","https://c.tenor.com/BW0Y6l-U_7UAAAAC/anime-anime-opening.gif"]
    choice = random.choice(meme)
    embed = discord.Embed(
        description=f"**Random Anime Meme** 🤣\n[Click Here if the image does not appear]({choice})",
        color=0xd0c0e9)
    embed.set_image(url=choice)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def hentai(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/hentai")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Hentai Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def blowjob(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/blowjob")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"BlowJob Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def pussy(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/pussy")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Pussy Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def boobs(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/boobs")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
      description=f"Boobs Random Image 🔞\n[Click Here if the image does not appear]({img})", color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def yaoi(self, ctx):
    hunterimg = ["https://imgur.com/1JRW8YV.png","https://imgur.com/zMtWJnc.png","https://imgur.com/auuIKQ2.jpg","https://imgur.com/ERzkMIU.jpg","https://imgur.com/lUWjHb6.jpg","https://i.imgur.com/kM7QM5N.gif","https://i.imgur.com/Y7vgl2O.png","https://i.imgur.com/gu3atn4.png","https://i.imgur.com/aRvOPEf.gif","https://imgur.com/MPY2vHV.jpg","https://imgur.com/UUnWphB.png","https://imgur.com/ctu2yVL.png","https://imgur.com/BHbDnC5.png","https://i.imgur.com/DcTAvzi.jpg","https://imgur.com/glOhJQ5.jpg"]
    embed = discord.Embed(
      description=f"Yaoi Random Image 🔞\n[Click Here if the image does not appear]({hunterimg})", color=0xd0c0e9)
    embed.set_image(url=hunterimg)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

	
  @commands.command()
  @commands.is_nsfw()
  async def lewd(self, ctx):
      animekiss = requests.get("http://api.nekos.fun:8080/api/lewd")
      choice = animekiss.json()
      img = choice['image']
      embed = discord.Embed(
        description=f"Lewd Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
      embed.set_image(url=img)
      embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
      await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def yuri(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/lesbian")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"Yuri Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_nsfw()
  async def cum(self, ctx):
    animekiss = requests.get("http://api.nekos.fun:8080/api/cum")
    choice = animekiss.json()
    img = choice['image']
    embed = discord.Embed(
        description=f"Cum Random Image 🔞\n[Click Here if the image does not appear]({img})",
        color=0xd0c0e9)
    embed.set_image(url=img)
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/0SLdaEN.png")
    await ctx.send(embed=embed)