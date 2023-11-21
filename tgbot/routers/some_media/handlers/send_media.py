from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo

from misc.root import get_root


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(get_root() + "/tgbot/data/media/audio.mp3", filename="Heathen")
    await bot.send_audio(chat_id=message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile(get_root() + "/tgbot/data/media/document.pdf")
    await bot.send_document(chat_id=message.chat.id, document=document)


async def get_media_group(message: Message, bot: Bot):
    photo = InputMediaPhoto(
        type="photo",
        media=FSInputFile(get_root() + "/tgbot/data/media/photo.jpg"),
        caption="It's a photo!"
    )
    video = InputMediaVideo(
        type="video",
        media=FSInputFile(get_root() + "/tgbot/data/media/video.mp4"),
        caption="It's a video!"
    )
    media = [photo, video]
    await bot.send_media_group(chat_id=message.chat.id, media=media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(get_root() + "/tgbot/data/media/photo.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


async def get_video(message: Message, bot: Bot):
    video = FSInputFile(get_root() + "/tgbot/data/media/video.mp4")
    await bot.send_video(chat_id=message.chat.id, video=video)


async def get_sticker(message: Message, bot: Bot):
    photo = FSInputFile(get_root() + "/tgbot/data/media/photo.jpg")
    await bot.send_sticker(chat_id=message.chat.id, sticker=photo)


async def get_video_note(message: Message, bot: Bot):
    video = FSInputFile(get_root() + "/tgbot/data/media/video_note.mp4")
    await bot.send_video_note(chat_id=message.chat.id, video_note=video)


async def get_voice(message: Message, bot: Bot):
    audio = FSInputFile(get_root() + "/tgbot/data/media/audio.mp3")
    await bot.send_voice(chat_id=message.chat.id, voice=audio)


def register(router: Router):
    router.message.register(get_audio, Command(commands="audio"), flags={"chat_action": "upload_document"})
    router.message.register(get_document, Command(commands="document"), flags={"chat_action": "upload_document"})
    router.message.register(get_media_group, Command(commands="media_group"), flags={"chat_action": "upload_photo"})
    router.message.register(get_photo, Command(commands="photo"), flags={"chat_action": "upload_photo"})
    router.message.register(get_video, Command(commands="video"), flags={"chat_action": "upload_video"})
    router.message.register(get_sticker, Command(commands="sticker"), flags={"chat_action": "choose_sticker"})
    router.message.register(get_video_note, Command(commands="video_note"), flags={"chat_action": "upload_video_note"})
    router.message.register(get_voice, Command(commands="voice"), flags={"chat_action": "record_voice"})

