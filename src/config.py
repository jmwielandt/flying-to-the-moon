import logging
import os
from dataclasses import dataclass

from dynaconf import Dynaconf, Validator


@dataclass
class DbConfig:
    host: str
    port: int
    name: str


@dataclass()
class Misc:
    log_level: int


@dataclass
class AppConfig:
    db: DbConfig
    misc: Misc


def __parse_log_level(x: str | int | float):
    if isinstance(x, float):
        x = int(x)
    if isinstance(x, int):
        if x < logging.NOTSET:
            x = logging.NOTSET
        elif x > logging.CRITICAL:
            x = logging.CRITICAL
    elif isinstance(x, str):
        x = x.strip("'\"")
        x = logging._nameToLevel[x.upper()]
    return x


def __load_db_settings(settings: Dynaconf) -> DbConfig:
    db_config = DbConfig(
        settings.db.host,  # type: ignore
        settings.db.port,  # type: ignore
        settings.db.name,  # type: ignore
    )
    return db_config


def __load_misc_settings(settings: Dynaconf) -> Misc:
    misc = Misc(
        settings.misc.log_level,  # type: ignore
    )
    return misc


def __load_settings():
    root_path = "."
    desired_root_path = "./configs/"
    if os.path.exists(desired_root_path) and os.path.isdir(desired_root_path):
        root_path = desired_root_path
    settings = Dynaconf(
        dotenv_override=True,
        envvar_prefix=False,
        environments=False,
        load_dotenv=True,
        root_path=root_path,
        validators=[
            Validator("db.host", is_type_of=str, default="localhost"),
            Validator("db.port", is_type_of=int, default=28015),
            Validator("db.name", is_type_of=str, default="test"),
            Validator(
                "misc.log_level",
                is_type_of=str | int,
                cast=__parse_log_level,
                default=logging.DEBUG,
            ),
        ],
    )

    global app_config

    app_config = AppConfig(
        __load_db_settings(settings),
        __load_misc_settings(settings),
    )
    return app_config


app_config: AppConfig = __load_settings()  # type: ignore
