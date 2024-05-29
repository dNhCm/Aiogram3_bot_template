from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Router
from aiogram.types import TelegramObject

from tgbot.utils.scheduler import scheduler


class Scheduler(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data['scheduler'] = scheduler
        return await handler(event, data)


def register(router: Router):
    router.message.middleware.register(Scheduler())
