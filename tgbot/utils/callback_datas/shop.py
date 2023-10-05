from aiogram.filters.callback_data import CallbackData


class Product(CallbackData, prefix="food"):
    name: str
    mass: int
    price: int
