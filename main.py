# Imports
import discord
from discord.ext import commands
import random

# JAKE REMINDER TO CHANGE THE TOKEN IF YOUR COPY AND PASTING THE CODE! CHANGE IT FROM NOT THE KYOKO (TEST) TOKEN, BUT KYOKO (MAIN) TOKEN

# Credentials
# TOKEN FOR FOR KYOKO (MAIN) IS ODUzMzk2Mjg4MTYyMTAzMzA3.YMUxOg.cg1IbTAlJwXRxjiacHkN4oL3CBE
# TOKEN FOR KYOKO (TEST) IS ODQ5NjEzOTEyMDI1OTg5MTUw.YLdunQ.-MfU88k5sPNxQ0svpuNlDLRNTS0
TOKEN = 'ODUzMzk2Mjg4MTYyMTAzMzA3.YMUxOg.cg1IbTAlJwXRxjiacHkN4oL3CBE'

# Create bot
client = commands.Bot(command_prefix='k!',
                      activity=discord.Activity(type=discord.ActivityType.watching,
                                                name="TOO MANY NAGITO EDITS | v0.4.2 | Made by xx-jake-xx#5302  "))
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
    'Yachiyo https://static.wikia.nocookie.net/madoka/images/c/c9/Yachiyo_Profile.png/revision/latest?cb=20200130194756',
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
    'Ao https://images.puella-magi.net/thumb/5/57/Card_10234_l.png/300px-Card_10234_l.png?20200413161241',
    'Juri https://static.wikia.nocookie.net/character-stats-and-profiles/images/7/70/Oba_School.png/revision/latest/scale-to-width-down/350?cb=20191025192814',
    'Shizuka https://images.puella-magi.net/thumb/c/c8/Character_image-01-pc.png/150px-Character_image-01-pc.png?20200827052609',
    'Hiroe https://static.wikia.nocookie.net/magiarecord-en/images/7/73/Hiroe_Chiharu_Hiroe_Chiharu.png/revision/latest?cb=20190810085319',
    'Sunao https://images.puella-magi.net/thumb/6/6c/Card_10274_l.png/300px-Card_10274_l.png?20191111161904',
    'Himena https://images.puella-magi.net/thumb/e/e5/Himena_PM.png/150px-Himena_PM.png?20200529151223',
    'Miyabi https://static.wikia.nocookie.net/magiarecord-en/images/c/cb/Miyabi_Shigure_Miyabi_Shigure.png/revision/latest/scale-to-width-down/400?cb=20191210112018',
    'Hagumu https://images.puella-magi.net/thumb/f/f7/Card_10304_l. png/300px-Card_10304_l.png?20200225160028',
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

