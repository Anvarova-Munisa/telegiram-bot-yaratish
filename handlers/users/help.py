from aiogram import Router,types
from aiogram.filters import Command
router = Router()

@router.message(Command("help"))
async def help(msg: types.Message):
    await msg.answer("bu botdan foydalanish uchun oldin unga /start tugmasini bosing\n\n"
                     "yoki yordam olishni hohlasangiz /help tugmasini bosing\n\n")
