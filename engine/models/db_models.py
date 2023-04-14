# mypy: disable-error-code="name-defined"
from pony import orm 
from datetime import date


db = orm.Database()


class Tamka(db.Entity):
    text: str = orm.Required(str)
    success: bool | None = orm.Optional(bool)
    date_of: date = orm.Required(date, default=date.today())
    language: str = orm.Required(str)
    level: str = orm.Required(str)

class User(db.Entity):
    username: str = orm.Required(str)
    password: bytes = orm.Required(bytes)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)