# mypy: disable-error-code="name-defined"
from pony import orm
from datetime import date
from typing import Sequence


db = orm.Database()


class User(db.Entity):
    username: str = orm.Required(str, unique=True)
    password: bytes = orm.Required(bytes)
    game: Sequence[int] = orm.Set("GameSession")
    tamka: Sequence[int] = orm.Set("Tamka")
    statistic: Sequence[int] = orm.Set("Statistics")
    stats_by_sentence: int = orm.Set("StatsBySentence")
    by_level: Sequence[int] = orm.Set("StatsByLevel")


class Tamka(db.Entity):
    user: int = orm.Required("User")
    text:  str = orm.Required(str)
    language: str = orm.Required(str)
    level: str = orm.Required(str)
    date_of: date = orm.Required(date, default=date.today())
    game: int = orm.Optional("GameSession")


class GameSession(db.Entity):
    user: int = orm.Required("User")
    tamka: int = orm.Required("Tamka")
    success: str = orm.Required(bool)
    date_of: date = orm.Required(date, default=date.today())


class Statistics(db.Entity):
    user: int = orm.Required("User")
    language: str = orm.Required(str)
    success_number: int = orm.Required(int)
    by_sentence: int = orm.Optional("StatsBySentence")
    by_level: int = orm.Optional("StatsByLevel")


class StatsBySentence(db.Entity):
    user: int = orm.Required("User")
    sentence: str = orm.Required(str)
    statistics: int = orm.Required("Statistics")


class StatsByLevel(db.Entity):
    user: int = orm.Required("User")
    level: str = orm.Required(str)
    statistics: int = orm.Required("Statistics")


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
