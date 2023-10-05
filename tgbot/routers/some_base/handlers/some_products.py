from typing import Any

from aiogram import Router

from tgbot.misc.handlers.custom_callback_query_handler import CustomCallbackQueryHandler
from tgbot.routers.some_base.scripts.some_callbackquery_feedback import feedback
from tgbot.utils.callback_datas.shop import Product


class SendProductInfo(CustomCallbackQueryHandler):
    """
    Use My class CustomCallbackQueryHandler from tgbot.misc.handlers.custom_callback_query_handler
    if you use CallbackData for callback_data
    And import CallbackQueryHandler from aiogram.handlers
    if you use usual callback_data, like "data0:data1:data2..."

    ! Notation !
    If you code in some IDE than use type annotation for local data var with your CallbackData to display hints
    And dismiss the type support warning;
    Otherwise, don't use annotations to avoid getting a TypeError.
    """

    async def handle(self) -> Any:
        data: Product = self.callback_data
        text = f"""This is a {data.name}s
Which contains {data.mass} kg
And costs ${data.price}"""
        await self.message.answer(text=text)
        await feedback(self.message.chat.id)

        return self.update.callback_query.answer()


def register(router: Router):
    router.callback_query.register(SendProductInfo, Product.filter())
