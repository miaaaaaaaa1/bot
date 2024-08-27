import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import find_dotenv, load_dotenv
import os
from headlers.user_private import user_private_router
from headlers.user_group import user_group_router
from common.bot_command_list import listOfCommands
from aiogram.types import BotCommandScopeAllPrivateChats

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()



async def main():
    dp.include_routers(user_private_router)
    dp.include_routers(user_group_router)
    await bot.set_my_commands(commands=listOfCommands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

try:
   asyncio.run(main())
except KeyboardInterrupt:
    print("End of work")