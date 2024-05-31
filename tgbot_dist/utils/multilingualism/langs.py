from tgbot.data.config import get_config


def get_text(lang_code: str, text_name: str) -> str:
    config = get_config()
    if not lang_code in config.tgbot.langs.keys():
        lang_code = config.tgbot.default_lang_code
    if not text_name in config.tgbot.langs[lang_code].keys():
        lang_code = config.tgbot.default_lang_code
    return config.tgbot.langs[lang_code][text_name]
