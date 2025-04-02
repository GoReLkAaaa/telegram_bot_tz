# from dotenv import load_dotenv
# from aiogram.filters import CommandStart
# from aiogram import Bot, Dispatcher, types
# import os
# import asyncio
#
# load_dotenv()
#
# bot = Bot(token=os.getenv('TOKEN_ADMIN'))
# dp = Dispatcher()
#
# @dp.message(CommandStart())
# async def start_command(message: types.Message):
#     await message.answer("Это была команда старт")
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# asyncio.run(main())