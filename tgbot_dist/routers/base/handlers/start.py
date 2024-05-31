
from typing import Any

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.handlers import MessageHandler, MessageHandlerCommandMixin
from aiogram.methods import SendMessage


class StartHandler(MessageHandler, MessageHandlerCommandMixin):
    async def handle(self) -> Any:
        return SendMessage(
            chat_id=self.from_user.id,
            text="Hello World!"
        )


def register(router: Router):
    router.message.register(StartHandler, CommandStart())
