import datetime

from aiogram import F, types, Router
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pyperclip import copy

from src.handlers.admin_handlers import c, bot
from src.button_text.button import help_button, support_button, get_data_button
from src.button_text.text import pay_comment, card_number

router = Router()

""" Выбор тарифа """


@router.callback_query(F.data == "Месяц")
async def tarif_month(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=None)
    query = c.get_status_user(callback.message.chat.id)
    if query == "ok":
        time_user = c.get_endtime_user(callback.message.chat.id)
        time_user = time_user - datetime.datetime.now()
        await callback.message.answer(text=f"Подписка уже активна\nДней до конца действия: {time_user.days}")
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Оплатил", callback_data="Оплатил"))
        await callback.message.answer(pay_comment, reply_markup=builder.as_markup())
        await callback.message.answer(card_number)
        await callback.message.answer(f"{callback.message.chat.id}")
        c.create_user(callback.message.chat.id, 30)


@router.callback_query(F.data == "Неделя")
async def tarif_week(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                                 message_id=callback.message.message_id, reply_markup=None)
    query = c.get_status_user(callback.message.chat.id)
    if query == "ok":
        time_user = c.get_endtime_user(callback.message.chat.id)
        time_user = time_user - datetime.datetime.now()
        await callback.message.answer(text=f"Подписка уже активна\nДней до конца действия: {time_user.days}")
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Оплатил", callback_data="Оплатил"))
        await callback.message.answer(pay_comment, reply_markup=builder.as_markup())
        await callback.message.answer(card_number)
        await callback.message.answer(f"{callback.message.chat.id}")
        c.create_user(callback.message.chat.id, 7)


@router.callback_query(F.data == "День")
async def tarif_day(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=None)
    query = c.get_status_user(callback.message.chat.id)
    if query == "ok":
        time_user = c.get_endtime_user(callback.message.chat.id)
        time_user = time_user - datetime.datetime.now()
        await callback.message.answer(text=f"Подписка уже активна\nДней до конца действия: {time_user.days}")
    else:
        kb = [help_button, support_button, get_data_button]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await callback.message.answer("Бесплатный период активен", reply_markup=keyboard)
        c.create_user(callback.message.chat.id, 1)
        c.update_val(callback.message.chat.id, "ok")