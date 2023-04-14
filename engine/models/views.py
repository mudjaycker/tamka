from pony.orm.core import Query # for typing

from pony import orm
from  . db_models import Tamka, User, date
import bcrypt
from typing import Callable, Sequence, Union

Users = Union[Query , Sequence[User] ]
Tamkas = Union[Query,  Sequence[Tamka]]


class TamkaView:
    def set(self, text: str, level: str, success: bool, language:str, date_of: date=date.today()):
        """text: str, success: Optional[bool], language: str, 
            level: str, date_of: Optional[datetime]"""
            
        with orm.db_session():
            Tamka(text=text, language=language, level=level, date_of=date_of)

    def get_where(self, condition: Callable[[Tamka], bool]):
        with orm.db_session():
            query: Tamkas = Tamka.select(condition)
        return query


class UserView:
    def set(self, username: str, password: str):
        password_encoded = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_encoded, bcrypt.gensalt())

        with orm.db_session():
            User(username=username, password=hashed)

    def is_user(self, username: str, password: str) -> bool:
        password_encoded = password.encode("utf-8")
        with orm.db_session():
            query: Users = User.select(lambda x: x.username == username)
            print(query)
            user = query[:][0]

            return bcrypt.checkpw(password_encoded, user.password)


# u = UserView()

# u.set("tom", "test123")
# print(u.is_user("tom", "test1234"))
