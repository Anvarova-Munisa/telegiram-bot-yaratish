from aiogram import Router,filters,types
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
    elif msg.fail:
        await msg.reply("siz fail yubordingiz")
    elif msg.document:
        await msg.reply("siz dokument yubordingiz")
    elif msg.sticker:
        await msg.reply("siz stiker yubordingiz")
    elif msg.frist_name:
        await msg.reply("siz foydalanuvchi nomingizni yubordingiz")
    elif msg.music:
        await msg.reply("siz musiqa yubordingiz")
    else:
        await msg.reply("nomalum malumot")


@rt.message()
async def start(msg: types.Message):
    if msg.group_chat_created:
        await msg.answer("yaratildi")
        # print(msg.group_chat_created)
    elif msg.new_chat_members:
        await msg.answer("keldi")
        # print(msg.new_chat_members)
    elif msg.left_chat_member:
        await msg.answer("ketti")
        # print(msg.left_chat_member)
    elif msg.new_chat_photo:
        await msg.answer("new rasm")
        # rasm = msg.new_chat_photo
        # print(rasm)
        # await msg.answer_photo(rasm)
    elif msg.delete_chat_photo:
        await msg.answer("delete rasm")
        # print(msg.delete_chat_photo)