# mypy: disable-error-code="name-defined"
from pony import orm
from datetime import date
from typing import Sequence


db = orm.Database()


class User(db.Entity):
    username: str = orm.Required(str, unique=True)
    password: bytes = orm.Required(bytes)
    game: Sequence[int] = orm.Set("Game")
    tamka: Sequence[int] = orm.Set("Tamka")
    statistic: Sequence[int] = orm.Set("Statistic")
    stats_by_sentence: int = orm.Set("StatsBySentence")


class Tamka(db.Entity):
    user: int = orm.Required("User")
    text:  str = orm.Required(str)
    language: str = orm.Required(str)
    level: str = orm.Required(str)
    date_of: date = orm.Required(date, default=date.today())
    game: int = orm.Optional("Game")


class Game(db.Entity):
    user: int = orm.Required("User")
    tamka: int = orm.Required("Tamka")
    succes: str = orm.Required(bool)
    date_of: date = orm.Required(date, default=date.today())


class Statistic(db.Entity):
    user: int = orm.Required("User")
    language: str = orm.Required(str)
    by_sentence: int = orm.Required("StatsBySentence")
    by_senteces: Sequence[int] = orm.Set("StatsBySentence")
    by_level: str = orm.Required(float)


class StatsBySentence(db.Entity):
    user: int = orm.Required("User")
    sentence: str = db.Column(db.String)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