record_side = [
    'Asuka https://static.wikia.nocookie.net/madoka/images/e/ec/Asuka_profile.png/revision/latest?cb=20200812070421',
    'Kanoko https://images.puella-magi.net/thumb/c/c1/Kanoko_profile.png/300px-Kanoko_profile.png?20170904041254',
    'Natsuki https://static.wikia.nocookie.net/magiarecord-en/images/2/21/Utsuho_Natsuki_Utsuho_Natsuki.png/revision/latest?cb=20190830113316',
    'Hinano Miyako https://images.puella-magi.net/thumb/4/45/Hinano_profile.png/300px-Hinano_profile.png?20170904110506',
    'Minagi https://static.wikia.nocookie.net/magiarecord-en/images/4/45/Minagi_Sasara_Minagi_Sasara.png/revision/latest?cb=20190830113012',
    'Nanaka https://static.wikia.nocookie.net/character-stats-and-profiles/images/4/43/Nanaka1.png/revision/latest?cb=20190116204310',
    'Emiri https://images.puella-magi.net/thumb/0/01/Emiri_profile.png/300px-Emiri_profile.png?20170904181132',
    'Shizuku https://images.puella-magi.net/thumb/2/23/Shizuku_profile.png/300px-Shizuku_profile.png?20170904182440',
    'Akira https://images.puella-magi.net/thumb/1/11/Akira_profile.png/300px-Akira_profile.png?20170904183037',
    'Manaka https://images.puella-magi.net/thumb/0/06/Manaka_profile.png/300px-Manaka_profile.png?20170904183509',
    'Ria https://images.puella-magi.net/thumb/3/3d/Ria_Ami_profile.png/300px-Ria_Ami_profile.png?20180423091839',
    'Natsume https://static.wikia.nocookie.net/magiarecord-en/images/7/7f/Natsume_Kako_Natsume_Kako.png/revision/latest?cb=20190829092143',
    'Kako https://static.wikia.nocookie.net/magiarecord-en/images/7/7f/Natsume_Kako_Natsume_Kako.png/revision/latest?cb=20190829092143',
    'Meiyui https://gamepress.gg/magiarecord/sites/magiarecord/files/2019-06/meiyui_magical.png',
    'Leila https://images.puella-magi.net/thumb/e/ee/Leila_Ibuki_profile.png/300px-Leila_Ibuki_profile.png?20180312112302',
    'Seika https://images.puella-magi.net/thumb/4/41/Seika_sousui_profile.png/300px-Seika_sousui_profile.png?20180312113204',
    'Mito https://images.puella-magi.net/thumb/c/c8/Mito_aino_profile.png/300px-Mito_aino_profile.png?20180312111600'
    'Awane https://images.puella-magi.net/thumb/2/24/Awane_Kokoro_4_star_card.png/300px-Awane_Kokoro_4_star_card.png?20171110123923',
    'Yukika https://images.puella-magi.net/thumb/d/d6/Card_30174_l.png/300px-Card_30174_l.png?20190917154946',
    'Sarasa https://images.puella-magi.net/thumb/7/7c/Sarasa_profile.png/300px-Sarasa_profile.png?20190524145522',
    'Ayaka https://static.wikia.nocookie.net/magiarecord-en/images/b/bf/Mariko_Ayaka_Mariko_Ayaka.png/revision/latest?cb=20190830112041',
    'Himika https://images.puella-magi.net/thumb/d/d9/Himika_Mao_profile.png/300px-Himika_Mao_profile.png?20180402121243',
    'Sakuya https://images.puella-magi.net/thumb/7/77/Card_30212_l.png/300px-Card_30212_l.png?20200127201651',
    'Aimi https://images.puella-magi.net/thumb/5/5d/Aimi_magia_record_profile.png/300px-Aimi_magia_record_profile.png?20171024003827',
    'Wakana https://static.wikia.nocookie.net/magiarecord-en/images/a/af/Wakana_Tsumugi_Wakana_Tsumugi.png/revision/latest/scale-to-width-down/400?cb=20200518152012',
    'Ren https://static.wikia.nocookie.net/character-stats-and-profiles/images/2/2c/Renisuzu.png/revision/latest?cb=20180910121900',
    'Konoha https://images.puella-magi.net/thumb/8/87/Konoha_profile_magia_record.png/300px-Konoha_profile_magia_record.png?20171010113340',
    'Hazuki https://images.puella-magi.net/thumb/6/6e/Hazuki_profile_magia_record.png/300px-Hazuki_profile_magia_record.png?20171010112848',
    'Ayame https://gamepress.gg/magiarecord/sites/magiarecord/files/2019-06/ayame_magical.png',
    'Masara https://static.wikia.nocookie.net/yuripedia/images/a/a2/Masara_profile.png/revision/latest?cb=20200424010905',
    'Konomi https://images.puella-magi.net/thumb/7/7b/Konomi_profile.png/300px-Konomi_profile.png?20170904194239',
    'Rika https://images.puella-magi.net/thumb/d/d1/Rika_Profile.png/300px-Rika_Profile.png?20170904200710',
    'Mayu https://images.puella-magi.net/thumb/d/d0/Mayu_profile.png/300px-Mayu_profile.png?20180323234317',
    'Sayuki https://images.puella-magi.net/thumb/d/db/Sayuki_PM.png/150px-Sayuki_PM.png?20190805015245',
    'Megumi https://static.wikia.nocookie.net/magiarecord-en/images/6/6b/Megumi_Moka_Megumi_Moka.png/revision/latest/scale-to-width-down/2000?cb=20200225151808',
    'Riko https://images.puella-magi.net/thumb/2/2b/Riko_Chiaki_Profile.png/300px-Riko_Chiaki_Profile.png?20181014200504',
    'Maria https://images.puella-magi.net/thumb/b/be/Card_30363_l.png/300px-Card_30363_l.png?20200413161257',
    'Mel https://images.puella-magi.net/thumb/5/5e/Meru_Magireco_Profile.png/300px-Meru_Magireco_Profile.png?20180521101132',
    'Mikura https://images.puella-magi.net/thumb/5/55/Card_30384_l.png/300px-Card_30384_l.png?20191223230849',
    'Seira https://static.wikia.nocookie.net/magiarecord-en/images/5/5a/Mihono_Seira_Mihono_Seira.png/revision/latest?cb=20191202134839',
    'Temari https://images.puella-magi.net/thumb/2/2d/Card_30403_l.png/300px-Card_30403_l.png?20191223230859',
    'Hotori https://ami.animecharactersdatabase.com/uploads/chars/68195-1058825310.png',
    'Meguru https://static.wikia.nocookie.net/magiarecord-en/images/b/b9/Hibiki_Meguru_Hibiki_Meguru.png/revision/latest/scale-to-width-down/2000?cb=20200309195148',
    'Eternal https://images.puella-magi.net/thumb/1/1c/Card_30434_l.png/300px-Card_30434_l.png?20190325194249',
    'Ranka https://images.puella-magi.net/thumb/7/79/Card_30443_l.png/300px-Card_30443_l.png?20200120203447',
    'Rion https://static.wikia.nocookie.net/magiarecord-en/images/a/af/Yuzuki_Rion_Yuzuki_Rion.png/revision/latest/scale-to-width-down/2000?cb=20200529180128',
    'Ryou https://images.puella-magi.net/thumb/9/91/Midori_Ryou_Profile.png/300px-Midori_Ryou_Profile.png?20181112234216',
    'Chika https://images.puella-magi.net/thumb/6/6b/Card_30473_l.png/300px-Card_30473_l.png?20200706160956',
    'Kanae https://images.puella-magi.net/thumb/d/dd/Kanae_magireco_profile.png/300px-Kanae_magireco_profile.png?20180521100333',
    'Yuuna https://images.puella-magi.net/thumb/c/c9/Card_30504_l.png/300px-Card_30504_l.png?20200529144014',
    'Jun https://static.wikia.nocookie.net/magiarecord-en/images/9/97/Kazari_Jun_Sprite.png/revision/latest/scale-to-width-down/280?cb=20200928082116',
    'Ashley https://images.puella-magi.net/thumb/d/d2/Card_30524_l.png/300px-Card_30524_l.png?20200331152021',
    'Ikumi https://images.puella-magi.net/thumb/c/cb/Makino_Ikumi_Profile.png/300px-Makino_Ikumi_Profile.png?20181112233434',
    'Mitsune https://images.puella-magi.net/thumb/b/bc/Card_30544_l.png/300px-Card_30544_l.png?20210322151042',
    'Sae https://images.puella-magi.net/thumb/0/0a/Card_30554_l.png/300px-Card_30554_l.png?20210430135639',
    'Rui https://images.puella-magi.net/thumb/9/96/Card_30564_l.png/300px-Card_30564_l.png?20200504181439',
    'Ryoko https://images.puella-magi.net/thumb/9/9f/Card_30584_l.png/300px-Card_30584_l.png?20200127201704',
    'Kushu https://images.puella-magi.net/thumb/5/53/Kushu_Iremei.png/300px-Kushu_Iremei.png?20210212170628',
    'Kuro https://images.puella-magi.net/thumb/f/fb/Kuro_profile.png/300px-Kuro_profile.png?20180216114946',
    'Yu https://images.puella-magi.net/thumb/c/c8/Yu_PM.png/200px-Yu_PM.png?20200514181639',
    'Kuroe https://static.wikia.nocookie.net/madoka/images/d/d8/Kuroe.png/revision/latest?cb=20200811020157',
    'Mabayu https://images.puella-magi.net/thumb/6/61/Aki_Mabayu_Profile_v1.png/150px-Aki_Mabayu_Profile_v1.png?20210425141619']

