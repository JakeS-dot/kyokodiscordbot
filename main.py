# Imports
import asyncio
import json
import random

import discord
from discord.ext import commands

# Todo: 8b
#   hug
#   say
#   fight
#   coinflip

#
# JAKE REMINDER TO CHANGE THE TOKEN IF YOUR COPY AND PASTING THE CODE! CHANGE IT FROM NOT THE KYOKO (TEST) TOKEN, BUT KYOKO (MAIN) TOKEN

# Credentials
# TOKEN FOR FOR KYOKO (MAIN) IS ODUzMzk2Mjg4MTYyMTAzMzA3.YMUxOg.cg1IbTAlJwXRxjiacHkN4oL3CBE
# TOKEN FOR KYOKO (TEST) IS ODQ5NjEzOTEyMDI1OTg5MTUw.YLdunQ.-MfU88k5sPNxQ0svpuNlDLRNTS0
TOKEN = 'ODUzMzk2Mjg4MTYyMTAzMzA3.YMUxOg.cg1IbTAlJwXRxjiacHkN4oL3CBE'

# Create bot
client = commands.Bot(command_prefix='k!')
activity_string = 'TOO MANY NAGITO EDITS | v0..6.1 | Made by xx-jake-xx#5302 | On {} servers'.format(len(client.guilds))
client = commands.Bot(command_prefilx='k!',
                      activity=discord.Activity(type=discord.ActivityType.watching,
                                                name=activity_string)
client.remove_command('help')

# lists for commands
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

ball_list = ['It is certain', 'Without a doubt', 'It is decidedly so', 'Yes', 'Most Likely', 'Reply Hazy, Try again',
             'Ask again later', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My Reply Is No',
             'Outlook not so good', 'Very Doubtful']

hug_gifs = ['https://i.gifer.com/TR2G.gif', 'https://thumbs.gfycat.com/FarAdvancedGrouper-size_restricted.gif',
            'https://i.gifer.com/LIKl.gif']

fight_gifs = ['https://64.media.tumblr.com/135357ab0c4d347848d9d2a05affa8d0/tumblr_mrocoq7Fz91scsnv1o2_r3_400.gif',
              'https://i.pinimg.com/originals/4d/17/0d/4d170d8d76741a9c2c1996227b2e18ae.gif',
              'https://thumbs.gfycat.com/GrizzledMilkyFluke-max-1mb.gif',
              'https://i.pinimg.com/originals/47/bf/ce/47bfcea600dd3b14eae3a749c5656dbd.gif',
              'https://64.media.tumblr.com/09c858ef85be3428eb179232869b2458/tumblr_n3cmlwCccm1sial0xo2_500.gif']


# ship command
@client.command()
async def ship(ctx):
    ship_cmd = discord.Embed(title=('In my opinion, ' + (random.choice(ship_list)) + ' and ' + (
        random.choice(ship_list)) + ' would be a great ship!'), color=0xa00000)
    ship_cmd.set_footer(text=(random.choice(ship_dis)))
    ship_cmd.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/801105512933752882/845050099678576640/unknown.png")
    ship_cmd.set_image(url="https://i.pinimg.com/originals/45/09/c7/4509c76ea660d121c11c303a31908c23.png")
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
                                          str(random.choice(death_sur)), color=0xa00000)
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


# 8b command
@client.command()
@commands.cooldown(1.0, 60.0, commands.BucketType.user)
async def eightball(message):
    await message.channel.send(random.choice(ball_list))


# Hug command
@client.command()
@commands.cooldown(1.0, 5.0, commands.BucketType.user)
async def hug(ctx, *, member: discord.Member = None):
    try:
        if member is None:
            await ctx.send(ctx.message.author.mention + " has been hugged!")
            await ctx.send(random.choice(hug_gifs))
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + "... I can hug you if y-you want?")
                await asyncio.sleep(1.3)
                await ctx.send("*sighs* come here.")
            else:
                await ctx.send(member.mention + " has been hugged by " + ctx.message.author.mention + "!")
                await ctx.send(random.choice(hug_gifs))

    except:
        await ctx.send("Invalid Input")


@client.command()
@commands.cooldown(1.0, 5.0, commands.BucketType.user)
async def fight(ctx, *, member: discord.Member = None):
    try:
        if member is None:
            await ctx.send(ctx.message.author.mention + " has been challenged to fight!!")
            await ctx.send(random.choice(fight_gifs))
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + "challenges... himself? to fight!")
            else:
                await ctx.send(member.mention + " has been challenged to fight by " + ctx.message.author.mention + "!")
                await ctx.send(random.choice(fight_gifs))
    except:
        await ctx.send("Invalid Input")


