import importlib
import os

from aiogram import Dispatcher

from misc.root import get_root, get_abspath, get_list_abspath


def register_dp_middlewares(dp: Dispatcher):
    """


    :param dp:
    :return:
    """

    modules: list[str] = list(map(lambda x: x[:-3], os.listdir(get_abspath(__file__))))
    modules.remove('__init__')
    modules.remove('__pycach')

    package = ".".join(get_list_abspath(__file__)[len(get_root().split('/')):])
    for module in modules:
        import_register = importlib.import_module(f".{module}", package=package).register
        import_register(dp)
