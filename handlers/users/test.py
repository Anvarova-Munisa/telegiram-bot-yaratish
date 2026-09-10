
# from aiogram import Router,types
# from aiogram.filters import Command
# import datetime
# import asyncio
# import json
# from datetime import timedelta
# from aiogram import  F
#
# router = Router()
# @router.message(Command("test"))
# async def test(msg:types.Message):
#     info = msg.chat
#     n = f"id: {info.id}\n"
#     n += f"type:{info.type}\n"
#     n += f"first_name: {info.first_name}\n"
#     if info.last_name:
#         familya = info.last_name
#     else:
#         familya = "mavjud emas"
#     n += f"last_name: {familya}\n"
#     n += f"username: {info.username}\n"
#     await msg.answer(n)
# @router.message(Command("user"))
# async def user_info(msg:types.Message):
#     info = msg.chat
#     n = f"id: {info.id}\n"
#     n += f"First_name: {info.first_name}\n"
#     if info.last_name:
#         familya = info.last_name
#     else:
#         familya = "mavjud emas"
#     n += f"Last_name: {familya}\n"
#     n += f"Username: @{info.username}\n" if info.username else "Username: mavjud emas\n"
#     if msg.from_user:
#         n += f"Til (language_code): {msg.from_user.language_code}\n"
#         n += f"Premium foydalanuvchimi: {'HA' if msg.from_user.is_premium else "Yoq"}\n"
#         n += f"Bot emasmi: {"Ha" if not msg.from_user.is_bot else "Yoq"}\n"
#     await msg.answer(n)
#
# @router.message(Command("soat"))
# async def soat_cmd(msg:types.Message):
#     await msg.answer(f"{(msg.date + datetime.timedelta(hours=5)).strftime("%H:%S:%M")}")
#
#
# @router.message(Command("salom"))
# async def salom_cmd(msg:types.Message):
#     await msg.reply(f"{msg.message_id}")
# #
# #
# # guruhlar = []
# # @router.message()
# # async def media_handler(msg:types.Message):
# #     if msg.media_group_id:
# #        if msg.media_group_id in guruhlar:
# #            return
# #        guruhlar.append(msg.media_group_id)
# #     await msg.answer("rasmlani qabul qildim")
#
#
#
#
#
#
#
# router = Router()
# handling_groups = set()
#
#
# @router.message(F.forward_date)
# async def get_forward_dict(msg: types.Message):
#
#     if msg.media_group_id:
#         if msg.media_group_id in handling_groups: return
#         handling_groups.add(msg.media_group_id)
#         asyncio.create_task(asyncio.sleep(1.5)).add_done_callback(lambda _: handling_groups.discard(msg.media_group_id))
#
#     if msg.forward_from_chat:
#         manba = msg.forward_from_chat.title
#         manba_id = msg.forward_from_chat.id
#         turi = "chat_yoki_kanal"
#     elif msg.forward_from:
#         manba = msg.forward_from.first_name
#         manba_id = msg.forward_from.id
#         turi = "foydalanuvchi"
#     else:
#         manba = msg.forward_sender_name
#         manba_id = "yashirilgan"
#         turi = "yopiq_profil"
#
#     uzb_vaqt = msg.forward_date + timedelta(hours=5)
#     sana = uzb_vaqt.strftime('%d.%m.%Y %H:%M')
#
#     forward_data = {
#         "manba_nomi": manba,
#         "telegram_id": manba_id,
#         "turi": turi,
#         "sana_vaqt": sana
#     }
#
#
#     dict_matni = json.dumps(forward_data, ensure_ascii=False, indent=2)
#
#     await msg.answer(f"```json\n{dict_matni}\n```", parse_mode="MarkdownV2")
#
# guruhlar = []
#
# # 1. PIN qilingan xabarlarni tutish (Tepada turishi shart!)
# @router.message(F.pinned_message)
# async def pinned_handler(msg: types.Message):
#     pinned = msg.pinned_message
#     txt = pinned.text or pinned.caption or "Media xabar"
#     user = msg.from_user.first_name if msg.from_user else "Admin"
#     await msg.answer(f"📌 {user} \"{txt}\"ni qadadi")
#
# # 2. Faqat rasmlar/media guruhlar kelganda ishlash
# @router.message()
# async def media_handler(msg: types.Message):
#     if msg.media_group_id:
#         if msg.media_group_id in guruhlar:
#             return
#         guruhlar.append(msg.media_group_id)
#         await msg.answer("rasmlarni qabul qildim")




    # if msg.caption:
    #     await msg.answer("bu caption")


# from aiogram import Router, types
# router = Router()
# @router.message()
# async def reklma(msg: types.Message):
#     if msg.entities:
#         await msg.delete()
#     elif msg.caption_entities:
#         await msg.delete()

# from aiogram import Router, types
# router = Router()
# @router.message()
# async def test(msg: types.Message):
#     if msg.caption:
#         await msg.answer("siz rasm va xabar yubordingiz")
#     elif msg.photo:
#         await msg.answer("siz rasm yubordingiz")
#     elif msg.video:
#         await msg.answer("siz yubordingiz")