@client.command()
@commands.cooldown(1.0, 0.5, commands.BucketType.user)
async def say(ctx, say_text=None):
    if say_text is None:
        await ctx.send("I CANT SAY NOTHING STUPID!")
        return
    await ctx.send(say_text)


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
    changelog_embed = discord.Embed(title="Change Log For v0.6.1", color=0xa80000)
    changelog_embed.add_field(name="This Update Is More Focused On :sparkles: Fun :sparkles: ", value="Were at 737 lines of code, and we added 4 commands!", inline=False)
    changelog_embed.add_field(name="k!eightball", value="Ask kyoko a question and she'll pull out her magic 8 ball!", inline=False)
    changelog_embed.add_field(name="k!hug", value="Hug someone... we all need it", inline=False)
    changelog_embed.add_field(name="k!fight", value="Challenge someone to fight!", inline=False)
    changelog_embed.add_field(name="Major Revamps and bug fixes", value=":bug: :dizzy_face: ", inline=False)
    changelog_embed.add_field(name="k!say", value="Kyoko will say what ever you want!", inline=False)
    changelog_embed.add_field(name="plz report any bugs to xx-jake-xx#5302... ty", value=":heart:", inline=False)
    await ctx.send(embed=changelog_embed)


# HEEP COMMAND!
@client.command()
@commands.cooldown(1.0, 10.0, commands.BucketType.user)
async def help(ctx):
    page1 = discord.Embed(title="Help!",
                          description="Hello! I am Kyoko Sakura, you know, that magical girl from Madoka Magica.. I hope to serve you well in your server, to entertain, to laugh at, to crush your poor little heart. I can do over 15 commands and keywords! The creator (me) has worked very, very hard on this. I hope I did my best, and I hope I can give you a bot of a lifetime... ",
                          color=0xa80000)
    page1.add_field(name="Bot Invite", value="https://top.gg/bot/853396288162103307", inline=False)
    page1.add_field(name="Creator", value="xx-jake-xx#5302 (Only friend/dm me for a bug report, ty)", inline=True)
    page1.set_image(url='https://i.imgur.com/Sz4Ogro.png')

    page2 = discord.Embed(title="Page 2/4 | Commands", color=0xa80000,
                          description="Anime/Other Commands of the Kyoko bot!")
    page2.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")
    page2.add_field(name="k!help", value="Shows this menu, how impressive.", inline=False)
    page2.add_field(name="k!sidestory",
                    value="A command that randomly generates a side story character from a custom list", inline=True)
    page2.add_field(name="k!ship", value="Generates a ship from a list of Madoka Magica Characters!!", inline=True)
    page2.add_field(name="k!survival", value="A command that randomly generates chances of surviving madoka magica",
                    inline=True)
    page2.add_field(name="k!magica", value="A command that randomly selects a character from the anime Madoka Magica",
                    inline=True)
    page2.add_field(name="k!rebellion ",
                    value="A command that randomly selects a character from Madoka Magica Rebellion", inline=True)
    page2.add_field(name="k!record ", value="A command that randomly selects a character from Madoka Magica Record",
                    inline=True)
    page2.add_field(name="k!recordside ",
                    value="A command that randomly selects a side story character from Madoka Magica Record",
                    inline=True)
    page2.add_field(name="k!changelog ", value="Its a change log for the latest update!", inline=True)

    page3 = discord.Embed(title="Page 3/4 | Keywords", color=0xa80000, description="Keywords of the Kyoko bot!")
    page3.add_field(name="Madoka/Magical Girl/Meguca", value="It is suffering..", inline=True)
    page3.add_field(name="Dance", value="  I'll send a funny gif!", inline=True)
    page3.add_field(name="Sayaka", value="Ill react to any kind of message with the keyword of sayaka", inline=True)
    page3.add_field(name="Kyubey", value="Hehe, f/// you kyubey", inline=True)
    page3.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")

    page4 = discord.Embed(title="Page 4/4 | Economy/Fun", color=0xa80000,
                          description="Economy Commands of the Kyoko Discord™ bot!")
    page4.add_field(name="k!wallet", value="Shows your e-wallet! ", inline=True)
    page4.add_field(name="k!beg", value="Beg for some koins!", inline=True)
    page4.add_field(name="k!patrol", value="Go on witch patrol and maybe get some koins?", inline=True)
    page4.add_field(name="k!daily", value="Use this command once per day to hang out with some magical girls!",
                    inline=True)
    page4.add_field(name="k!slots", value="Bet your money in the slot machine! Earn up ", inline=True)
    page4.add_field(name="k!eightball", value="Kyoko gets out her eight ball!", inline=True)
    page4.add_field(name="k!fight", value="Fight a user!", inline=True)
    page4.add_field(name="k!hug", value="Hug a user!", inline=True)
    page4.add_field(name="k!say", value="I'll say whatever! ", inline=True)
    page4.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/844706643936935987/f1d040d84ee02cfcf643465297571f26.png?size=128")

    pages = [page1, page2, page3, page4]

    message = await ctx.send(embed=page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user_help):
        return user_help == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            # Make V To add 1 to that number when adding a new embed page
            if i < 3:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            #   V same here
            i = 3
            await message.edit(embed=pages[i])

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


