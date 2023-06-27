from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import datetime
import asyncio

import os

TOKEN = "6127733344:AAE8dVlw86p6kt1BqtXFqb8KPgsi6wIxHbo"
bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

TEXTS = ["Ты зайка <3", "Ты солнце <3", "Ты котик <3", "Я люблю рыжих", "Ты девочка Кирюши <3"]


def compliment():
    return random.choice(TEXTS)


def is_not_night():
    current_time = datetime.datetime.utcnow().time()
    print(current_time)
    start_time = datetime.time(6, 0)  # Define your desired start time for daytime
    end_time = datetime.time(21, 0)  # Define your desired end time for daytime

    # Check if the current time is within the desired time range
    if start_time <= current_time <= end_time:
        return True
    else:
        return False


@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer("NOT Implemented")
    if message.from_id == 380442849 and message.text == "/ping":
        tmp = compliment()
        await bot.send_message(781095277, tmp)
        await bot.send_message(380442849, "{} to {}".format(tmp, 781095277))
    if message.from_id == 781095277:
        await bot.send_message(380442849, message.text + "from Inna")
        await bot.send_message(781095277, "отправил Кириллу")

    if message.text == "/time":
        await bot.send_message(380442849, str(is_not_night()))


async def send_periodic_message():
    while True:
        time = random.randint(int(3600 * 5 / 6), int(3600 * 7 / 6))
        await asyncio.sleep(time)  # Change the interval as per your requirement
        chat_id = 781095277  # Replace with the actual chat ID
        message = compliment()  # Replace with your desired message content
        if is_not_night():
            await bot.send_message(chat_id, message)
            await bot.send_message(380442849, message + "to inna")


loop = asyncio.get_event_loop()
loop.create_task(send_periodic_message())
executor.start_polling(dp, skip_updates=True)
