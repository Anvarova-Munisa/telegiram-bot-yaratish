import datetime


from aiogram import Router,types
from aiogram.filters import Command
router = Router()
@router.message(Command("soat"))
async def get_time_command(msg:types.Message):
    vaqt = datetime.datetime.now().strftime("%H:%M:%S")
    await msg.answer(f"Hozirgi vaqt: {vaqt}")
