from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from src.database import CRUD
from src.button_text.button import help_button, support_button, get_data_button
from src.config import TOKEN


TOKEN = f"{TOKEN}"


bot = Bot(token=TOKEN)
c = CRUD()
router = Router()

"""################################################СОЗДАНИЕ АДМИНИСТРАТОРА################################################"""


@router.message(F.text == "5617")
async def create_su(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Изменить статус пользователя")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    c.create_user(message.chat.id, 5000, 1, "ok")
    await message.answer("Status: ok", reply_markup=keyboard)



""" ################################################АДМИН ПАНЕЛЬ##################################################### """
class Form(StatesGroup):
    id = State()


@router.message(F.text == "Изменить статус пользователя")
async def update_status_user(message: types.Message, state: FSMContext):
    if c.get_admin_id(1) == message.chat.id:
        await state.set_state(Form.id)
        await message.answer("Введите id")
    else: await message.answer("Вы не админ")


@router.message(Form.id)
async def form_id(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    data = await state.get_data()
    await state.clear()
    query = c.get_status_user(data['id'])
    kb = [help_button, support_button, get_data_button,]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    if query == 'ok':
        c.update_val(message.text, 'not_sub')
        await message.answer("Статус изменен, теперь not_sub")
    else:
        c.update_val(message.text, 'ok')
        await bot.send_message(data['id'], text="Подписка снова активна", reply_markup=keyboard)
        await message.answer("Статус изменен, теперь ok")
