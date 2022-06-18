import discord
import discord.utils
import asyncio
from discord_slash import SlashCommand, ButtonStyle
from discord.ext import commands
from discord_slash.utils.manage_components import *

class admin(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  # THIS COG IS IN DEV TO BE UPDATED
  # Old Admin Commands that work but i don't use it
		
  # Create Role
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def role(self, ctx, *, role_name):
    guild = ctx.guild
    await guild.create_role(name=f"{role_name}")
    embed = discord.Embed(title="Created Role", description=f'Role : **{role_name}**', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)

  # Delete Rôle
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def deleterole(self, ctx, role_name):
    role = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role.delete()
    embed = discord.Embed(title="Delete Role", description=f'Role : **{role_name}**', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)


  # Show Rôles
  @commands.command(pass_context=True)
  @commands.has_permissions(manage_guild=True)
  async def showroles(self, ctx):
    guild = ctx.guild
    roles = [role for role in guild.roles if role != ctx.guild.default_role]
    roles = roles[::-1]
    embed = discord.Embed(title=f"📝 Roles of {ctx.guild.name}", description=f" ".join([role.mention + '\n' for role in roles]), color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/kaRCm9ELxKgAAAAC/menhera-chan-chibi.gif")
    await ctx.send(embed=embed)


  # Change Nickname
  @commands.command(pass_context=True)
  @commands.has_permissions(manage_nicknames=True)
  async def nickname(self, ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(title="🔁 Changed Nickname", description=f'New Nickname for : {member.mention}', color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)


  # Text Channel
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def textchannel(self, ctx, *, channel_name):
    guild = ctx.message.guild
    await guild.create_text_channel(channel_name)
    embed = discord.Embed(title="Textual Channel Created", description = f"**Name** : {channel_name}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)


  # Voice Channel
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def voicechannel(self, ctx, *, channel_name):
    guild = ctx.message.guild
    await guild.create_voice_channel(channel_name)
    embed = discord.Embed(title="Voice Channel Created", description = f"**Name** : {channel_name}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)


  # Delete Category
  @commands.command(pass_context=True)
  @commands.has_permissions(manage_guild=True)
  async def delcategory(self, ctx, category: discord.CategoryChannel):
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

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def warn(self, ctx, member: discord.Member):
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
            print('Nice')
            cursor.execute(f"INSERT INTO `Warn`(`ID`, `WARNS`) VALUES ('{val}','1')")
            mydb.commit()
            embed = discord.Embed(title="Member Warn 🔨", description=f"{member.mention} has been warn\nHe receive a warn private message", color=0xd0c0e9)
            embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(title=f"{ctx.guild.name} Warn ⚠️", description=f"You receive a warn from **{ctx.guild.name}**\nFor a bad attitude in this server\nPlease keep a good behavior !", color=0xd0c0e9)
            embed2.set_thumbnail(url="https://i.ibb.co/HYhhSPf/Warning-PNG-Free-Image.png")
            await member.send(embed=embed2)
    
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def warnlist(self, ctx, member: discord.User):
      val = f"{member.id}-{ctx.guild.id}"
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

  @commands.command(aliase="reset warns")
  @commands.has_permissions(manage_guild=True)
  async def resetwarns(self, ctx, member: discord.User):
    val = f"{member.id}-{ctx.guild.id}"
    cursor.execute(f"SELECT * FROM `Warn` WHERE `ID` = '{val}'")
    value = cursor.fetchone()
    if value is not None:
      cursor.execute(f"DELETE FROM `Warn` WHERE `ID` = '{val}'")
      mydb.commit()
      await ctx.send(f"The warnings of {member.mention} have been reset")
    else:
      await ctx.send(f"{member.name} don't have warns actually")

  # Create Category
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def category(self, ctx, category_name):
    guild = ctx.message.guild
    await ctx.guild.create_category(category_name)
    embed = discord.Embed(title="Category Created", description = f"**Name** : {category_name}", color = 0xd0c0e9)
    await ctx.send(embed=embed)


  # Delete Channel
  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def deletechannel(self, ctx, channel: discord.TextChannel):
    guild = ctx.guild
    if not channel:
      await ctx.send("{channel} don't exist")
    else:
      await channel.delete()
      embed = discord.Embed(title="Channel Deleted", description = f"**Name** : {channel}", color = 0xd0c0e9)
      embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
      await ctx.send(embed=embed)


  # Commande de suppression de message (Tous les messages)
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clearall(self, ctx):
    messages = await ctx.channel.history().flatten()
    for message in messages:
        await message.delete()


  # Commande de suppression de message (nombre personnalisable)
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, nombres: int):
    messages = await ctx.channel.history(limit=nombres + 1).flatten()
    for message in messages:
      await message.delete()  

  
  


  @commands.Cog.listener(name='on_command')
  async def print(self, ctx):
    user = ctx.author
    command = ctx.command
    channel = discord.utils.get(ctx.guild.channels, name="📦・nayo-logs")
    if channel is None:
      pass
    else:
      await channel.send(f"➥ **{command}** command carried-out by **{user}**")


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def logs(self, ctx):
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

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def clone(self, ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel is not None:
        await existing_channel.clone(reason="Channel Clone Successfully")
        await existing_channel.delete()
        await ctx.send("Channel Clone Successfully")
    else:
        await ctx.send(f'No channel named **{channel_name}** was found')

  @commands.command()
  async def voicecount(self, ctx):
    guild = ctx.guild
    channel = discord.utils.get(guild.channels, name = f'👤・Member(s) : {guild.member_count}')
    if channel is None:
      overwrites = {
        guild.default_role: discord.PermissionOverwrite(connect=False),
        guild.me: discord.PermissionOverwrite(connect=False)
      }
      await guild.create_voice_channel(f"👤・Member(s) : {guild.member_count}", overwrites=overwrites)
    else:
      await ctx.send(f'👤・Member(s) : {guild.member_count} already exist in this server')
		

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    embed = discord.Embed(title="Channel Locked 🔒", color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    embed = discord.Embed(title="Channel UnLocked 🔓", color=0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(embed=embed)
      
  # Commande d'expulsion d'un membre
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.message.add_reaction("✅")
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="Member Kick 🔨", description=f"Member : {user.mention}\nReason : {reason}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def mpsupport(self, ctx, user: discord.User, arg):
    messages = await ctx.channel.history(limit=1).flatten()
    for message in messages:
      await message.delete()
    await user.send(arg)

		
  # Commande de bannissement d'un membre
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="No Reason"):
    reason = " ".join(reason)
    await ctx.guild.ban(member, reason=reason)
    embed = discord.Embed(title="Member Ban 🔨", description=f"Member : {member.mention}\nReason : {reason}", color = 0xd0c0e9)
    embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
    await ctx.send(embed=embed)

  
  # Commande Unban
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
		
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        embed = discord.Embed(title="Member UnBan 🔨", description=f"Member : {user.mention}", color=0xd0c0e9)
        embed.set_thumbnail(url="https://c.tenor.com/g3TAB8h_QgwAAAAC/good-anime.gif")
        await ctx.send(embed=embed)