from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name;
    await message.answer(f'Здравствуйте, {user_name}! мы рады приветствовать вас в нашем магазине.')

@dp.message_handler()
async def invalid_command(message: types.Message):
    await message.reply('Неверная команда.')

if __name__ == '__main__':
    executor.start_polling(dp)