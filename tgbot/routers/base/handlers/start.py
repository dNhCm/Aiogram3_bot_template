
from typing import Any

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.handlers import MessageHandler, MessageHandlerCommandMixin
from aiogram.methods import SendMessage

from tgbot.keyboards.some_inlinekeyboard import inline_keyboard
from tgbot.models.users import Users


class StartHandler(MessageHandler, MessageHandlerCommandMixin):
    async def handle(self) -> Any:
        await self.bot.send_message(
            chat_id=self.from_user.id,
            text='\n'.join(await Users.get_table())
        )
        return SendMessage(
            chat_id=self.from_user.id,
            text=str(self.command.args),
            reply_markup=inline_keyboard()
        )


def register(router: Router):
    router.message.register(StartHandler, CommandStart())
