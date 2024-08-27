
from aiogram.types import Message
from aiogram import Router
from filters.chat_filters import ChattypeFilter

user_group_router = Router()
user_group_router.message.filter(ChattypeFilter(['group', 'supergroup']))

bad_words = {'bad', 'word', 'bad_word', 'badword'}

@user_group_router.message()
@user_group_router.edited_message()
async def check_words(message:Message):
    if bad_words.intersection(set(message.text.lower().split())):
        await message.delete()
        await message.text.replace('*')
        await message.answer("You can't use this word here")
    else:
        await message.answer("Your message is ok")