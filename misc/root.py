import os.path


def get_root() -> str:
    return "/".join(
        os.path.abspath(__file__).split('\\')[:-2]
        if len(os.path.abspath(__file__).split('/')) == 1
        else os.path.abspath(__file__).split('/')[:-2]
    )


def get_list_root() -> list[str]:
    return (
        os.path.abspath(__file__).split('\\')[:-2]
        if len(os.path.abspath(__file__).split('/')) == 1
        else os.path.abspath(__file__).split('/')[:-2]
    )


def get_abspath(file: __file__) -> str:
    return "/".join(
        os.path.abspath(file).split('\\')[:-1]
        if len(os.path.abspath(file).split('/')) == 1
        else os.path.abspath(file).split('/')[:-1]
    )


def get_list_abspath(file: __file__) -> list[str]:
    return (
        os.path.abspath(file).split('\\')[:-1]
        if len(os.path.abspath(file).split('/')) == 1
        else os.path.abspath(file).split('/')[:-1]
    )
