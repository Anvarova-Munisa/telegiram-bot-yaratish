import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.settings import BOT_TOKEN
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.test import router as test_router
dp = Dispatcher()

async def main() :
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )
    dp.include_router(help_router)
    dp.include_router(start_router)
    dp.include_router(test_router)


    await dp.start_polling(bot)
if __name__ == "__main__":
    print("Bot ishga tushmoqda..")
    asyncio.run(main())
