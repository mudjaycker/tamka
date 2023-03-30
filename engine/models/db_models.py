from pony import orm
from datetime import date

db = orm.Database()


class Tamka(db.Entity):
    text = orm.Required(str)
    success = orm.Optional(bool)
    date_of = orm.Required(date, default=date.today())
    language = orm.Required(str)
    level = orm.Required(str)
    

class User(db.Entity):
    username = orm.Required(str)
    password = orm.Required(bytes)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)