from aiogram import F, types, Router
from src.button_text.button import help_button, support_button, get_data_button
from src.button_text.text import help_txt, support_txt

router = Router()

@router.message(F.text == "Помощь")
async def help(message: types.Message):
    kb = [help_button, support_button, get_data_button,]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text=help_txt, reply_markup=keyboard)


@router.message(F.text == "Связаться с поддержкой")
async def support(message: types.Message):
    kb = [help_button, support_button, get_data_button,]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text=support_txt, reply_markup=keyboard)
