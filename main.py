from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

INVALID_COMMAND_MESSAGE = 'Что-то пошло не так. Проверте правильность команды или исполните её позже.'

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Наши товары').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Наши товары').add('Корзина').add('Контакты').add('Панель админа')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if is_admin(user_id):
        await message.answer(
            f'Здравствуйте, {user_name}! Вы автаризованы как админ.',
            reply_markup=main_admin
        )
    else:
        await message.answer(
            f'Здравствуйте, {user_name}! Мы рады приветствовать вас в нашем магазине.',
            reply_markup=main
        )


@dp.message_handler(commands=['id'])
async def start(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'ID: {user_id}')


@dp.message_handler(text=['Наши товары'])
async def catalog(message: types.Message):
    await message.answer(f'Товары отсутствуют.')


@dp.message_handler(text=['Корзина'])
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста.')


@dp.message_handler(text=['Контакты'])
async def contacts(message: types.Message):
    await message.answer(f'Наши контакты.')


@dp.message_handler(text=['Панель админа'])
async def contacts(message: types.Message):
    user_id = message.from_user.id
    if is_admin(user_id):
        await message.answer(f'Вы вошли в панель админа.', reply_markup=admin_panel)
    else:
        await message.reply(INVALID_COMMAND_MESSAGE)


@dp.message_handler()
async def invalid_command(message: types.Message):
    await message.reply(INVALID_COMMAND_MESSAGE)


def is_admin(user_id: int):
    return user_id == int(os.getenv('ADMIN_ID'))


if __name__ == '__main__':
    executor.start_polling(dp)
