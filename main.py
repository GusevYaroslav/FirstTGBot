import logging
import random
from random import randint
from aiogram import Bot, Dispatcher, executor, types

global i
i = 0

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

API_TOKEN = '6343130135:AAFDdhJp2pvvS7zNnZS9Py8aoeNXiTgMcAY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    i += 1


@dp.message_handler(commands=['description'])
async def send_welcome(message: types.Message):
    await message.reply("Bot's description")
    i += 1


'''
@dp.message_handler()
async def echo(message: types.Message):
    symb_num = random.randint(0, len(alf) - 1)
    await message.answer(alf[symb_num])
'''


@dp.message_handler(commands=['count'])
async def send_welcome(message: types.Message):
    await message.reply(i)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == '0' or message.text == 0:
        await message.answer('Yes')

    else:
        await message.answer('No')

    i += 1


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
