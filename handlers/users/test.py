
from aiogram import Router,types
# from aiogram.filters import Command
# import datetime
# import asyncio
# import json
# from datetime import timedelta
# from aiogram import  F
#
router = Router()
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

@router.message()
async def test(msg: types.Message):
    if msg.entities:
        await msg.delete()
    elif msg.caption_entities:
        await msg.delete()


    # if msg.caption:
    #     await msg.answer("bu caption")





































