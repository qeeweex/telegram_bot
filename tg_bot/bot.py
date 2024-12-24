import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from handlers import commands  

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)  
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())