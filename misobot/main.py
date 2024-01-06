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

@dp.message_handler(commands=['man'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CVy_pRAABAoLdZJTPhmp4ZX5VChm2JbGyQsb49XgAAgkDAAKpmQVT5F7cw3tIZe4vBA')
    await message.reply_media_group(media=media)



@dp.message_handler(commands=['voices'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CSL8EywABA4eqY2xdKt2JsCw0OuXLEbw6rTTNWIgAAv4DAALS811SayYWwSvwyyMrBA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['incredible'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CUMx1MQABBuUwZZm7CeMOOBcG06okVNTL_1zk5e0AAiwDAAJjvRVT_4gfVO9nA6k0BA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['reward'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CVy_pRAABBXn_ZZm-NPDq83jAHbGcO6ENY-d9GvIAAiINAAIRZYBS9yGluoQzI640BA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['пынявый'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CUMx1MQABBuSoZZm66yV11CK6d0wTe-HykJMHpxMAAssQAAI2uJBSOk3mknxvmUs0BA')
    await message.reply_media_group(media=media)

@dp.message_handler(commands=['🟩'])
async def send_message(message: types.Message):
    media = types.MediaGroup()
    media.attach_video('CgACAgQAAx0CVy_pRAABBXrUZZnDbhbg7RE2oT4-vLdk-7EqF48AAu4QAAJRfShSNGTGTm-uGqA0BA')
    await message.reply_media_group(media=media)

#@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
#async def send_message(message:types.Message):
#    await message.reply(message.document.file_id)
    
#this following bit i borrowed from @jDan735's jdanbot    
@dp.message_handler(commands=["reverse"])
async def reverse_gif(message: types.Message):
    reply = message.reply_to_message

    if reply.animation:
        (video := reply.animation).file_size
    elif reply.sticker and reply.sticker.is_video:
        (video := reply.sticker).file_size
    elif reply.video:
        (video := reply.video).file_size
    else:
        raise KeyError("Reply to GIF | video | video sticker")

    if video.file_size > 5000000:
        await message.reply("errors.is_too_big_gif")
        return

    await video.download(destination_file="test3.mp4")

    process = (
        ffmpeg.input("test3.mp4")
        .output("test4.mp4", vf="reverse")
        .overwrite_output()
        .run_async()
    )

    process.communicate()

    await message.reply_animation(animation=open("test4.mp4", "rb"))

    os.remove("test3.mp4")
    os.remove("test4.mp4")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
