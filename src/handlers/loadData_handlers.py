from aiogram import F, types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.button_text.button import help_button, support_button, month_button, week_button
from src.handlers.admin_handlers import c

router = Router()

""" Получение данных из файла """


@router.message(F.text == "Получить данные")
async def load_data(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="На месяц", callback_data="Месяц"))
    builder.add(types.InlineKeyboardButton(text="На неделю", callback_data="Неделя"))
    query = c.get_status_user(message.from_user.id)
    if query == "ok":
        file = open("data.txt")
        file = file.read()
        await message.answer(text=file)
    else:
        await message.answer(text="Нет подписки")
        await message.answer(text="Выберите желаемый тариф", reply_markup=builder.as_markup())
