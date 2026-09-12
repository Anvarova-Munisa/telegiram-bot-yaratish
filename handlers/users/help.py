from aiogram import Router,types
from aiogram.filters import Command
router = Router()

@router.message(Command("help"))
async def help(msg: types.Message):
    await msg.answer("Bu botdan qanday foydalanishingiz  mumkun?\n\n"
                     "1) Hayvonlar haqida malumot va rasmlar\n\n"
                     "2) soat sana va kun\n\n"
                     "3) ozingiz haqingizdagi malumotlarni kiritishingiz \n\n"
                     "keyinchalik yana foydalanish uchun malumot va boshqa narsalar qoshamn")
