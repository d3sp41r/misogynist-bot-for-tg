import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '<token>'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['women'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CSL8EywABAe6XYrWqc4eVSQcrpjiA2PzP--rXHwUAAhQDAAJgTLVSmKVerjkQLTUpBA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['msg_id'])
async def send_message(message: types.Message):
    await message.reply(message.message_id)
    
@dp.message_handler(commands=['men'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CUMx1MQABAqUSYrniZhVtxCS4wp68TFsO5NLlQUYAAtwJAAIP9LhTBzfa89_SY6ApBA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['cuh'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgIAAx0CVy_pRAABARC0Y-LdkriLIMnXcVQiddLPO4SnpAkAAhcnAAI61hlL0wQEHPMCKkQuBA')
    await message.reply_media_group(media=media)
    
@dp.message_handler(commands=['voices'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CSL8EywABA4eqY2xdKt2JsCw0OuXLEbw6rTTNWIgAAv4DAALS811SayYWwSvwyyMrBA')
    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

