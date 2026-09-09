from aiogram import Router,filters,types
from aiogram.types import user

rt = Router()
@rt.message()
async def start(msg: types.Message):
    if msg.location:
        await msg.reply("siz lokatsiya yubordingiz")
    elif msg.gift:
        await msg.reply("siz gift yubordingiz")
    elif msg.photo:
        await msg.reply("siz photo yubordingiz")
    elif msg.video:
        await msg.reply("siz video yubordingiz")
    elif msg.document:
        await msg.reply("siz dokument yubordingiz")
    elif msg.sticker:
        await msg.reply("siz stiker yubordingiz")
    elif msg.text:
        await msg.reply("siz matn  yubordingiz")
    elif msg.audio:
        await msg.reply("siz audio  yubordingiz")
    else:
        await msg.reply("nomalum malumot")


@rt.message()
async def start(msg: types.Message):
    user = msg.from_user.first_name 
    if msg.group_chat_created:

        await msg.answer(f" {user}yangi guruh yaratildi")
        # print(msg.group_chat_created)
    elif msg.new_chat_members:
        new_user = msg.new_chat_members[0].first_name
        await msg.answer(f"{new_user} ni qoshdi")
        # print(msg.new_chat_members)
    elif msg.left_chat_member:
        left_user = msg.left_chat_member.first_name
        await msg.answer(f"{left_user}ni chiqarb yubordi")
        # print(msg.left_chat_member)
    elif msg.new_chat_title:
        await msg.answer(f"{msg.new_chat_title}ga ozgartirdi")
        # print(user)
    elif msg.new_chat_photo:
        await msg.answer(f"{msg.new_chat_photo[-1].file_id} guruh rasmini ozgartirdi")
        # rasm = msg.new_chat_photo
        # print(rasm)
        # await msg.answer_photo(rasm)
    elif msg.delete_chat_photo:
        await msg.answer(f"{msg.delete_chat_photo} rasmini ochirdi")
        # print(msg.delete_chat_photo)