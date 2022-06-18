# Nayo Discord Bot
## Multipurpose Bot Based on Anime with lot's of Fun, Cool and Useful Commands like Anime, Hentai, Administration, Moderation, Economy and More...

### Important Links :

[Website](https://nayobot.moe),
[Server](https://discord.gg/J33NPfctv4),
[Nayo Commands](https://nayobot.moe/commands),
[Documentation](https://docs.nayobot.moe),
[Nayo API](https://docs.nayobot.moe#content-nayo-api),
[Support Nayo](https://nayobot.moe/premium)


## Discover Nayo

### 🌸 Anime Waifu

<sub>Create a Bank Account and start buy and collect Waifu ✿>ω<</sub>
  
<sub>See your collection and get extra gems and Cukeni every 30 Minutes by meeting a Waifu !</sub>

![Waifu](https://nayobot.moe/img/pre-3.3.png)
  
------
### 📋 Anime Informations

<sub>Search Anime Informations and get duration, episodes, community rating and More...</sub>

![Waifu](https://nayobot.moe/img/pre-1.1.png)
  
------
### 😂 Anime Reactions

<sub>React with Fun and Cool Gifs like Angry, Bang, Kill, Cry, Happy and More...</sub>

![Waifu](https://nayobot.moe/img/pre-2.2.png)
  
------
### 🆙 Leveling System

<sub>Discover Nayo Leveling System based on Anime (Currently in Developement)</sub>

![Waifu](https://nayobot.moe/img/pre-4.4.png)
  
------
  
# WARNING : Following Content Contains NSFW Image
  
### 🔞 Anime NSFW

<sub>See and Send (NSFW Channels Only) : Hentai, Yaoi, Yuri, Pussy, Lewd, Boobs, Blowjob and more Anime NSFW Images... >///<</sub>

![Waifu](https://nayobot.moe/img/pre-7.7.png)
  
------
  
## Discover Nayo API
  
<sub>The powerful API that let you get cool and fun Anime Gifs, Using JSON with a lot's of Gifs !</sub>
  
```
API Base Url : https://nayobot.moe/api/
```
  
Request Type : GET
  
#### Response Type (Example) :
```json
{"Code":200,"Img":"https://nayobot.moe/api/hug/hug_20.gif"}
```
  
#### Use Nayo API with Python (Example) :
```python
animeshocked = requests.get("https://nayobot.moe/api/shocked") # Using Request Module
gif = animeshocked.json() # Get JSON on Html Page
Img = gif['Img'] # Get the gif
embed = discord.Embed(description=f"**{ctx.author.name}** is shocked 😱", color=0xd0c0e9) # Embed Example
embed.set_image(url=Img) # Embed Image
await ctx.send(embed=embed) # Sending Embed with Gif
```
