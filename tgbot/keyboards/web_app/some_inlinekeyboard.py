from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.callback_datas.shop import Product


def web_app_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Open Web App",
        web_app=WebAppInfo(url="url/to/web-app")
    )

    return keyboard.as_markup()
