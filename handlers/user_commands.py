from aiogram import Router, types
from aiogram.filters import Command, CommandStart

import keyboard

# from keyboards import reply

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!", reply_markup=keyboard.main_kb)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm a file worker bot.\nSend me a file!"
    await message.answer(text=text)
