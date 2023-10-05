
from typing import Awaitable, Any, Dict, Callable

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject

from tgbot.models.users import Users


class Counter(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        user_id = data['event_from_user'].id

        await Users.insert(user_id)

        await event.bot.send_message(
            chat_id=user_id,
            text=str(self.counter)
        )

        return await handler(event, data)


def register(dp: Dispatcher):
    dp.update.middleware.register(Counter())
