from aiogram import types

from loader import db, dp
from bot.utils.misc.decorators import check_if_user_is_registered


@dp.message_handler(commands="start")
@check_if_user_is_registered
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}, I'm ShareBot and I will help you manage your shared expenses. Add me to group and enter /help for more info.")
