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


# couple command

@client.command()
async def couple(ctx):
    embed = discord.Embed(title=('In my opinion, ' + (random.choice(couple_list)) + ' and ' + (
        random.choice(couple_list)) + ' would be a great pair!'), color=0x8b0000)
    embed.set_footer(text="What a nice couple 💘💖💗💓🧡💝💙❤💕💔♥♥")
    await ctx.send(embed=embed)


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
                         value="Joins a voice call and plays a random ost from the Madoka Magica series (Have to be in a vc to use)",
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
    embed_help.set_image(url='https://cdn.discordapp.com/attachments/783124120492572684/845654137286033448/2922757-7815334573-POTK-.png')
    await ctx.send(embed=embed_help)


# status
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name='TOO MANY NAGITO EDITS!!'))


# ########################### #


@client.event
async def on_message(message):
    if "madoka" in message.content:
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


Beep(1000, 300)
client.run(TOKEN)
