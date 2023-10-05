
from . import bot
from tgbot.keyboards.some_replykeyboard import reply_keyboard


async def script(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="This message was send from some script",
        reply_markup=reply_keyboard()
    )
