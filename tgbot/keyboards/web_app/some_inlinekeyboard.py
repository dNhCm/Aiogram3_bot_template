from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.data.config import get_config


def web_app_reply_keyboard() -> InlineKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(
        text="Open Web App",
        web_app=WebAppInfo(url=get_config().tgbot.web_apps['urls']['app'])
    )

    return keyboard.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Open Web app using button below!",
        one_time_keyboard=True
    )
