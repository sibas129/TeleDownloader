from aiogram import Router, F, types

router = Router()


# Обработчик для загрузки файла
@router.message(F.document | F.video | F.photo)
async def download_file(message: types.Message):
    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
    elif message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name
    else:
        file_id = message.photo[-1].file_id
        file_name = message.photo[-1].file_name

    #    file = await bot.get_file(file_id)
    #    downloaded_file = await bot.download_file(file_path=file.file_path)
    await message.answer(f'Following file is uploaded:\n{file_name}\nID: {file_id}')
