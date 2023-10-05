from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.callback_datas.shop import Product


def inline_keyboard() -> InlineKeyboardMarkup:
    """
    Creating of the Inline Keyboard works in 3 stages:
    1. Initialization InlineKeyboardBuilder
    2. Make buttons with button() method; Use CallBackData subclass for better data experience (U can create one in tgbot.utils.callback_datas)
    3. Resize your keyboard by adjust() method; every argument is count of buttons in line

    :keyboard: variable with InlineKeyboardBuilder
    :return: Markup of the created InlineKeyboard
    """

    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Potato",
        callback_data=Product(
            name='potato',
            mass=2,
            price=5
        )
    )
    keyboard.button(
        text="Tomato",
        callback_data=Product(
            name='tomato',
            mass=5,
            price=10
        )
    )
    keyboard.button(
        text="Onion",
        callback_data=Product(
            name='onion',
            mass=1,
            price=4
        )
    )

    return keyboard.as_markup()
