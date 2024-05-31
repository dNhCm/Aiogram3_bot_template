import importlib
import os
from copy import deepcopy

from misc.root import get_root, get_abspath, get_list_abspath


async def connect_models():
    python_models = os.listdir(get_abspath(__file__))

    for el in deepcopy(python_models):
        if not el[-3:] == ".py":
            python_models.remove(el)
    python_models.remove("__init__.py")
    python_models = list(map(lambda x: x[:-3], python_models))

    package = ".".join(get_list_abspath(__file__)[len(get_root().split('/')):])
    for module in python_models:
        import_connect = importlib.import_module(f".{module}", package=package).main
        await import_connect()
