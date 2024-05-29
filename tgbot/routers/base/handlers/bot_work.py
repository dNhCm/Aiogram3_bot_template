from aiogram import Router, Bot
from aiogram.exceptions import TelegramBadRequest

from misc.logger import logger
from tgbot.data.config import get_config


async def startup(bot: Bot):
    admins = get_config().tgbot.admins
    for admin in admins:
        try:
            await bot.send_message(
                chat_id=admin,
                text="Bot was started!"
            )
        except TelegramBadRequest:
            logger.error(f"!!! ADMIN WITH {admin} ID DOESN'T START CHAT WITH ME !!!")


async def shutdown(bot: Bot):
    admins = get_config().tgbot.admins
    for admin in admins:
        try:
            await bot.send_message(
                chat_id=admin,
                text="Bot was stopped!"
            )
        except TelegramBadRequest:
            logger.error(f"!!! ADMIN WITH {admin} ID DOESN'T START CHAT WITH ME !!!")


def register(router: Router):
    router.startup.register(startup)
    router.shutdown.register(shutdown)