sidestory_list = ['Kazumi https://images.puella-magi.net/4/4b/PMMMO-KazumiFull.png?20130712122133',
                  'Umika https://images.puella-magi.net/thumb/8/82/Umika_magireco_profile.png/300px-Umika_magireco_profile.png?20171120192046',
                  'Kaoru https://images.puella-magi.net/thumb/3/3d/Kaoru_maki_magireco_profile.png/300px-Kaoru_maki_magireco_profile.png?20171120192506',
                  'Suzune https://images.puella-magi.net/thumb/9/96/Suzune_amano_magireco_profile.png/300px-Suzune_amano_magireco_profile.png?20180501085527',
                  'Arisa https://images.puella-magi.net/thumb/d/dd/Arisa_magireco_profile.png/300px-Arisa_magireco_profile.png?20180501085629',
                  'Matsuri https://images.puella-magi.net/thumb/9/9e/Card_40324_l.png/300px-Card_40324_l.png?20191031160303',
                  'Tsubaki https://images.puella-magi.net/thumb/5/5e/Card_40364_l.png/300px-Card_40364_l.png?20210125210656',
                  'Chisato https://images.puella-magi.net/thumb/4/43/Chisato_Shion_Magireco_Profile.png/300px-Chisato_Shion_Magireco_Profile.png?20180501090404',
                  'Haruka https://images.puella-magi.net/thumb/b/b4/Card_40353_l.png/300px-Card_40353_l.png?20191031161338',
                  'Tart https://static.wikia.nocookie.net/vsbattles/images/d/d1/IMG_5606.png/revision/latest?cb=20171009180555',
                  'Oriko https://images.puella-magi.net/thumb/0/01/Oriko_magia_record_profile.png/300px-Oriko_magia_record_profile.png?20171008175121',
                  'Yuuri https://i.imgur.com/g5Y1Xpg.png']


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


