from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChattypeFilter
from common.functions import get_random_dog


user_private_router = Router()
user_private_router.message.filter(ChattypeFilter(['private']))

@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} and have a nice day")

@user_private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I'm a simple bot that can greet you. Just type /start to start")

@user_private_router.message(Command('dog'))
async def cmd_dog(message: Message):
    await message.answer_photo(get_random_dog())

@user_private_router.message(F.photo)
async def get_photo(message: Message):
    await message.reply('This is photo but i need some text to help you')

@user_private_router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello! How are you?")