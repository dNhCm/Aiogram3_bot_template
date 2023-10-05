from tgbot.keyboards.some_replykeyboard import reply_keyboard
from . import bot


async def feedback(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="You have used the button with callback query!",
        reply_markup=reply_keyboard()
    )
