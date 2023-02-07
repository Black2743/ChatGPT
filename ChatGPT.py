  GNU nano 5.4                            TelegramBot.py                                      
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5972044151:AAGocm3kJ1gWnbNi0dUhIaQIWobFNrC1M3c'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