from aiogram import Router, types
router = Router()
tulki = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Foxes_of_Island_Beach_State_Park_New_Jersey_%2816138030480%29.jpg/960px-Foxes_of_Island_Beach_State_Park_New_Jersey_%2816138030480%29.jpg"
ayiq = "https://avatars.mds.yandex.net/i?id=cc308ccfda95fa5579b535c3d40a845f4baa8f1d-12644621-images-thumbs&n=13"
bori = " https://i.ytimg.com/vi/EWFQNqmxf8E/hq2.jpg?sqp=-oaymwEoCOADEOgC8quKqQMcGADwAQH4AYwCgALgA4oCDAgAEAEYaiBqKGowDw==&amp;rs=AOn4CLAEzus5Zm-MwuY_TuGA0Eyb6omiTw"
sher = "https://i.pinimg.com/736x/4b/a7/54/4ba7540f800e243c63ad11b34c3de447.jpg"
yolbars = " https://avatars.mds.yandex.net/i?id=db4d7670513b91c04b121460d31e333b43b5db77-12587729-images-thumbs&n=13"
quyon = "https://i.pinimg.com/736x/78/ac/80/78ac8081bef36780e8326eea8221502e.jpg"
fil ="https://avatars.mds.yandex.net/i?id=bf9cffcc8c8573a0fd3c66323ee7ebd33265464c-4566301-images-thumbs&n=13"
jirafa = "https://static1-repo.aif.ru/1/1a/3047359/034797c065331ab6eaf38ac6dfba5ac1.webp"
zebra = "https://i.pinimg.com/originals/31/33/41/313341b8f662927bf7cfa2ba239920b6.jpg"
maymun = "https://img.magnific.com/free-photo/funny-monkey-outdoors_23-2150844166.jpg?semt=ais_hybrid&w=740"
panda = "https://avatars.mds.yandex.net/i?id=3d5368d387531d38c365ef176a02c56d053dc532-4469622-images-thumbs&n=13"
sigir = "https://avatars.mds.yandex.net/i?id=62faec3e57a6ff61d38e596adf1740b4e015e0e8-12384509-images-thumbs&n=13 "
it = "https://i.pinimg.com/originals/30/33/cf/3033cf31b0d1632d5011320261d47fd2.jpg"
mushuk = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Oczy_kota_domowego_-Aw58-.JPG/500px-Oczy_kota_domowego_-Aw58-.JPG"
tovuq = "https://avatars.mds.yandex.net/i?id=639ec0efaf0b44cb972646728d6a962f6f6183bd-5716853-images-thumbs&n=13"
qush = "https://i.ytimg.com/vi/VEL4_WMcNr8/maxresdefault.jpg "
sichqon = "https://avatars.mds.yandex.net/i?id=02728728ff397ea1f1680dbdcb3699e960a23b34-13096454-images-thumbs&n=13 "
tumsoh = "https://i.ytimg.com/vi/pXdO7S-Fy88/maxresdefault.jpg "
gorilla  = " https://media.istockphoto.com/id/1750304305/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B0%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F-%D0%B7%D0%B0%D0%BF%D0%B0%D0%B4%D0%BD%D0%B0%D1%8F-%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B3%D0%BE%D1%80%D0%B8%D0%BB%D0%BB%D0%B0-%D0%B4%D0%BE%D0%BC%D0%B8%D0%BD%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B9-%D1%81%D0%B0%D0%BC%D0%B5%D1%86-%D1%81%D0%B8%D0%B4%D0%B8%D1%82-%D0%B2-%D0%BD%D0%B8%D0%B7%D0%B8%D0%BD%D0%B0%D1%85-%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BB%D1%83%D0%B3%D0%B0.jpg?s=612x612&w=0&k=20&c=gH4axQw3M0TmWUuZo2sGw31uNKt6gTvG1Y_hoCfOHcE="
ot = "https://i.ytimg.com/vi/ARoYeU9vdPA/maxres2.jpg?sqp=-oaymwEoCIAKENAF8quKqQMcGADwAQH4Ac4FgAK0BooCDAgAEAEYOSBjKHIwDw==&amp;rs=AOn4CLDHh4E1_pYBQMdMwS7dLJJNuWckzw "
tuya = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/07._Camel_Profile%2C_near_Silverton%2C_NSW%2C_07.07.2007.jpg/1280px-07._Camel_Profile%2C_near_Silverton%2C_NSW%2C_07.07.2007.jpg "

@router.message()
async def test_hayvonlar(msg: types.Message):
    if msg.text:
        soz = msg.text.lower()

        if soz == "tulki":
            await msg.reply_photo(tulki)
        elif soz == "qush":
            await msg.reply_photo(qush)
        elif soz == "gorilla":
            await msg.reply_photo(gorilla)
        elif soz == "ot":
            await msg.reply_photo(ot)
        elif soz == "tumsoh":
            await msg.reply_photo(tumsoh)
        elif soz == "sigir":
            await msg.reply_photo(sigir)
        elif soz == "sichqon":
            await msg.reply_photo(sichqon)
        elif soz == "panda":
            await msg.reply_photo(panda)
        elif soz == "ayiq":
            await msg.reply_photo(ayiq)

        elif soz == "bo'ri" or soz == "boʻri":
            await msg.reply_photo(bori)

        elif soz == "sher":
            await msg.reply_photo(sher)

        elif soz == "yo'lbars" or soz == "yoʻlbars":
            await msg.reply_photo(yolbars)

        elif soz == "quyon":
            await msg.reply_photo(quyon)

        elif soz == "fil":
            await msg.reply_photo(fil)

        elif soz == "jirafa":
            await msg.reply_photo(jirafa)

        elif soz == "zebra":
            await msg.reply_photo(zebra)

        elif soz == "maymun":
            await msg.reply_photo(maymun)

        elif soz == "it":
            await msg.reply_photo(it)

        elif soz == "mushuk":
            await msg.reply_photo(mushuk)
        else:
            await msg.reply("kechirasiz bunday hayvon turi meni royxatimda yo'q buning uchun uzur so'rayman va keyinchalik bu hayvon turini"
                            "royxatimga qoshishga harakt qilamn ")




































