# mypy: disable-error-code="name-defined"
from pony import orm
from datetime import date


db = orm.Database()


class User(db.Entity):
    username: str = orm.Required(str, unique=True)
    password: bytes = orm.Required(bytes)
    game = orm.Set("Game")
    tamka = orm.Set("Tamka")
    statistic = orm.Set("Statistic")


class Tamka(db.Entity):
    user: User = orm.Required("User")
    text:  str = orm.Required(str)
    language: str = orm.Required(str)
    level: str = orm.Required(str)
    date_of: date = orm.Required(date, default=date.today())
    game = orm.Optional("Game")


class Game(db.Entity):
    user: User = orm.Required("User")
    tamka: Tamka = orm.Required("Tamka")
    succes: str = orm.Required(bool)
    date_of: date = orm.Required(date, default=date.today())


class Statistic(db.Entity):
    user: User = orm.Required("User")
    language: str = orm.Required(str)
    by_sentence: str = orm.Required(float)
    by_senteces: str = orm.Required(float)
    by_level: str = orm.Required(float)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
