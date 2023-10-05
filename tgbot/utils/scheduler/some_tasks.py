from datetime import datetime, timedelta

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.models.users import Users


async def send_message_time(bot: Bot):
    users_id = await Users.get_table()
    for user_id in users_id:
        await bot.send_message(
            chat_id=user_id,
            text="Was send message for appointed time"
        )


async def send_message_cron(bot: Bot):
    users_id = await Users.get_table()
    for user_id in users_id:
        await bot.send_message(
            chat_id=user_id,
            text="Was send message by cron method"
        )


async def send_message_interval(bot: Bot):
    users_id = await Users.get_table()
    for user_id in users_id:
        await bot.send_message(
            chat_id=user_id,
            text="You will see this message every 30 minutes"
        )


def register(scheduler: AsyncIOScheduler, bot: Bot):
    scheduler.add_job(
        send_message_time,
        trigger="date",
        run_date=datetime.now()+timedelta(seconds=10),
        kwargs={"bot": bot}
    )
    scheduler.add_job(
        send_message_cron,
        trigger="cron",
        start_date=datetime.now(),
        hour=datetime.now().hour,
        minute=datetime.now().minute + 1,
        kwargs={"bot": bot}
    )
    scheduler.add_job(
        send_message_interval,
        trigger="interval",
        minutes=30,
        kwargs={"bot": bot}
    )
