import discord
import discord.utils
from discord.ext import commands

class anime(commands.Cog):
  def __init__(self, bot):
	  self.bot = bot

  
  # THIS COG IS IN DEV TO BE UPDATED
  # Old Anime Commands that work but i don't use it



  # ------------ Gambling School ------------- #
	
	
  @commands.command()
  async def yumeko_jabami(self, ctx):
    embed2 = discord.Embed(title="Yumeko Jabami 🎰", description="She's a transfer student at Hyakkaou Private Academy and the classmate of Ryota Suzui and Mary Saotome. She is the main character, she is a impulsive gambler who play for the risk", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="17 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Women", inline=True)
    embed2.add_field(name="Height", value="170cm (5'5)", inline=True)
    embed2.add_field(name="Birthday", value="21 February", inline=True)
    embed2.add_field(name="Sexual Identity", value="Bisexual", inline=True)
    embed2.set_image(url="https://pbs.twimg.com/media/D9XS7pIXkAAbIgu?format=jpg&name=small")
    await ctx.send(embed=embed2)

  @commands.command()
  async def mary_saotome(self, ctx):
    embed2 = discord.Embed(title="Mary Saotome 🎰", description="She is the first character in the entire series\nthat challenges Yumeko and loses against her\nShe finally get closer Yumeko and Ryota", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="16 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="162cm (5'4)", inline=True)
    embed2.add_field(name="Birthday", value="8 March", inline=True)
    embed2.add_field(name="Sexual Identity", value="Lesbian", inline=True)
    embed2.set_image(url="https://i.ibb.co/zG5RJzg/removal-ai-tmp-61dda23ed9fb9.png")
    await ctx.send(embed=embed2)


  @commands.command()
  async def ryota_suzui(self, ctx):
    embed2 = discord.Embed(title="Ryota Suzui 🎰", description="He is a former housepet, whom he became after losing to Mary Saotome in a gambling match\nHowever, thanks to Yumeko Jabami, Ryota's debt was repaid after she gave him money as thanks\nbecoming her first friend in Hyakkaou Private Academy.", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="17 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Male", inline = True)
    embed2.add_field(name="Height", value="173cm (5'8)", inline=True)
    embed2.add_field(name="Sexual Identity", value="Hetero Sexual (Probably)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.set_image(url="https://scontent-mrs2-2.xx.fbcdn.net/v/t1.6435-9/123118624_109002814343019_8104581893338609078_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=z9YlJWRGu9MAX_8WmgH&_nc_ht=scontent-mrs2-2.xx&oh=00_AT_cuDtQ-4j_W0valWvhJdqdh4dAzou-wjP5SSfjaQjwYQ&oe=6204ADBB")
    await ctx.send(embed=embed2)


  @commands.command()
  async def runa_yomosuki(self, ctx):
    embed2 = discord.Embed(title="Runa Yomosuki 🎰", description="She is a Member of the Student Council and the Leader of the Election Committe, Runa possess a streak of cruelty and tends to get bored very easily, She play a neutral role in the story", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="Around ~ 18 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="130cm (4'3)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.set_image(url="https://i.pinimg.com/564x/ea/2a/2d/ea2a2dca98cb80934beaa3d6e380579e.jpg")
    await ctx.send(embed=embed2)


  @commands.command()
  async def kirari_momobami(self, ctx):
    embed2 = discord.Embed(title="Kirari Momobami 🎰", description="She is the 105th Student Council President at Hyakkaou Private Academy and the one responsible for the current hierarchy at the academy whose family is aligned with the family of Yumeko Jabami. She is the creator of the infamous pet system", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="17 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Birthday", value="14 April", inline=True)
    embed2.add_field(name="Height", value="166cm (5'5½)", inline=True)
    embed2.add_field(name="Sexual Identity", value="Lesbian", inline=True)
    embed2.set_image(url="https://www.nautiljon.com/images/perso/00/43/momobami_kirari_17634.jpg?1542730341")
    await ctx.send(embed=embed2)

  @commands.command()
  async def yumemi_yumemite(self, ctx):
    embed2 = discord.Embed(title="Yumemi Yumemite 🎰", description="She is the Student Council Head's of Public Relations and a part-time Idol whose dream has always been to become a world famous actress, just like Kawaru Natari. On the outside she appears really sweet and cheerful. She is always upbeat and shows to love her fans above all else. But in reality, she's arrogant, calculated and sadistic", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="Aroud ~ 17 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="161cm (5'3½)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.set_image(url="https://i.ibb.co/mJRJZjW/a11da2f1677ec435ddb0df2692f5ed611fdc2b61-hq.gif")
    await ctx.send(embed=embed2)

  @commands.command()
  async def midari_ikishima(self, ctx):
    embed2 = discord.Embed(title="Midari Ikishima 🎰", description="She is a second-year student at Hyakkaou Private\nAcademy, a member of the student council and\n the president of the Beautification Council", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="18 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="170cm (5'7½)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.add_field(name="Sexual Identity", value="Lesbian", inline=True)
    embed2.set_image(url="https://i.pinimg.com/564x/ca/b0/78/cab078eed86054373b88e671f6b55181.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def kaede_manyuda(self, ctx):
    embed2 = discord.Embed(title="Kaede Manyuda 🎰", description="He is the manipulative former Treasurer of the Student Council\nwho has his own goal to take down Kirari Momobami", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="Around ~ 18 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Male", inline = True)
    embed2.add_field(name="Height", value="180cm (5'11)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.add_field(name="Sexual Identity", value="No Informations", inline=True)
    embed2.set_image(url="https://www.nautiljon.com/images/perso/00/06/manyuda_kaede_17660.jpg?1543241601")
    await ctx.send(embed=embed2)

  @commands.command()
  async def yuriko_nishinotouin(self, ctx):
    embed2 = discord.Embed(title="Yuriko Nishinotouin 🎰", description="She is a third-year student in Hyakkaou Private Academy, a member of the Student Council and the Head of the Traditional Culture Club.", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="Around ~ 19 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="163cm (5'4)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.add_field(name="Sexual Identity", value="No Informations", inline=True)
    embed2.set_image(url="https://wallpapercave.com/wp/wp9271345.jpg")
    await ctx.send(embed=embed2)


  @commands.command()
  async def sayaka_igarashi(self, ctx):
    embed2 = discord.Embed(title="Sayaka Igarashi 🎰", description="She is the Secretary of the Student Council and the Personal Assistant of the current Student Council President, Kirari Momobami.", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="16 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="160cm (5'3)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.add_field(name="Sexual Identity", value="Lesbian", inline=True)
    embed2.set_image(url="https://wallpapercave.com/wp/wp9271345.jpg")
    await ctx.send(embed=embed2)


  @commands.command()
  async def itsuki_sumeragi(self, ctx):
    embed2 = discord.Embed(title="Itsuki Sumeragi 🎰", description="She is a first-year student who belongs to the 'Flower' class at Hyakkaou Private Academy and a member of the Student Council whose father is the president of a prominent toy company in Japan.", color=0xf00020)
    embed2.add_field(name="Anime", value="Gambling School", inline=True)
    embed2.add_field(name="Age", value="16 Years Old", inline=True)
    embed2.add_field(name="Gender", value="Female", inline = True)
    embed2.add_field(name="Height", value="160cm (5'3)", inline=True)
    embed2.add_field(name="School Year", value="Second Year", inline=True)
    embed2.add_field(name="Sexual Identity", value="Lesbian", inline=True)
    embed2.set_image(url="https://www.nautiljon.com/images/perso/00/23/sumeragi_itsuki_17332.jpg?0")
    await ctx.send(embed=embed2)

  # --------------- Genshin Impact --------------- #

  @commands.command()
  async def shogun_raiden(self, ctx):
    embed2 = discord.Embed(title="Shogun Raiden ⚡", description="Raiden Shogun is the Electro Archon\n She is at the head of the Inazuma archipelago, where she pursues an isolationist policy. She is also at the origin of the Decree of seizure, by which she intends to confiscate all the divine eyes of the country. Is real name is Narukami Ogosho", color=0x8A2BE2)
    embed2.add_field(name="Vision", value="Electro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Sub DPS")
    embed2.add_field(name="Weapon Type", value="Polearm")
    embed2.add_field(name="Best Weapon", value="Reaper Light")
    embed2.add_field(name="Build", value="[Sub DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/10/Raiden_SupportDPS_V2.png)")
    embed2.set_image(url="https://www.nautiljon.com/images/jeuxvideo_persos/00/42/raiden_shogun_5024.jpg?0")
    await ctx.send(embed=embed2)

  @commands.command()
  async def kokomi_sangonomiya(self, ctx):
    embed2 = discord.Embed(title="Kokomi Sangonomiya 💧", description="The young Divine Priestess of Watatsumi\nIsland and a descendant of the Sangonomiya\n Clan, kokomi is in charge of most of \nWatatsumi's affairs shouldering heavy\nresponsibilities alone in hopes for giving\n Watatsumi Island's\npeople the hopes and happiness that they\ndesire.", color=0x2C75FF)
    embed2.add_field(name="Vision", value="Hydro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Support")
    embed2.add_field(name="Weapon Type", value="Catalyst")
    embed2.add_field(name="Best Weapon", value="Glow of the\neternal moon")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/09/Kokomi_Support_V2.png)")
    embed2.set_image(url="https://www.gamereactor.fr/media/39/_3533903b.jpg")
    await ctx.send(embed=embed2)

  
  @commands.command()
  async def arataki_itto(self, ctx):
    embed2 = discord.Embed(title="Arataki Itto ‍⚖️", description="A descendant of the crimson oni, Itto is also the leader and founder of the Arataki Gang.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Claymore")
    embed2.add_field(name="Best Weapon", value="Red horn stone breaker")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/12/Itto_DPSGeo.png)")
    embed2.set_image(url="https://i.ibb.co/sR5vwCL/image-2022-01-13-141002.png")
    await ctx.send(embed=embed2)


  @commands.command()
  async def hu_tao(self, ctx):
    embed2 = discord.Embed(title="Hu Tao ‍🔥", description="She is the 77th Director of the Wangsheng Funeral Parlor.", color=0xf00020)
    embed2.add_field(name="Vision", value="Pyro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Polearm")
    embed2.add_field(name="Best Weapon", value="Homa stick")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/09/Hutao_DPSPyro_V3.png)")
    embed2.set_image(url="https://upload-os-bbs.mihoyo.com/upload/2021/02/26/1015613/584bb1af3422f8cb9a2d96040f61904d_5123315465496787090.png?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,png")
    await ctx.send(embed=embed2)


  @commands.command()
  async def kamisato_ayaka(self, ctx):
    embed2 = discord.Embed(title="Ayaka Kamisato ‍❄️", description="She is the oldest daughter of the Kamisato Clan and sister of Kamisato Ayato. Being beautiful, elegant, and graceful, the common folk have nothing to bad-mouth Ayaka about", color=0x87CEFA)
    embed2.add_field(name="Vision", value="Cryo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Sword")
    embed2.add_field(name="Best Weapon", value="Mist slice reflection")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Ayaka_DPSCryo.png)")
    embed2.set_image(url="https://scontent-mrs2-1.xx.fbcdn.net/v/t1.6435-9/199334362_840730983226266_5169159086157944203_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=730e14&_nc_ohc=Gh947mnH4BgAX_AaFeh&_nc_ht=scontent-mrs2-1.xx&oh=00_AT_hyIUt-xbKUThL7IYau0dE4oUjg4Iu3yjMA5LX4zwQ0g&oe=62061F43")
    await ctx.send(embed=embed2)

  @commands.command()
  async def yoimiya(self, ctx):
    embed2 = discord.Embed(title="Yoimiya 🔥", description="She is the daughter of Naganohara Ryuunosuke and the current owner of Naganohara Fireworks. With her colorful fireworks and outgoing personality, Yoimiya is beloved by everyone on Narukami Island, who believe summer is not the same without her.", color=0xf00020)
    embed2.add_field(name="Vision", value="Pyro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Bow")
    embed2.add_field(name="Best Weapon", value="Thundering Pulse")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Yoimiya_DPSPyro.png)")
    embed2.set_image(url="https://scontent-mrs2-1.xx.fbcdn.net/v/t1.6435-9/198493713_840730016559696_1660857362534226810_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=730e14&_nc_ohc=wMuM1cyhs28AX-Nn_5B&_nc_oc=AQmQ1CDZMsXwq0Mb8oNtcN7Lu6TM-DGpRNVQjl-zCIzSfNhsg3Smqwg8W5vqFfTwwQo&_nc_ht=scontent-mrs2-1.xx&oh=00_AT8zgVMUofu7oSpPolvrF_z7wnQzkRSH0VesVFzhy0lGlg&oe=62063A49")
    await ctx.send(embed=embed2)


  @commands.command()
  async def shenhe(self, ctx):
    embed2 = discord.Embed(title="Shenhe ❄️", description="The daughter of an unnamed exorcist couple, Shenhe was taken in by Cloud Retainer as a disciple following a traumatic incident during her childhood.", color=0x87CEFA)
    embed2.add_field(name="Vision", value="Cryo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Sub DPS")
    embed2.add_field(name="Weapon Type", value="Polearm")
    embed2.add_field(name="Best Weapon", value="Calamity Queller")
    embed2.add_field(name="Build", value="[Sub DPS](https://www.genshin-impact.fr/wp-content/uploads/2022/01/Shenhe_SupportDPS.png)")
    embed2.set_image(url="https://assets.promediateknologi.com/crop/0x0:0x0/x/photo/2021/11/23/383559389.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def tartaglia(self, ctx):
    embed2 = discord.Embed(title="Tartaglia 💧", description="He is the Eleventh of the Fatui Harbingers. Following danger wherever he goes, Childe is always eager for a challenge, making him extremely dangerous despite being the youngest member.", color=0x2C75FF)
    embed2.add_field(name="Vision", value="Hydro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Bow")
    embed2.add_field(name="Best Weapon", value="North Star")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/10/Tartaglia_DPSHydro_V2.png)")
    embed2.set_image(url="https://www.nautiljon.com/images/jeuxvideo_persos/00/21/tartaglia_5012.jpg?1633727053")
    await ctx.send(embed=embed2)

  @commands.command()
  async def xiao(self, ctx):
    embed2 = discord.Embed(title="Xiao 💨", description="He is an adeptus, under the name Alatus, and the only known remaining member of the five foremost Yakshas dispatched by Morax to subdue the demonic spirits that plagued Liyue. He currently resides in Wangshu Inn and mostly secludes himself from crowds and human interactions.", color=0xb0f2b6)
    embed2.add_field(name="Vision", value="Anemo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Polearm")
    embed2.add_field(name="Best Weapon", value="Homa stick")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Xiao_DPSAnemo-1.png)")
    embed2.set_image(url="https://uploadstatic-sea.mihoyo.com/contentweb/20210211/2021021110492982765.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def kazuha(self, ctx):
    embed2 = discord.Embed(title="Kaedehara Kazuha 💨", description="A wandering samurai of the once-famed Kaedehara Clan, Kazuha is a temporary crewmember of The Crux.", color=0xb0f2b6)
    embed2.add_field(name="Vision", value="Anemo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Support, DPS")
    embed2.add_field(name="Weapon Type", value="Sword")
    embed2.add_field(name="Best Weapon", value="Mist slice reflection")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Kazuha_Support.png)\n[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Kazuha_DPSAnemo.png)")
    embed2.set_image(url="https://www.gamereactor.fr/media/81/_3488153b.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def keqing(self, ctx):
    embed2 = discord.Embed(title="Keqing ⚡", description="As the Yuheng of the Liyue Qixing, she is someone who seeks her own answers instead of idly letting chaos run amok in Liyue. She chooses her own path with her own power and ability, instead of letting the gods determine her fate.", color=0x8A2BE2)
    embed2.add_field(name="Vision", value="Electro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Sword")
    embed2.add_field(name="Best Weapon", value="Mist slice reflection")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Keqing_DPSElectro_V2.png)")
    embed2.set_image(url="https://i0.wp.com/uploadstatic-sea.mihoyo.com/contentweb/20200911/2020091119432453840.jpg")
    embed2.set_thumbnail(url="")
    await ctx.send(embed=embed2)

  @commands.command()
  async def venti(self, ctx):
    embed2 = discord.Embed(title="Venti 💨", description="He is a free-spirited, wine-loving bard in Mondstadt and the current mortal vessel of Barbatos, the Anemo Archon. He first appears during the Archon Quest Prologue: Act I - The Outlander Who Caught the Wind.", color=0xb0f2b6)
    embed2.add_field(name="Vision", value="Anemo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Bow")
    embed2.add_field(name="Best Weapon", value="Skyward Harp")
    embed2.add_field(name="Build", value="[Sub DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/09/Venti_SupportDPS_V2.png)\n[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Venti_Support.png)")
    embed2.set_image(url="https://i.ibb.co/fX7QKX4/Venti-Character-2.jpg")
    embed2.set_thumbnail(url="")
    await ctx.send(embed=embed2)


  @commands.command()
  async def mona(self, ctx):
    embed2 = discord.Embed(title="Mona 💧", description="He is a free-spirited, wine-loving bard in Mondstadt and the current mortal vessel of Barbatos, the Anemo Archon. He first appears during the Archon Quest Prologue: Act I - The Outlander Who Caught the Wind.", color=0x2C75FF)
    embed2.add_field(name="Vision", value="Hydro", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Support")
    embed2.add_field(name="Weapon Type", value="Catalyst")
    embed2.add_field(name="Best Weapon", value="Widsith")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Mona_SupportBurst.png)")
    embed2.set_image(url="https://static1.millenium.org/articles/4/37/14/34/@/1412467-artwork-officiel-de-mona-article_image_d-1.jpg")
    embed2.set_thumbnail(url="")
    await ctx.send(embed=embed2)

  @commands.command()
  async def barbara(self, ctx):
    embed2 = discord.Embed(title="Barbara 💧", description="She is the deaconess of the Church of Favonius and a self-proclaimed idol after learning about them from the intrepid adventurer Alice. She is also the daughter of Frederica Gunnhildr and Seamus Pegg, and the younger sister of Jean. Through Frederica she is a descendant of the prestigious Gunnhildr Clan.", color=0x2C75FF)
    embed2.add_field(name="Vision", value="Hydro", inline=True)
    embed2.add_field(name="Character", value="4 ★★★★")
    embed2.add_field(name="Character Type", value="Heal")
    embed2.add_field(name="Weapon Type", value="Catalyst")
    embed2.add_field(name="Best Weapon", value="Prototype Amber")
    embed2.add_field(name="Build", value="[Heal](https://www.genshin-impact.fr/wp-content/uploads/2021/11/Barbara_Heal_V3.png)")
    embed2.set_image(url="https://www.nautiljon.com/images/jeuxvideo_persos/00/95/barbara_4959.jpg?0")
    embed2.set_thumbnail(url="")
    await ctx.send(embed=embed2)

  @commands.command()
  async def xingqiu(self, ctx):
    embed2 = discord.Embed(title="Xingqiu 💧", description="He is the second son of the Guild Manager of the Feiyun Commerce Guild, an influential group in Liyue, and is also a self-proclaimed practitioner of the Guhua Clan's arts.", color=0x2C75FF)
    embed2.add_field(name="Vision", value="Hydro", inline=True)
    embed2.add_field(name="Character", value="4 ★★★★")
    embed2.add_field(name="Character Type", value="Support")
    embed2.add_field(name="Weapon Type", value="Sword")
    embed2.add_field(name="Best Weapon", value="The Sacrificial Sword")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Xingqiu_SupportDPS.png)")
    embed2.set_image(url="https://www.nautiljon.com/images/jeuxvideo_persos/00/79/xingqiu_5097.jpg?0")
    embed2.set_thumbnail(url="")
    await ctx.send(embed=embed2)

  @commands.command()
  async def yunjin(self, ctx):
    embed2 = discord.Embed(title="Yun Jin ‍⚖️", description="She is a prestigious dancer, singer, and brewer who works at the Heyu Tea House.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Sub DPS")
    embed2.add_field(name="Weapon Type", value="Lance")
    embed2.add_field(name="Best Weapon", value="Reaper light")
    embed2.add_field(name="Build", value="[Sub DPS](https://www.genshin-impact.fr/wp-content/uploads/2022/01/unknown-4.png)")
    embed2.set_image(url="https://i.ibb.co/sR5vwCL/image-2022-01-13-141002.png")
    await ctx.send(embed=embed2)

  @commands.command()
  async def gorou(self, ctx):
    embed2 = discord.Embed(title="Gorou ⚖️", description="He is the courageous and reliable general\nof the Watatsumi Army, a leader whose\nmen can always place their trust in.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="4 ★★★★")
    embed2.add_field(name="Character Type", value="Support")
    embed2.add_field(name="Weapon Type", value="Bow")
    embed2.add_field(name="Best Weapon", value="Favonius Warbow")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/12/Gorou_Support.png)")
    embed2.set_image(url="https://i.ibb.co/ysqxJPg/CG.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def zhongli(self, ctx):
    embed2 = discord.Embed(title="Zhongli ⚖️", description="He is later revealed to be the current vessel of the Geo Archon, Morax, who has decided to experience the world from the perspective of a mortal. After giving up his Gnosis, he retires from his position as an Archon and returns to his former identity as an Adeptus, although still under the guise of being a human. He currently works as a consultant of the Wangsheng Funeral Parlor.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Support")
    embed2.add_field(name="Weapon Type", value="Polearm")
    embed2.add_field(name="Best Weapon", value="Staff of Homa")
    embed2.add_field(name="Build", value="[Support](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Zhongli_Support.png)")
    embed2.set_image(url="https://i.pinimg.com/564x/f8/a3/91/f8a3917b3a8913e9a596b1525e49cc10.jpg")
    await ctx.send(embed=embed2)

  @commands.command()
  async def albedo(self, ctx):
    embed2 = discord.Embed(title="Albedo ⚖️", description="A synthetic human made by the alchemist Rhinedottir, the mysterious Albedo is the Chief Alchemist and Captain of the Investigation Team of the Knights of Favonius. Through a recommendation from the adventurer Alice, with Sucrose as his assistant, he holds an infinite desire to learn about the world of Teyvat, carefully studying every object around him.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="5 ★★★★★")
    embed2.add_field(name="Character Type", value="Sub DPS")
    embed2.add_field(name="Weapon Type", value="Sword")
    embed2.add_field(name="Best Weapon", value=" Favonius Sword")
    embed2.add_field(name="Build", value="[Sub DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/11/Albedo_SupportDPS_V3.png)")
    embed2.set_image(url="https://www.nautiljon.com/images/jeuxvideo_persos/00/71/albedo_4917.jpg?1625102932")
    await ctx.send(embed=embed2)

  @commands.command()
  async def ningguang(self, ctx):
    embed2 = discord.Embed(title="Ningguang ⚖️", description="She is the Tianquan of the Liyue Qixing and owns the floating Jade Chamber in the skies of Liyue.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="4 ★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Catalyst")
    embed2.add_field(name="Best Weapon", value="Memory of Dust")
    embed2.add_field(name="Build", value="[DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/08/Ningguang_DPSGeo.png)")
    embed2.set_image(url="https://jeuendroit.com/wp-content/uploads/2022/01/Genshin-Impact-Ningguang-Hangout-Guide-–-Deverrouiller-Outift-toutes-les.png")
    await ctx.send(embed=embed2)

  @commands.command()
  async def noelle(self, ctx):
    embed2 = discord.Embed(title="Noelle ⚖️", description="While not yet a knight, she seeks to one day join the Knights of Favonius by first serving as a dutiful maid.", color=0xefd807)
    embed2.add_field(name="Vision", value="Geo", inline=True)
    embed2.add_field(name="Character", value="4 ★★★★")
    embed2.add_field(name="Character Type", value="DPS")
    embed2.add_field(name="Weapon Type", value="Claymore")
    embed2.add_field(name="Best Weapon", value="Skyward Pride")
    embed2.add_field(name="Build", value="[Support Heal](https://www.genshin-impact.fr/wp-content/uploads/2021/12/Noelle_SupportHeal_V3.png)\n[Support DPS](https://www.genshin-impact.fr/wp-content/uploads/2021/12/Noelle_SupportDPS_V3.png)")
    embed2.set_image(url="https://scontent-mrs2-1.xx.fbcdn.net/v/t1.6435-9/90014916_562207354411965_5022845814653845504_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=730e14&_nc_ohc=4ySo08YYHS8AX9i7K8Q&_nc_ht=scontent-mrs2-1.xx&oh=00_AT-buusgYo-LOEZyWSVHccFod7jHeuUQc1fiaMZ4vQgTJw&oe=620D54B6")
    await ctx.send(embed=embed2)