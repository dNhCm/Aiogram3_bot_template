from datetime import timedelta, datetime
from typing import Any

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.keyboards.forms.some_quiz_agreement_replykeyboard import quiz_agreement_keyboard
from tgbot.misc.handlers.custom_message_handler import CustomMessageHandler
from tgbot.utils.states.quiz import QuizForm


class Quiz(CustomMessageHandler):
    async def handle(self) -> Any:
        await self.bot.send_message(
            chat_id=self.from_user.id,
            text=f"Fast quiz\nIt's fast quiz with simple questions for testing bot"
        )

        await start(self.update.message, self.state)


async def cancel(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.answer("Come back soon, please!")
    await state.clear()


async def start(message: Message, state: FSMContext):
    await message.answer("How old are you?")
    await state.set_state(QuizForm.GET_OLD)


async def get_old(message: Message, state: FSMContext):
    await state.update_data(old=message.text)
    await message.answer("Do you like Aiogram 3?", reply_markup=quiz_agreement_keyboard())
    await state.set_state(QuizForm.LIKE_AIOGRAM3)


async def yes_like_aiogram3(message: Message, state: FSMContext):
    await state.update_data(like_aiogram=message.text)
    await message.answer("It's so awesome!")
    await message.answer("Do you like our quiz?", reply_markup=quiz_agreement_keyboard())
    await state.set_state(QuizForm.LIKE_QUIZ)


async def no_like_aiogram3(message: Message, state: FSMContext):
    await state.update_data(like_aiogram=message.text)
    await message.answer("Oh.. It's bad(")
    await message.answer("Do you like our quiz?", reply_markup=quiz_agreement_keyboard())
    await state.set_state(QuizForm.LIKE_QUIZ)


async def unknown_like_aiogram3(message: Message, state: FSMContext):
    await message.answer("I don't understand(")
    await message.answer("Do you like Aiogram 3?", reply_markup=quiz_agreement_keyboard())
    await state.set_state(QuizForm.LIKE_AIOGRAM3)


async def finish(message: Message, state: FSMContext):
    context_data = await state.get_data()
    text = f"{message.from_user.full_name}, your answers:\r\n" \
           f"Your age is {context_data['old']}\r\n" \
           f"Do you like Aiogram 3? - {context_data['like_aiogram']}"
    await message.answer(text=text)
    await state.clear()


def finish_scheduler_job(scheduler: AsyncIOScheduler, message: Message, state: FSMContext):
    scheduler.add_job(
        finish,
        trigger="date",
        run_date=datetime.now() + timedelta(seconds=10),
        kwargs={
            "message": message,
            "state": state
        }
    )


async def yes_finish(message: Message, state: FSMContext, scheduler: AsyncIOScheduler):
    await state.update_data(like_quiz=message.text)
    await message.answer("We are happy!\r\nHave a nice day!")
    finish_scheduler_job(scheduler, message, state)


async def no_finish(message: Message, state: FSMContext, scheduler: AsyncIOScheduler):
    await state.update_data(like_quiz=message.text)
    await message.answer("We are disappointed(\r\nBut for the next time will be better!!")
    finish_scheduler_job(scheduler, message, state)


async def unknown_finish(message: Message, state: FSMContext, scheduler: AsyncIOScheduler):
    finish_scheduler_job(scheduler, message, state)


def register(router: Router):
    router.message.register(Quiz, Command(commands="quiz"))
    router.message.register(cancel, Command(commands="cancel"), F.text.casefold() == "/cancel")
    router.message.register(get_old, QuizForm.GET_OLD)
    router.message.register(yes_like_aiogram3, QuizForm.LIKE_AIOGRAM3, F.text.casefold() == "yes")
    router.message.register(no_like_aiogram3, QuizForm.LIKE_AIOGRAM3, F.text.casefold() == "no")
    router.message.register(unknown_like_aiogram3, QuizForm.LIKE_AIOGRAM3)
    router.message.register(yes_finish, QuizForm.LIKE_QUIZ, F.text.casefold() == "yes")
    router.message.register(no_finish, QuizForm.LIKE_QUIZ, F.text.casefold() == "no")
    router.message.register(unknown_finish, QuizForm.LIKE_QUIZ)
