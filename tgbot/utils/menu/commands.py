from aiogram import Bot
from aiogram.types import BotCommand


async def register_my_commands(bot: Bot):
    return await bot.set_my_commands(
        [
            BotCommand(
                command="start",
                description="Starts bot"
            ),
            BotCommand(
                command="pay",
                description="Payment for some product"
            ),
            BotCommand(
                command="quiz",
                description="Starts quick quiz"
            ),
            BotCommand(
                command="web_app",
                description="Gives you keyboard to open web app"
            ),
            BotCommand(
                command="audio",
                description="Get some audio"
            ),
            BotCommand(
                command="document",
                description="Get some document"
            ),
            BotCommand(
                command="media_group",
                description="Get the media group"
            ),
            BotCommand(
                command="photo",
                description="Get some photo"
            ),
            BotCommand(
                command="sticker",
                description="Get some sticker"
            ),
            BotCommand(
                command="video",
                description="Get some video"
            ),
            BotCommand(
                command="video_note",
                description="Send the video note"
            ),
            BotCommand(
                command="voice",
                description="Send voice message"
            )
        ]
    )
