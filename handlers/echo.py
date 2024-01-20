from aiogram import Router, types

router = Router()


@router.message()
async def echo_message(message: types.Message):
    try:
        await message.answer("Use files only, please")
    except TypeError:
        await message.reply(text="Error((((")
