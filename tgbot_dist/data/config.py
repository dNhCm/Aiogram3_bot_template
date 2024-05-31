import os
from configparser import ConfigParser
from dataclasses import dataclass
from environs import Env

from misc.root import get_root


@dataclass
class Tgbot:
    token: str
    admins: list[int]
    default_lang_code: str
    web_apps: dict[str, dict[str, str]]
    langs: dict[str, dict[str, str]]
    use_redis: bool


@dataclass
class Redis:
    host: str
    port: int
    password: str


@dataclass
class Payment:
    token: str
    currency: str


@dataclass
class Misc:
    tz: str


@dataclass
class Config:
    tgbot: Tgbot
    redis: Redis
    payment: Payment
    misc: Misc


def get_config() -> Config:
    env = Env()
    path = './tgbot/.env'
    env.read_env(path)

    config = ConfigParser()
    config.read(get_root() + '/tgbot/data/web_apps.ini')

    return Config(
        tgbot=Tgbot(
            token=env.str("TOKEN"),
            admins=list(map(int, env.str("ADMINS").split(' '))),
            default_lang_code=env.str("DEFAULT_LANG_CODE"),
            web_apps={
                section.lower(): {option: config.get(section, option)}
                for section in config.sections()
                for option in config.options(section)
            },
            langs={
                lang: {
                    text[:-4]: open(get_root() + f'/tgbot/data/lang/{lang}/{text}', 'r', encoding="UTF-8").read()
                    for text in os.listdir(get_root() + '/tgbot/data/lang/' + lang)
                }
                for lang in os.listdir(get_root() + '/tgbot/data/lang')
            },
            use_redis=env.bool("USE_REDIS"),
        ),
        redis=Redis(
            host=env.str("REDIS_HOST"),
            port=env.int("REDIS_PORT"),
            password=env.str("REDIS_PASSWORD"),
        ),
        payment=Payment(
            token=env.str("PAYMENT_PROVIDER_TOKEN"),
            currency=env.str("PAYMENT_CURRENCY"),
        ),
        misc=Misc(
            tz=env.str("SCHEDULER_TZ")
        )
    )
