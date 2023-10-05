from aiogram.fsm.state import StatesGroup, State


class QuizForm(StatesGroup):
    GET_OLD = State()
    LIKE_AIOGRAM3 = State()
    LIKE_QUIZ = State()
