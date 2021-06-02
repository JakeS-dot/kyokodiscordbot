# Imports
import discord
from discord.ext import commands
import random

# Credentials

TOKEN = 'ODQ5NjEzOTEyMDI1OTg5MTUw.YLdunQ.eCwrLl7yBwzOVJMctYTyVwZc2JE'

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
magica_characters = [
    'Kyosuke https://static.wikia.nocookie.net/madoka/images/8/87/KyosukeCharacterDesignWebsite.png/revision/latest/scale-to-width/360?cb=20150715030458',
    'Madoka https://davedalessiowrites.files.wordpress.com/2020/03/madoka-kaname.png',
    'Homura https://i.pinimg.com/originals/90/ed/92/90ed9250ac172a0b0ce97d145d891b63.png',
    'Mami https://static.wikia.nocookie.net/mugen/images/0/0b/Tomoe_Mami.png/revision/latest?cb=20180423040637',
    'Sayaka https://static.wikia.nocookie.net/characterprofile/images/f/f5/Sayaka_Miki%2C_Madoka_Kaname%27s_Protector.png/revision/latest?cb=20160109071921',
    'Kyoko https://static.wikia.nocookie.net/madoka/images/c/cb/Kyoko_magical_outfit_1.png/revision/latest/scale-to-width-down/238?cb=20160821020253',
    'Hitomi https://static.wikia.nocookie.net/all-worlds-alliance/images/f/f8/Hitomi-shizuki.png/revision/latest?cb=20180529035937']

rebellion_characters = [
    'Kyosuke https://static.wikia.nocookie.net/madoka/images/8/87/KyosukeCharacterDesignWebsite.png/revision/latest/scale-to-width/360?cb=20150715030458',
    'Madoka https://davedalessiowrites.files.wordpress.com/2020/03/madoka-kaname.png',
    'Homura https://i.pinimg.com/originals/90/ed/92/90ed9250ac172a0b0ce97d145d891b63.png',
    'Mami https://static.wikia.nocookie.net/mugen/images/0/0b/Tomoe_Mami.png/revision/latest?cb=20180423040637',
    'Sayaka https://static.wikia.nocookie.net/characterprofile/images/f/f5/Sayaka_Miki%2C_Madoka_Kaname%27s_Protector.png/revision/latest?cb=20160109071921',
    'Kyoko https://static.wikia.nocookie.net/madoka/images/c/cb/Kyoko_magical_outfit_1.png/revision/latest/scale-to-width-down/238?cb=20160821020253',
    'Hitomi https://static.wikia.nocookie.net/all-worlds-alliance/images/f/f8/Hitomi-shizuki.png/revision/latest?cb=20180529035937',
    'Nagisa Momoe https://static.wikia.nocookie.net/magicalgirlmadokamagica/images/d/da/Nagisa_Momoe.png/revision/latest?cb=20150116234215']

fact_list = [
    'here are actually a fair few subjects Madoka dislikes, being English, Science, Chemistry, and she also notes a dislike of Physical Education, due to her low fortitude.',
    'Madoka is in two clubs, both the gardening and crafts clubs.',
    '', ]


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
                               description="Well it seems like you need help. Noob. Anyways here's the commands you wanted.",
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
    await message.channel.send(
        "Here's a random one... " + random.choice(magica_characters) + " is a good character! (I think..)")


# Rebellion command
@client.command()
async def rebellion(message):
    await message.channel.send(
        "Here's a random one... " + random.choice(rebellion_characters) + " is a good pick! (I think..)")


# Waiting

# Fact Command
# @client.command()
# async def fact(message):
#    await message.channel.send(
#        "No. Command in progress")


# (random.choice(fact_list))

# status
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name='TO MANY NAGITO EDITS | k!help | v1.0.2, day idk of making this bot | Bot Made By xx-jake-xx#5302'))


# @client.event
# async def on_ready():
# await client.change_presence(
# activity=discord.Streaming(name='Coding Kyoko To Be Better!', url='https://www.twitch.tv/xx_jake0930_xx'))


# ########################### #


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return

    if "Madoka" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "magical girl" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "meguca" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")

    if "sayaka" in message.content:
        await message.add_reaction('\U00002764')

    if "Sayaka" in message.content:
        await message.add_reaction('\U00002764')

    if "Kyubey" in message.content:
        await message.add_reaction('\U0001F620')

    if "kyubey" in message.content:
        await message.add_reaction('\U0001F620')

    await client.process_commands(message)


client.run(TOKEN)
