from aiogram import Router,types


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


