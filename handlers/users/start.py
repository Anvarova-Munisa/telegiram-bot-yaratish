from aiogram import Router,types,filters




router = Router()

@router.message(filters.Command("start",prefix="%.+/-="))
async def test(msg: types.Message):
    n = "Xush kelibsiz"
    n += " agar  yordam kerak bolsa /help tugmasini bosing"
    await msg.answer(n)


















    # await msg.reply("botdan kerakli malumot oldingiz degan umiddamn")
    # await msg.answer_photo("https://yandex.uz/maps/org/room_mafia/229701263103/gallery/")
    # await msg.answer_dice(emoji=DiceEmoji.BOWLING)
    # await msg.delete()
    # await msg.pin()
    # await msg.forward(6820934345)
    # await msg.copy_to(6820943454)
