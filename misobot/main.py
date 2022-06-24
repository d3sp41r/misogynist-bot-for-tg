import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '<token>'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['women'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CUMx1MQABApuJYrUhEeaDvenC2KhlnHWyQ-0w2d0AAhQDAAJgTLVSTjSefpf73VApBA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['msg_id'])
async def send_message(message: types.Message):
    await message.reply(message.message_id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

