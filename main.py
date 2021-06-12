# Imports
import discord
from discord.ext import commands
import random

# JAKE REMINDER TO CHANGE THE TOKEN IF YOUR COPY AND PASTING THE CODE! CHANGE IT FROM NOT BOT TESTER TOKEN, BUT KYOKO TOKEN

# Credentials
# TOKEN FOR BOT TESTER FOR KYOKO IS ODQ5NjEzOTEyMDI1OTg5MTUw.YLdunQ.eCwrLl7yBwzOVJMctYTyVwZc2JE
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

record_characters = [
    'Iroha https://static.wikia.nocookie.net/madoka/images/2/2a/Iroha_Character.png/revision/latest?cb=20200528195609',
    'Yachiyo https://static.wikia.nocookie.net/madoka/images/c/c9/Yachiyo_Profile.png/revision/latest?cb=20200130194756'
    'Tsuruno https://images.puella-magi.net/thumb/3/39/Tsuruno_character.png/300px-Tsuruno_character.png?20170514003003',
    'Sana https://images.puella-magi.net/thumb/e/e4/Sana_character.png/300px-Sana_character.png?20170514002521',
    'Felicia https://static.wikia.nocookie.net/madoka/images/f/f3/Felicia_Profile.png/revision/latest?cb=20200130214559',
    'Mifuyu https://images.puella-magi.net/thumb/d/d5/Mifuyu_Magireco_Profile.png/300px-Mifuyu_Magireco_Profile.png?20180609015225',
    'Touka https://static.wikia.nocookie.net/madoka/images/6/69/Satomi_Touka.png/revision/latest?cb=20200810071722',
    'Alina https://static.wikia.nocookie.net/madoka/images/7/71/Alinagray-0.png/revision/latest?cb=20200810065935',
    'Nemu https://images.puella-magi.net/thumb/5/5e/Nemu_Temp_Profile.png/300px-Nemu_Temp_Profile.png?20190319212729',
    'Ui https://images.puella-magi.net/thumb/6/68/Character_image-06-pc.png/150px-Character_image-06-pc.png?20200830134120',
    'Rena https://static.wikia.nocookie.net/madoka/images/7/7c/Rena.png/revision/latest?cb=20201224204513',
    'Momoko https://images.puella-magi.net/thumb/2/21/Momoko_Togame.png/300px-Momoko_Togame.png?20170723182841',
    'Akino https://images.puella-magi.net/thumb/2/21/Akino_kaede.png/300px-Akino_kaede.png?20170815190110',
    'Karin https://images.puella-magi.net/thumb/e/ed/Karin_profile_magia_record.png/300px-Karin_profile_magia_record.png?20171030100952',
    'Kanagi https://images.puella-magi.net/thumb/8/89/Kanagi_magireco_profile.png/300px-Kanagi_magireco_profile.png?20180618122308',
    'Mitama https://images.puella-magi.net/thumb/c/c8/Mitama_magireco_profile.png/300px-Mitama_magireco_profile.png?20180413084735',
    'Tsukuyo https://static.wikia.nocookie.net/madoka/images/c/ce/Tsukuyo.png/revision/latest?cb=20200812041910',
    'Tsukasa https://images.puella-magi.net/thumb/4/4d/Tsukasa_profile.png/300px-Tsukasa_profile.png?20171130120813',
    'Kagome https://static.wikia.nocookie.net/character-stats-and-profiles/images/8/83/Kagome_school.png/revision/latest?cb=20200117221612',
    'Yuna https://images.puella-magi.net/thumb/d/d4/Character_image-01-pc_%282%29.png/150px-Character_image-01-pc_%282%29.png?20200827053513',
    'Kirari https://static.wikia.nocookie.net/magiarecord-en/images/8/87/Kirari_Hikaru_Kirari_Hikaru.png/revision/latest?cb=20191015142418',
    'Ao https://images.puella-magi.net/thumb/5/57/Card_10234_l.png/300px-Card_10234_l.png?20200413161241,'
    'Juri https://static.wikia.nocookie.net/character-stats-and-profiles/images/7/70/Oba_School.png/revision/latest/scale-to-width-down/350?cb=20191025192814',
    'Shizuka https://images.puella-magi.net/thumb/c/c8/Character_image-01-pc.png/150px-Character_image-01-pc.png?20200827052609',
    'Hiroe https://static.wikia.nocookie.net/magiarecord-en/images/7/73/Hiroe_Chiharu_Hiroe_Chiharu.png/revision/latest?cb=20190810085319',
    'Sunao https://images.puella-magi.net/thumb/6/6c/Card_10274_l.png/300px-Card_10274_l.png?20191111161904',
    'Himena https://preview.redd.it/10ydwy3vre251.jpg?auto=webp&s=383b83fbc697a41ce3a84c99ddb3f54c5179337e',
    'Miyabi https://static.wikia.nocookie.net/magiarecord-en/images/c/cb/Miyabi_Shigure_Miyabi_Shigure.png/revision/latest/scale-to-width-down/400?cb=20191210112018',
    'Hagumu https://images.puella-magi.net/thumb/f/f7/Card_10304_l.png/300px-Card_10304_l.png?20200225160028,'
    'San https://images.puella-magi.net/thumb/4/4d/San_PM.png/300px-San_PM.png?20210322154351',
    'Miyuri https://images.puella-magi.net/thumb/c/c3/Miyuri_PM.png/300px-Miyuri_PM.png?20210322154358',
    'Rabi https://images.puella-magi.net/thumb/8/88/Unknown_9.png/150px-Unknown_9.png?20191110225936',
    'Asashi https://images.puella-magi.net/thumb/2/27/Asashi_PM.png/150px-Asashi_PM.png?20200415032245',
    'Alexandra https://images.puella-magi.net/thumb/9/9b/Card_10354_l.png/200px-Card_10354_l.png?20210414144230',
    'Ulala https://images.puella-magi.net/thumb/b/ba/Urara_PM.png/150px-Urara_PM.png?20200529151225',
    'Nayuta https://images.puella-magi.net/thumb/4/45/Nayuta_PM.png/150px-Nayuta_PM.png?20200630173031',
    'Mikage https://images.puella-magi.net/thumb/0/0c/Card_10384_l.png/300px-Card_10384_l.png?20201116154251',
    'Sudachi https://images.puella-magi.net/thumb/7/76/Card_10394_l.png/300px-Card_10394_l.png?20200706160947',
    'Yozuru https://images.puella-magi.net/thumb/e/e1/Card_10404_l.png/300px-Card_10404_l.png?20200309194729',
    'Medrios https://static.wikia.nocookie.net/magiarecord-en/images/7/7b/Livia_Medeiros_Livia_Medeiros.png/revision/latest/scale-to-width-down/400?cb=20200117093256',
    'Lil Kubey https://images.puella-magi.net/thumb/c/c5/Mokyu.png/250px-Mokyu.png?20190807195659']


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
    embed_help.add_field(name="k!magica",
                         value="A command that randomly selects a character from the anime Madoka Magica",
                         inline=False)
    embed_help.add_field(name="k!rebellion ",
                         value="A command that randomly selects a character from Madoka Magica Rebellion",
                         inline=False)
    embed_help.add_field(name="k!record ",
                         value="A command that randomly selects a character from Madoka Magica Rebellion",
                         inline=False)
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


# Record Command

@client.command()
async def record(message):
    await message.channel.send(
        "Here's a random one... " + random.choice(record_characters) + " is a good pick! (I think..)")


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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
