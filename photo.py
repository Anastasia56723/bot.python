import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '2019302491:AAFS80zm_gr6EUsBvEL5g9RVlDR8Itsrl4c'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(content_types='text')
async def main(message: types.Message):
         if message.text=='хочу капибару' or message.text=='привет':
             _keyboard = [
        [types.KeyboardButton('Да')], 
        [types.KeyboardButton('Нет')],
    ]
             keyboard = types.ReplyKeyboardMarkup(keyboard=_keyboard)

             await message.reply("Тебе нравиться моя фотография?", reply_markup=keyboard) 
         pic1 = InputFile("C:/Users/a.stepanushkina/Desktop/awdawdawd/vodosvinka-ili-kapibara.jpg")
         await bot.send_photo(message.from_user.id, pic1,caption='Нравится?') 




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
