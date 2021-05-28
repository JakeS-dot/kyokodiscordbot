# Imports
from winsound import Beep
import discord
from discord.ext import commands
import random

# Credentials

TOKEN = 'ODQ0NzA2NjQzOTM2OTM1OTg3.YKWUXQ.Nv7tkuzZmg1ssug0flOwkWNWQfM'

# Create bot
client = commands.Bot(command_prefix='k!')
client.remove_command('help')

# lists for commands
couple_list = ['Jake', 'Chair Man', 'Eleanor', 'Sofy', 'Vae', 'Pebble', 'Tenko', 'Nagito', 'MEE6', 'Carl-Bot', 'Iman']
ship_list = ['Madoka Kaname', 'Homura Akemi', 'Sayaka Miki', 'Mami Tomoe', 'Kyo(u)ko Sakura', 'Hitomi Shizuki',
             'Kyosuke Kamijio']
ship_dis = ['It would be so intense!', 'A nail biter!', 'Its the best pick I got!']
place_sur = ['3rd', '2nd', ]
death_sur = ['became a witch.', 'had your soul gem destroyed.', 'were killed by a witch. ']
ost_list = ['ost_1.mp3', 'ost_2.mp3', 'ost_3.mp3', 'ost_4.mp3', 'ost_5.mp3', 'ost_6.mp3', 'ost_7.mp3', 'ost_8.mp3',
            'ost_9.mp3', 'ost_10.mp3', 'ost_11.mp3', 'ost_12.mp3', 'ost_13.mp3', 'ost_14.mp3', 'ost_15.mp3',
            'ost_16.mp3', 'ost_17, ost_18']
speak_list = ['speak_1.mp3', 'speak_2.mp3', 'speak_3.mpz`3', 'speak_4.mp3', 'speak_5.mp3', 'speak_6.mp3', 'speak_7.mp3',
              'speak_8.mp3', 'speak_9.mp3', 'speak_10.mp3']
magica_characters = ['Kyosuke', 'Madoka', 'Homura' 'Mami', 'Sayaka' 'Kyoko', 'Hitomi']
magica_pictures = [
    'https://static.wikia.nocookie.net/villains/images/3/36/Kyubey2.png/revision/latest?cb=20160427035119',
    'https://static.wikia.nocookie.net/madoka/images/c/c9/Yachiyo_Profile.png/revision/latest?cb=20200130194756',
    'https://static.wikia.nocookie.net/madoka/images/7/7c/Rena.png/revision/latest?cb=20201224204513',
    'https://static.wikia.nocookie.net/madoka/images/1/16/Momoko_ref.png/revision/latest/top-crop/width/360/height/450?cb=20201225084732',
    'https://static.wikia.nocookie.net/madoka/images/2/2a/Iroha_Character.png/revision/latest?cb=20200528195609',
    'https://static.wikia.nocookie.net/magiarecord-en/images/b/bf/Akino_Kaede_Akino_Kaede.png/revision/latest?cb=20190714034621']


# couple command
@client.command()
async def couple(ctx):
    embed_couple = discord.Embed(title=('In my opinion, ' + (random.choice(couple_list)) + ' and ' + (
        random.choice(couple_list)) + ' would be a great pair!'), color=0x8b0000)
    embed_couple.set_footer(text="What a nice couple 💘💖💗💓🧡💝💙❤💕💔♥♥")
    await ctx.send(embed=embed_couple)


# ship command
@client.command()
async def ship(ctx):
    ship_cmd = discord.Embed(title=('In my opinion, ' + (random.choice(ship_list)) + ' and ' + (
        random.choice(ship_list)) + ' would be a great ship!'), color=0x8b0000)
    ship_cmd.set_footer(text=(random.choice(ship_dis)))
    ship_cmd.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/801105512933752882/845050099678576640/unknown.png")
    await ctx.send(embed=ship_cmd)


