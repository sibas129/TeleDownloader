from aiogram import Router, F, types

router = Router()

# Обработчик для загрузки файла
@router.message(F.document | F.video | F.photo)
async def download_file(message: types.Message):
    if message.document:
        file_id = message.document.file_id
    elif message.video:
        file_id = message.video.file_id
    else:
        file_id = message.photo[-1].file_id

#    file = await bot.get_file(file_id)
#    downloaded_file = await bot.download_file(file_path=file.file_path)
    await message.answer(f'Файл {file_id} загружен')
