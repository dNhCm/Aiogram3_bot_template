
from typing import Any
import json

from aiogram import Router
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.handlers import MessageHandler, MessageHandlerCommandMixin
from aiogram.methods import SendMessage
from aiogram.types import Message

from tgbot.keyboards.web_app.some_inlinekeyboard import web_app_inline_keyboard


class WebAppHandler(MessageHandler, MessageHandlerCommandMixin):
    async def handle(self) -> Any:
        return SendMessage(
            chat_id=self.from_user.id,
            text="Check web app",
            reply_markup=web_app_inline_keyboard()
        )


async def web_app(message: Message):
    response = json.loads(message.web_app_data.data)

    BMI = response["weight"] / response["height"]**2
    answer = f"{response['full_name']} have "
    if BMI < 16:
        answer += "an acute weight deficiency"
    elif 16 <= BMI <= 18.5:
        answer += "an underweight"
    elif 16.5 < BMI <= 25:
        answer += "a normal weight"
    elif 25 < BMI <= 30:
        answer += "an excess body weight"
    elif 30 < BMI <= 35:
        answer += "an obesity of the first degree"
    elif 35 < BMI <= 40:
        answer += "an obesity of the second degree"
    elif BMI > 40:
        answer += "an obesity of the third degree"

    await message.answer(answer)


def register(router: Router):
    router.message.register(WebAppHandler, Command('web_app'))
    router.message.register(web_app, content_type=ContentType.WEB_APP_DATA)
