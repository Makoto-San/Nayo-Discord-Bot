import discord
import discord.utils
import PIL
import random
import mysql.connector
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw, ImageFont
import PIL.ImageOps
from discord.ext import commands
import psutil

class info(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  # THIS COG IS IN DEV TO BE UPDATED
  # Old Informations Commands that work but i don't use it

  # Commande Stats
  @commands.command()
  @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
  async def serverinfo(self, ctx):
    channel = ctx.channel
    created = ctx.guild.created_at.strftime("%H : %M, %A\n%B %Y")
    botnumber = [bot.mention for bot in ctx.guild.members if bot.bot]
    cowner = str(ctx.guild.owner)
    embed = discord.Embed(title=f"{ctx.guild.name}", colour=0xd0c0e9)
    embed.add_field(name=f"👑 Owner", value=f"{cowner}", inline=True)
    embed.add_field(name="🆔 Guild Id", value=f"`{ctx.guild.id}`", inline = True)
    embed.add_field(
        name="✏️ Created At",
        value=ctx.guild.created_at.__format__('%d %B %Y at %H:%M:%S'), inline=True)
    embed.add_field(name="📝 Description", value=ctx.guild.description, inline=True)
    embed.add_field(name="✅ Verification Level",
                    value=f"`{str(ctx.guild.verification_level)}`", inline=True)
    embed.add_field(name="📜 Number of Roles",
                    value=f"`{len(ctx.guild.roles)}`",
                    inline=True)
    embed.add_field(name="👥 Members", value=f"`{ctx.guild.member_count}`", inline=True)
    embed.add_field(name="📜 Number of Channels",
                    value=f"`{len(ctx.guild.channels)}`",
                    inline=True)
    embed.add_field(name="⌨️ Textuals Channels",
                    value=f"`{len(ctx.guild.text_channels)}`",
                    inline=True)
    embed.add_field(name="🎤 Voice Channels",
                    value=f"`{len(ctx.guild.voice_channels)}`",
                    inline=True)
    embed.add_field(name="🎤 ",
                    value=f"`{len(ctx.guild.voice_channels)}`",
                    inline=True)
    embed.add_field(name="🤖 Bots", value=(', '.join(botnumber)))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


  # Commande d'informations sur le nombre de serveurs
  @commands.command(pass_context=True)
  async def serverscount(self, ctx):
    await ctx.message.delete()
    await ctx.send("**★ Nayo is actually in " + str(len(self.bot.guilds)) + " servers ★**")


  # Affiche le propriétaire du serveur
  @commands.command()
  async def owner(self, ctx):
    gowner = self.bot.get_user(int(ctx.guild.owner.id))
    await ctx.send(
        f"★ The owner of **{ctx.guild.name}** is **{gowner}** ★")


  # Avatar
  @commands.command()
  async def icon(self, ctx, avatar : discord.Member=None):
    embed = discord.Embed(color=0xd0c0e9)
    embed.set_image(url=avatar.avatar_url)
    await ctx.send(embed=embed)


  # Discord Terms
  @commands.command()
  async def discordterms(self, ctx):
    await ctx.send("https://discordapp.com/terms")


  # Règlement
  @commands.command()
  @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
  @commands.has_permissions(manage_guild=True)
  async def regulation(self, ctx):
    embed = discord.Embed(title=f"Server Rules of {ctx.guild.name}",
                          colour=0xd0c0e9)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(
        name=
        "🖇️ In order to maintain a pleasant atmosphere in this server, we will ask you to follow these few rules",
        value=
        "• Your behavior must be respectful of all\n• Pornographic, religious and political content as well as discriminatory remarks are strictly prohibited\n• Your language must remain correct on the whole server\n• The pseudonyms or names of Inappropriate games (pornography, advertising, insults ...) are strictly prohibited\n• You will be held solely responsible for the content you post\n• You are prohibited from recording written and vocal rooms\n• Any use of a client modified to bypass permissions is prohibited and will lead to a permanent ban of this discord server.",
        inline=False)
    embed.add_field(
        name="✏️ In the Written Channels",
        value=
        "• Spam, flood, spoiler and abuse of emojis will be penalized\n• The distribution of private information or photos without the consent of the person is prohibited\n• Advertising is not allowed. This one remains prohibited in Private Messages, discord status, ...\n• It is strictly forbidden to mention without reason the high ranking. Mentions of roles are to be avoided except in cases of necessity. Favor unique mentions.",
        inline=False)
    embed.add_field(
        name="🔊 In the Voice Channels",
        value=
        "• Blowing into your microphone, using a voice modifier or soundboards is prohibited\n• Repetitive change of vocal channel is prohibited\n• Auditory spamming as well as audio screamers are strictly prohibited\n• Music is not allowed only in the channels provided for this purpose. 🎨 In specialized salons",
        inline=False)
    embed.add_field(
        name="📢 Additional Informations",
        value=
        "• You are liable to be sanctioned in the event of a breach of one or more of these rules, without prior warning\n• Moderation reserves the right to sanction you for a reason not specified in the rules if your behavior is inappropriate\n• Only moderators are able to enforce the rules\n• To be aware of the conditions of use of the Discord platform:\nhttps: //discordapp.com/terms",
        inline=False)
    embed.set_image(url="https://i.ibb.co/nkWsgg3/standard-2.gif")
    embed.set_footer(text=ctx.author.name)
    await ctx.message.delete()
    await ctx.send(embed=embed)


  @commands.command()
  async def profile(self, ctx, member : discord.Member=None):
    if not member:
        member = ctx.author
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    #cursor.execute(f"SELECT * FROM `Economy` WHERE `ID` = {ctx.author.id}")
    #results = cursor.fetchone()
    if value is not None:
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
          base = Image.open("base2.png").convert("RGBA")
          background = Image.open("NayoBack.png").convert("RGBA")

          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          name = f"{name[:16]}" if len(name)>16 else name
          nick = f"Alias - {nick[:17]}.." if len(nick)>17 else f"Alias - {nick}"
          value = "X"

          draw = ImageDraw.Draw(base)
          pfp = circle(pfp,(215,215))
          font = ImageFont.truetype("nunito-regular.ttf", 38)
          akafont = ImageFont.truetype("nunito-regular.ttf",30)
          subfont = ImageFont.truetype("nunito-regular.ttf",25)

          draw.text((280,240),name,font = font)
          draw.text((270,315),nick,font = akafont)
          draw.text((60,490),Id,font = subfont)
          draw.text((230,625),value,font = subfont)
          draw.text((405,490),status,font = subfont)
          draw.text((65,770),created_at,font = subfont)
          draw.text((405,770),joined_at,font = subfont)
          base.paste(pfp,(56,158),pfp)

          background.paste(base,(0,0),base)

          with BytesIO() as a:
            background.save(a, "PNG")
            a.seek(0)
            await ctx.send(file = discord.File(a, "profile.png"))
    else:
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
          base = Image.open("base1.png").convert("RGBA")
          background = Image.open("NayoBack.png").convert("RGBA")

          pfp = member.avatar_url_as(size=256)
          data = BytesIO(await pfp.read())
          pfp = Image.open(data).convert("RGBA")
          name = f"{name[:16]}" if len(name)>16 else name
          nick = f"Alias - {nick[:17]}.." if len(nick)>17 else f"Alias - {nick}"

          draw = ImageDraw.Draw(base)
          pfp = circle(pfp,(215,215))
          font = ImageFont.truetype("nunito-regular.ttf", 38)
          akafont = ImageFont.truetype("nunito-regular.ttf",30)
          subfont = ImageFont.truetype("nunito-regular.ttf",25)

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

  @commands.command()
  async def welcome(self, ctx, member: discord.Member):
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
    base = Image.open("BaseWF.png").convert("RGBA")
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("Discord.ttf", 35)
    font2 = ImageFont.truetype("Discord.ttf", 25)
    draw.text((290,140),name,font = font)
    draw.text((290,110),text,font = font2)
    base.paste(pfp,(55,38),pfp)
    with BytesIO() as image_binary:
      base.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

  @commands.command()
  async def farewell(self, ctx, member: discord.Member):
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
    base = Image.open("BaseWF.png").convert("RGBA")
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("Discord.ttf", 35)
    font2 = ImageFont.truetype("Discord.ttf", 25)
    draw.text((290,140),name,font = font)
    draw.text((290,110),text,font = font2)
    base.paste(pfp,(55,38),pfp)
    base.save('fare.png')

  @commands.command()
  async def nayoinfo(self, ctx):
    value = self.bot.latency * 1000
    embed = discord.Embed(title = 'ℹ️ Nayo Informations', description = f'See Nayo Informations\n🏠 **Guilds** : `{str(len(self.bot.guilds))}`\n📶 **Latency** : `{value}Ms`\n🖥️ **CPU Usage** : `{psutil.cpu_percent()}%`\n🗄️ **Memory Usage** : `{psutil.virtual_memory().percent}%`\n💾 **Available Memory** : `{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%`', color=0xd0c0e9)
    await ctx.send(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    value = self.bot.latency * 1000
    if value >= 100 and value <= 300:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Moderately Stable`', color=0xFFA500)
      await ctx.send(embed=embed)
    if value < 100:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Stable`', color=0x008000)
      await ctx.send(embed=embed)
    if value > 300:
      embed = discord.Embed(title = '🏓 Pong', description = f'📶 **Latency of Nayo** : `{value}Ms | Bad`', color=0xFF0000)
      await ctx.send(embed=embed)

  @commands.command()
  async def uptime(self, ctx):
    embed = discord.Embed(title="🕐 Nayo Uptime", description="Nayo Uptime : [Click Here](status.watchbot.app/bot/879082395750531093)", color=0xd0c0e9)
    embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def search(self, ctx, arg):
      embed = discord.Embed(
          title = f'📷 Random Image for : `{arg}`',
          color = 0xd0c0e9)
      embed.set_image(url='https://source.unsplash.com/1920x1080/?{}'.format(arg))            
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

  @commands.command()
  async def wanted(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author

    wanted = Image.open("Wanted.jpg")
    asset = member.avatar_url
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((300,300))
    wanted.paste(pfp, (80,220))
    wanted.save("wanted2.jpg")
    file = discord.File("wanted2.jpg")
    embed = discord.Embed(description=f"{member.mention} is WANTED 🔍", color=0xd0c0e9)
    embed.set_image(url="attachment://wanted2.jpg")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file = file, embed=embed)

  @commands.command()
  async def triggered(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author

    tri = Image.open("Triggered.png")
    tri2 = tri.resize((1050,230))
    asset = member.avatar_url
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((1024,1024))
    pfp.paste(tri2, (0,800))
    pfp.save("triggered2.png")
    file = discord.File("triggered2.png")
    embed = discord.Embed(description=f"{member.mention} is TRIGGERED 🤯", color=0xd0c0e9)
    embed.set_image(url="attachment://triggered2.png")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file=file, embed=embed)

  @commands.command()
  async def invert(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    image = member.avatar_url
    data = BytesIO(await image.read())
    pfp = Image.open(data)
    inverted_image = PIL.ImageOps.invert(pfp)
    inverted_image.save('inverted.png')
    file = discord.File("inverted.png")
    embed = discord.Embed(color=0xd0c0e9)
    embed.set_image(url="attachment://inverted.png")
    await ctx.send(file=file, embed=embed)

  @commands.command()
  async def uacard(self, ctx, member: discord.Member=None):
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
    ua = Image.open("ua.png")
    draw = ImageDraw.Draw(ua)
    ua.paste(pfp, (50,145))
    font2 = ImageFont.truetype("Discord.ttf", 20)
    draw.text((318,208),name,font = font2, fill=(0,0,0))
    draw.text((318,245),idm,font = font2, fill=(0,0,0))
    draw.text((318,140),grade,font = font2, fill=(0,0,0))
    draw.text((318,275),quirk,font = font2, fill=(0,0,0))
    ua.save("uacard.png")
    file = discord.File("uacard.png")
    embed = discord.Embed(description=f"{member.mention}, here your UA Card 💳",color=0xd0c0e9)
    embed.set_image(url="attachment://uacard.png")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file=file, embed=embed)

  @commands.command()
  async def yugioh(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author

    tri = Image.open("YuGiOh.png")
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
    font2 = ImageFont.truetype("light.ttf", 50)
    font = ImageFont.truetype("light.ttf", 30)
    draw.text((70,58),name,font = font2)
    draw.text((72,770),dis2,font = font)
    draw.text((70,810),desc,font = font)
    draw.text((440,930),atk,font = font)
    draw.text((580,930),defe,font = font)
    tri.save("yugioh2.png")
    file = discord.File("yugioh2.png")
    embed = discord.Embed(description=f"{member.mention} is a LIMITED EDITION ⭐", color=0xd0c0e9)
    embed.set_image(url="attachment://yugioh2.png")
    embed.set_footer(text=f"Nayo | {ctx.author.name}", icon_url="https://imgur.com/aHvi2yk.png")
    await ctx.send(file=file, embed=embed)