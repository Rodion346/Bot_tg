from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.button_text.button import help_button, support_button, month_button, week_button
from src.button_text.text import start_txt

router = Router()

""" Первый запуск """


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="На месяц", callback_data="Месяц"))
    builder.add(types.InlineKeyboardButton(text="На неделю", callback_data="Неделя"))
    await message.answer(start_txt, reply_markup=builder.as_markup())