# survival command
@client.command()
async def survival(ctx):
    username = ctx.message.author.name
    embed_sur = discord.Embed(title="Survival Rating",
                              description="Let's see...     " + username + ", I would say you have a " +
                                          str(random.randint(1,
                                                             99)) + "% chance of surviving Madoka Magica. You would die " +
                                          str(random.choice(place_sur)) + " and you died because you " +
                                          str(random.choice(death_sur)), color=0xb30000)
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


# Record Side Command
@client.command()
async def recordside(message):
    await message.channel.send("Here's a random one... " + random.choice(record_side) + " is a good pick! (I think..)")


# Side Story Command
@client.command()
async def sidestory(message):
    await message.channel.send(
        "Here's a random one... " + random.choice(sidestory_list) + " is a good pick! (I think..)")


@client.command()
async def changelog(ctx):
    changelog_embed = discord.Embed(title="Change log for v0.4.2", description="Here is the change log for 0.4.2! Enjoy!", color=0xa80000)
    changelog_embed.add_field(name="~New naming system!", value="Now we are on 0.4.2, so I can release bug fixes without having to wait till .5 or .6", inline=False)
    changelog_embed.add_field(name="~Bug fixes", value="Fixed pictures in sidestory and others, **DM ME ANY BUGS YOU FIND :heart:**", inline=False)
    await ctx.send(embed=changelog_embed)


# HEEP COMMAND!
@client.command()
async def help(ctx):
    page1 = discord.Embed(title="Page 1/2 | Commands", description="Well it seems like you need help. Noob. Anyways here's the commands you wanted.", color=0xa80000)
    page1.set_thumbnail(url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")
    page1.add_field(name="k!help", value="Shows this menu, how impressive.", inline=False)
    page1.add_field(name="k!couple", value="Generates A Couple!", inline=True)
    page1.add_field(name="k!ship", value="Generates a ship from a list of Madoka Magica Characters!!", inline=True)
    page1.add_field(name="k!survival", value="A command that randomly generates chances of surviving madoka magica", inline=True)
    page1.add_field(name="k!magica", value="A command that randomly selects a character from the anime Madoka Magica", inline=True)
    page1.add_field(name="k!rebellion ", value="A command that randomly selects a character from Madoka Magica Rebellion", inline=True)
    page1.add_field(name="k!record ", value="A command that randomly selects a character from Madoka Magica Record", inline=True)
    page1.add_field(name="k!recordside ", value="A command that randomly selects a side story character from Madoka Magica Record", inline=True)
    page1.add_field(name="k!changelog ", value="Its a change log for the latest update!", inline=True)
    page1.set_image(url='https://i.imgur.com/Sz4Ogro.png')

    page2 = discord.Embed(title="Page 2/2 | Keywords", color=0xa80000, description="Keywords of the Kyoko bot!")
    page2.add_field(name="Madoka/Magical Girl/Meguca", value="It is suffering..", inline=True)
    page2.add_field(name="Dance", value="  I'll send a funny gif!", inline=True)
    page2.add_field(name="Sayaka", value="Ill react to any kind of message with the keyword of sayaka", inline=True)
    page2.add_field(name="Kyubey", value="Hehe, f/// you kyubey", inline=True)
    page2.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")

    pages = [page1, page2]

    message = await ctx.send(embed=page1)
    # await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')

    # await message.add_reaction('⏭')

    def check(reaction, user_help):
        return user_help == ctx.author

    i = 0
    reaction = None

    while True:
        # if str(reaction) == '⏮':
        #  i = 0
        #    await message.edit(embed=pages[i])
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        # elif str(reaction) == '⏭':
        #    i = 2
        #    await message.edit(embed=pages[i])

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


# Waiting

# Fact Command
# @client.command()
# async def fact(message):
#    await message.channel.send(
#        "No. Command in progress")


# (random.choice(fact_list))


# ########################### #


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return
    if "Madoka" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "madoka" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "Magical girl" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "magical girl" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "meguca" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "Meguca" in message.content:
        await message.channel.send("✨being Meguca is suffering✨")
    if "dance" in message.content:
        await message.channel.send(
            'https://media1.tenor.com/images/2d32f3383f87f8d0822e2e4b327e2537/tenor.gif?itemid=19119793')
    if "Dance" in message.content:
        await message.channel.send(
            'https://media1.tenor.com/images/2d32f3383f87f8d0822e2e4b327e2537/tenor.gif?itemid=19119793')

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
