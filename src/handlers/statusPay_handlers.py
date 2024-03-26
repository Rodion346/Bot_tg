from aiogram import F, types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.button_text.button import help_button, support_button, get_data_button
from src.handlers.admin_handlers import bot, c

router = Router()


""" Отправка сообщения админу для подтверждения статуса оплаты """


@router.callback_query(F.data == "Оплатил")
async def check_pay(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=None)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text=f"Оплачен", callback_data=f"{callback.message.chat.id}"))
    builder.add(types.InlineKeyboardButton(text=f"Не оплачен", callback_data=f"notpay_{callback.message.chat.id}"))
    await callback.message.answer(text="Ожидайте когда администратор проверит статус оплаты, вы получите уведомление.")
    await bot.send_message(chat_id=c.get_admin_id(1), text=f"Подтвердите оплату для пользователя\n"
                                                           f"ID в комментарии к оплате: {callback.message.chat.id}", reply_markup=builder.as_markup())

""" Отправка статуса оплаты пользователю """


@router.callback_query(F.data)
async def status_pay(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=None)
    if "notpay_" in callback.data:
        kb = [help_button, support_button,]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        action = callback.data.split("_")[1]
        await bot.send_message(chat_id=int(action), text="Оплата не прошла\n"
                                                         "Обратитесь в поддержку", reply_markup=keyboard)
    else:
        c.update_val(callback.data, "ok")
        kb = [help_button, support_button, get_data_button]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await bot.send_message(chat_id=callback.data, text='Оплата прошла успешно', reply_markup=keyboard)