# help command
@client.command()
async def help(ctx):
    embed_help = discord.Embed(title="Help!",
                               description="Well it seems like you need help. Noob. Anyways heres the commands you wanted.",
                               color=0xa80000)
    embed_help.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")
    embed_help.add_field(name="k!help", value="Shows this menu, how impressive.", inline=False)
    embed_help.add_field(name="k!survival",
                         value="A command that randomly generates chances of surviving madoka magica",
                         inline=False)
    embed_help.add_field(name="k!ost",
                         value="Joins a voice call and plays a random ost from the Madoka Magica series (and some fan songs too!) (Have to be in a vc to use)",
                         inline=False)
    embed_help.add_field(name="k!magica",
                         value="A command that randomly selects a character from the anime Madoka Magica",
                         inline=False)
    embed_help.add_field(name="k!rebellion ",
                         value="A command that randomly selects a character from Madoka Magica Rebellion",
                         inline=False)
    embed_help.add_field(name="k!record",
                         value="A command that randomly selects a character from the anime Magia Record",
                         inline=False)
    embed_help.add_field(name="k!fact", value="A command that gives a random fact about the anime Madoka Magica",
                         inline=False)
    embed_help.add_field(name="k!speak", value="I'll speak! (Have to be in a vc to use)", inline=False)
    embed_help.set_image(
        url='https://cdn.discordapp.com/attachments/783124120492572684/845654137286033448/2922757-7815334573-POTK-.png')
    await ctx.send(embed=embed_help)


# survival command
@client.command()
async def survival(ctx):
    username = ctx.message.author.name
    embed_sur = discord.Embed(title="Survival Rating",
                              description="Let's see...     " + username + ", I would say you have a " + str(
                                  random.randint(1,
                                                 99)) + "% chance of surviving Madoka Magica. You would die " + str(
                                  random.choice(place_sur)) + " and you died because you " + str(
                                  random.choice(death_sur)), color=0xb30000, )
    embed_sur.set_image(url="https://www.pngkey.com/png/full/179-1790644_information-kyoko-sakura-power.png")
    await ctx.send(embed=embed_sur)


# ost command
@client.command()
async def ost(message):
    voice = await message.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio(random.choice(ost_list)))


# speak command
@client.command()
async def speak(message):
    voice_s = await message.author.voice.channel.connect()
    voice_s.play(discord.FFmpegPCMAudio(random.choice(speak_list)))


# stop command
@client.command()
async def stop(ctx):
    await ctx.voice_client.disconnect()


# Magica command
@client.command()
async def magica(message):
    await message.channel.send("Heres a random one..." + random.choice(magica_characters) + " is a good charecter! (I think..)")


# status
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name='TOO MANY NAGITO EDITS!!'))


# @client.event
# async def on_ready():
# await client.change_presence(
# activity=discord.Streaming(name='Coding Kyoko To Be Better!', url='https://www.twitch.tv/xx_jake0930_xx'))


# ########################### #


@client.event
async def on_message(message):
    if "madoka" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "magical girl" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "meguca" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "kyubey" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/villains/images/3/36/Kyubey2.png/revision/latest?cb=20160427035119")

    if "Yachiyo Nanami" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/madoka/images/c/c9/Yachiyo_Profile.png/revision/latest?cb=20200130194756")

    if "Rena Minami" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/madoka/images/7/7c/Rena.png/revision/latest?cb=20201224204513")

    if "Momoko Togame" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/madoka/images/1/16/Momoko_ref.png/revision/latest/top-crop/width/360/height/450?cb=20201225084732")

    if "Iroha Tamaki" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/madoka/images/2/2a/Iroha_Character.png/revision/latest?cb=20200528195609")

    if "Kaede Akino" in message.content:
        await message.channel.send("https://static.wikia.nocookie.net/magiarecord-en/images/b/bf/Akino_Kaede_Akino_Kaede.png/revision/latest?cb=20190714034621")

    if "sayaka" in message.content:
        await message.add_reaction('\U00002764')

    if "Sayaka" in message.content:
        await message.add_reaction('\U00002764')

    if "Kyubey" in message.content:
        await message.add_reaction('\U0001F620')

    if "kyubey" in message.content:
        await message.add_reaction('\U0001F620')

    await client.process_commands(message)


Beep(1000, 300)
client.run(TOKEN)