#########################
# OOOOOOOOOOO DAMM ITS ECONOMY TIMEE
beg_list = ['**Kyosuke**', '**Madoka**', '**Jake XD**', '**Homura**', '**Mami**', '**Sayaka**', '**Hitomi**',
            '**Kyoko**', '**Garfield**']


##########
# Daily Command
@client.command(pass_context=True)
@commands.cooldown(1.0, 43200.0, commands.BucketType.user)
async def daily(ctx):
    user = ctx.author
    users = await get_bank_data()
    daily_earnings = random.randrange(113, 358)
    seed_chance = ["1", "2", "3", "4", "5"]
    flipchoice = random.choice(seed_chance)
    if flipchoice == '1':
        await ctx.send("oh, you also got a greif seeed")
        users[str(user.id)]["bank"] += 1
        with open("bank.json", 'w') as f:
            json.dump(users, f)
    await ctx.send(
        "Are budget couldn't afford to but custom story embeds, so u got " + str(daily_earnings) + " koins ig")

    users[str(user.id)]["wallet"] += daily_earnings
    with open("bank.json", 'w') as f:
        json.dump(users, f)


# Fight Command
@client.command(pass_context=True)
@commands.cooldown(1.0, 1800.0, commands.BucketType.user)
async def hunt(ctx):
    user = ctx.author
    users = await get_bank_data()
    seed_chance = ["1", "2", "3", "4", "5", "6", "7", '8', '9', '10', '11',
                   '12', '13', '14', '15', '16', '17', '18', '19', '20']
    flipchoice = random.choice(seed_chance)
    fight_earnings = random.randrange(62, 276)
    if flipchoice == '1':
        await ctx.send("oh, you also got a greif seed")
        users[str(user.id)]["bank"] += 1
        with open("bank.json", 'w') as f:
            json.dump(users, f)

    await ctx.send(
        "Are budget couldn't afford to but custom story embeds, so u got " + str(fight_earnings) + " koins ig")

    users[str(user.id)]["wallet"] += fight_earnings
    with open("bank.json", 'w') as f:
        json.dump(users, f)


# Wallet command
@client.command(aliases=['bal'])
async def wallet(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed = discord.Embed(title=str(ctx.author.name) + "'s Wallet!!", color=0xa00000)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="Soul Gem Status", value="ok i haven't gotten to death crap so u know in progress",
                    inline=False)
    embed.add_field(name="Koins", value=wallet_amt, inline=False)
    embed.add_field(name="Greif Seeds", value=bank_amt, inline=False)
    await ctx.send(embed=embed)


# Beg command
@client.command()
@commands.cooldown(1.0, 59.1, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(random.choice(beg_list) + " gave you " + str(earnings) + " Koins!")

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)


# Slotss
@client.command(pass_context=True)
@commands.cooldown(1.0, 30.0, commands.BucketType.user)
async def slots(ctx, amount=None):
    if amount is None:
        await ctx.send("Please enter an amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("You don't have that much money!")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    slots = ['<:emoji8:859178701094912030>>', '<:emoji2:859178728852160512>', '<:emoji3min:859179625762652201>',
             '<:emoji4:859178815745949696>', '<:emohi5min:859179597262618624>', '<:emoji6:859178897181376552>',
             '<:emoji7:859178915113336832>']
    slot1 = slots[random.randint(0, 5)]
    slot2 = slots[random.randint(0, 5)]
    slot3 = slots[random.randint(0, 5)]

    slotOutput = '| {} | {} | {} |\n'.format(slot1, slot2, slot3)

    ok = discord.Embed(title="Slots Machine", color=discord.Color(0xa00000))
    ok.add_field(name="{}\nWon".format(slotOutput), value=f'You won {2 * amount} koins')

    won = discord.Embed(title="Slots Machine", color=discord.Color(0xa00000))
    won.add_field(name="{}\nWon".format(slotOutput), value=f'You won {3 * amount} koins')

    lost = discord.Embed(title="Slots Machine", color=discord.Color(0xa00000))
    lost.add_field(name="{}\nLost".format(slotOutput), value=f'You lost {1 * amount} koins')

    if slot1 == slot2 == slot3:
        await update_bank(ctx.author, 3 * amount)
        await ctx.send(embed=won)
        return

    if slot1 == slot2:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(embed=ok)
        return

    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(embed=lost)
        return


# Economy technical crap
async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('bank.json', 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open('bank.json', 'r') as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('bank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal


#################
# BYE ECONOMY
# Hello cool down code
@slots.error
async def slots_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'You have already done your daily event, try again 12 hours from your last use!'
        await ctx.send(msg)
    else:
        raise error


@fight.error
async def fight_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'You have already fought recently! Get some rest! Your body will let you fight in 30 minuets!'
        await ctx.send(msg)
    else:
        raise error


@beg.error
async def beg_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@eightball.error
async def eightball_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@fight.error
async def fight_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


#########
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
