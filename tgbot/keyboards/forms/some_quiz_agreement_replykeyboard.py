from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def quiz_agreement_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text="Yes")
    keyboard.button(text="No")

    return keyboard.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Choose answer: "
    )
