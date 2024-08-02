from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = '6991565738:AAH410s3f9Ak0_zI-jiU5x5Mh4Tjy4qezUA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()
data = get_all_products()

kb = InlineKeyboardMarkup(resize_keyboard=True)
b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
b2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(b1)
kb.add(b2)

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b3 = KeyboardButton(text='Рассчитать')
b4 = KeyboardButton(text='Информация')
b5 = KeyboardButton(text='Купить')
b6 = KeyboardButton(text='Регистрация')

Inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])

kb1.add(b3)
kb1.add(b4)
kb1.add(b5)
kb1.add(b6)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RigistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RigistrationState.username.set()


@dp.message_handler(state=RigistrationState.username)
async def set_username(message, state):
    # await message.answer('Введите имя пользователя (только латинский алфавит):')
    if is_include(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        await RigistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email')
        await RigistrationState.email.set()


@dp.message_handler(state=RigistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RigistrationState.age.set()


@dp.message_handler(state=RigistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешна', reply_markup=kb1)
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    count = 1
    for i in data:
        with open(f'{count}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        count += 1
    await message.answer('Выберите продукт для покупки', reply_markup=Inline)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def age_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f'Ваша норма калорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора')
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
