import discord
import discord.utils
import PIL
from discord_slash import SlashCommand
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw, ImageFont
import random, datetime, asyncio
from random import choice
from discord.ext import commands

class fun(commands.Cog):
  

  # THIS COG IS IN DEV TO BE UPDATED
  # Old Commands that work but i don't use it

  player1 = ""
  player2 = ""
  turn = ""
  gameOver = True
  board = []

  def __init__(self, bot):
	  self.bot = bot

  @commands.command()
  @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
  async def tictactoe(self, ctx, player1: discord.Member, player2: discord.Member):
    #global count
    #global player1
    #global player2
    #global turn
    #global gameOver

    if self.gameOver:
        #global board
        self.board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        self.turn = ""
        self.gameOver = False
        self.count = 0

        self.player1 = player1
        self.player2 = player2


        line = ""
        for x in range(len(self.board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + self.board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + self.board[x]


        num = random.randint(1, 2)
        if num == 1:
            self.turn = self.player1
            await ctx.send("It's <@" + str(self.player1.id) + "> turn")
        elif num == 2:
            self.turn = self.player2
            await ctx.send("It's <@" + str(self.player2.id) + "> turn")
    else:
        await ctx.send("A game is in progress")


  @commands.command()
  @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
  async def case(self, ctx, pos: int):
    winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    def checkWinner(winningConditions, mark):
      #global gameOver
      for condition in winningConditions:
            if self.board[condition[0]] == mark and self.board[
                condition[1]] == mark and self.board[condition[2]] == mark:
                self.gameOver = True

    #global turn
    #global player1
    #global player2
    #global board
    #global count
    #global gameOver

    if not self.gameOver:
        mark = ""
        if self.turn == ctx.author:
            if self.turn == self.player1:
                mark = ":regional_indicator_x:"
            elif self.turn == self.player2:
                mark = ":o2:"
            if 0 < pos < 10 and self.board[pos - 1] == ":white_large_square:":
                self.board[pos - 1] = mark
                self.count += 1


                line = ""
                for x in range(len(self.board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + self.board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + self.board[x]

                checkWinner(winningConditions, mark)
                if self.gameOver == True:
                    await ctx.send(mark + " win 🏆")
                elif self.count >= 9:
                    self.gameOver = True
                    await ctx.send("No Winner")


                if self.turn == self.player1:
                    self.turn = self.player2
                elif self.turn == self.player2:
                    self.turn = self.player1
            else:
                await ctx.send(
                    "You must enter a number between 1 and 9 (integers) and place your mark in an empty box"
                )
        else:
            await ctx.send("It's not your turn")
    else:
        await ctx.send("Start a new game with >tictactoe")
    
  @tictactoe.error
  async def tictactoe_error(self, ctx, error):
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Wait {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Mention two players")
    elif isinstance(error, commands.BadArgument):
      await ctx.send("Mention two players with the @")

  @case.error
  async def place_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Enter a correct position")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Enter a whole number")

  # Commande Fun (Répète une phrase en chinois)
  @commands.command()
  async def chinese(self, ctx, *text):
    chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char.lower()) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send(" ".join(chineseText))
 
  # Pile ou Face
  @commands.command()
  async def headsortails(self, ctx):
    liste = ["Heads", "Tails"]
    choix = random.choice(liste)
    embed = discord.Embed(title=f"🪙 {choix}", description=f"You came across\n**{choix}** this time ", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/514/PNG/512/coin-euro_icon-icons.com_51032.png")
    await ctx.send(embed=embed)

  @commands.command()
  async def dice(self, ctx):
    a = ["Yes", "yes"]
    b = ["No", "no"]
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send('Would you like a double throw ?')
    msg = await self.bot.wait_for('message', check=check)

    if msg.content in a:
      resultat = ["1", "2", "3", "4", "5", "6"]
      resultat2 = ["1", "2", "3", "4", "5", "6"]
      lancer = random.choice(resultat)
      lancer2 = random.choice(resultat2)
      embed = discord.Embed(title=f"🎲 Dice Throw", description=f"You came across **{lancer}** and **{lancer2}**", color=0xd0c0e9)
      embed.set_thumbnail(url="https://assets.stickpng.com/images/580b585b2edbce24c47b246f.png")
      await ctx.send(embed=embed)

    if msg.content in b:
      resultat = ["1", "2", "3", "4", "5", "6"]
      lancer = random.choice(resultat)
      embed = discord.Embed(title=f"🎲 Dice Throw", description=f"You came across **{lancer}**", color=0xd0c0e9)
      embed.set_thumbnail(url="https://assets.stickpng.com/images/580b585b2edbce24c47b246f.png")
      await ctx.send(embed=embed)

  @commands.command()
  async def chifumi(self, ctx):
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      PPC = ["Rock", "Paper", "Scissors"]
      a = ["Rock"]
      b = ["Paper"]
      c = ["Scissors"]
  
      await ctx.send("Type **Rock**, **Paper** or **Scissors**")
      msg = await self.bot.wait_for('message', check=check)
      choix = random.choice(PPC)
      if choix in a:
        embed = discord.Embed(color=0xd0c0e9)
        embed.set_thumbnail(url="https://topemojis.com/images/android-11/stone.png")
        await asyncio.sleep(1)
        n = await ctx.send(embed=embed)
        if msg.content in a:
          await msg.add_reaction("❌")
          await n.add_reaction("❌")
        if msg.content in b:
          await msg.add_reaction("🏆")
          await n.add_reaction("❌")
        if msg.content in c:
          await msg.add_reaction("❌")
          await n.add_reaction("🏆")

      if choix in b:
        embed = discord.Embed(color=0xd0c0e9)
        embed.set_thumbnail(url="https://images.emojiterra.com/twitter/v13.1/512px/1f4c3.png")
        await asyncio.sleep(1)
        n = await ctx.send(embed=embed)
        if msg.content in a:
          await msg.add_reaction("❌")
          await n.add_reaction("🏆")
        if msg.content in b:
          await msg.add_reaction("❌")
          await n.add_reaction("❌")
        if msg.content in c:
          await msg.add_reaction("🏆")
          await n.add_reaction("❌")


      if choix in c:
        embed = discord.Embed(color=0xd0c0e9)
        embed.set_thumbnail(url="https://www.pngmart.com/files/1/Cartoon-Scissor-PNG.png")
        await asyncio.sleep(1)
        n = await ctx.send(embed=embed)
        if msg.content in a:
          await msg.add_reaction("🏆")
          await n.add_reaction("❌")
        if msg.content in b:
          await msg.add_reaction("❌")
          await n.add_reaction("🏆")
        if msg.content in c:
          await msg.add_reaction("❌")
          await n.add_reaction("❌")

  @commands.command()
  async def rategay(self, ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Gay Rate 🌈", description=f"You are gay at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)
	
  @commands.command()
  async def ratecool(self, ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Cool Rate 😎", description=f"You are cool at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)

  @commands.command()
  async def rategeek(self, ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
    value = random.randrange(101)
    embed = discord.Embed(title="Geek Rate  👾", description=f"You are a geek at **{value}%** {member.mention}", color=0xd0c0e9)
    await ctx.send(embed=embed)

  @commands.command()
  async def ratelove(self, ctx, member: discord.Member, p2: discord.Member):
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
	
  @commands.command()
  async def ratelove_random(self, ctx):
    member = choice(ctx.guild.members)
    p2 = choice(ctx.guild.members)
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
		
  @commands.command(aliase="8ball")
  async def eightball(self, ctx, *, question):
    liste = ["Maybe, it's work","Hmm, i think No","Probably","Sure","Absolutely not","Yes","No","Perhaps","I cannot predict now","Of course","It's a big No","Negative","Positive","As i see it's a Yes","I predict that's a No","Hmm, i don't know","Hmm that's a Yes and a No"]
    choice = random.choice(liste)
    embed = discord.Embed(title="🎱 Magic 8 Ball", description=f"Question : **{question}**\nAnswer : **{choice}**", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://i.ibb.co/nbHvbPD/png-transparent-magic-8-ball-eight-ball-billiards-billiard-balls-ball-sphere-sports-pool.png")
    await ctx.send(embed=embed)

# Embed personnalisé
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def embed(self, ctx, salon: discord.TextChannel):
    a = ["yes", "Yes"]
    b = ["no", "No"]

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
			
    channel = discord.utils.get(ctx.guild.text_channels,
                                name=f"{salon}")
    await ctx.send('Enter your title')
    title = await self.bot.wait_for('message', check=check)

    await ctx.send('Enter your description')
    desc = await self.bot.wait_for('message', check=check)

    await ctx.send(
        "Would you like to add a footer ?"
    )
    msg = await self.bot.wait_for('message', check=check)
    if msg.content in a:
        await ctx.send(
            'Enter your footer')
        cfooter = await self.bot.wait_for('message', check=check)
        await ctx.send(
            "Would you like to add a main image ?"
        )
        msg2 = await self.bot.wait_for('message', check=check)
        if msg2.content in a:
            await ctx.send(
                'Enter a image url (Respond Fastly')
            cimage = await self.bot.wait_for('message', check=check)
            await ctx.send(
                "Would you like to add a thumbnail ?"
            )
            msg4 = await self.bot.wait_for('message', check=check)
            if msg4.content in a:
                await ctx.send(
                    "Enter a image url"
                )
                cthumbnail = await self.bot.wait_for('message', check=check)
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_footer(text=f"{cfooter.content}")
                embed.set_image(url=f"{cimage.content}")
                embed.set_thumbnail(url=f"{cthumbnail.content}")
                await channel.send(embed=embed)
            if msg4.content in b:
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_footer(text=f"{cfooter.content}")
                embed.set_image(url=f"{cimage.content}")
                await channel.send(embed=embed)
        if msg2.content in b:
            await ctx.send(
                "Would you like to add a thumbnail ?"
            )
            msg5 = await self.bot.wait_for('message', check=check)
            if msg5.content in a:
                await ctx.send(
                    "Enter a image url"
                )
                cthumbnail = await self.bot.wait_for('message', check=check)
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_footer(text=f"{cfooter.content}")
                embed.set_thumbnail(url=f"{cthumbnail.content}")
                await channel.send(embed=embed)
            if msg5.content in b:
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_footer(text=f"{cfooter.content}")
                await channel.send(embed=embed)

    if msg.content in b:
        await ctx.send(
            "Would you like to add a main image ?"
        )
        msg3 = await self.bot.wait_for('message', check=check)
        if msg3.content in a:
            await ctx.send(
                'Enter a image url')
            cimage = await self.bot.wait_for('message', check=check)
            await ctx.send(
                "Would you like to add a thumbnail"
            )
            msg6 = await self.bot.wait_for('message', check=check)
            if msg6.content in a:
                await ctx.send(
                    "Enter a image url"
                )
                cthumbnail = await self.bot.wait_for('message', check=check)
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_image(url=f"{cimage.content}")
                embed.set_thumbnail(url=f"{cthumbnail.content}")
                await channel.send(embed=embed)

        if msg3.content in b:
            await ctx.send(
                "Would you like to add a thumbnail ?"
            )
            msg7 = await self.bot.wait_for('message', check=check)
            if msg7.content in a:
                await ctx.send(
                    "Enter a image url"
                )
                cthumbnail = await self.bot.wait_for('message', check=check)
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                embed.set_thumbnail(url=f"{cthumbnail.content}")
                await channel.send(embed=embed)
            if msg7.content in b:
                embed = discord.Embed(title=title.content,
                                      description=desc.content,
                                      color=0xd0c0e9)
                await channel.send(embed=embed)
