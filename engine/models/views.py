# mypy: disable-error-code="name-defined"
# mypy: disable-error-code="union-attr"
from pony import orm
from typing import Callable, Sequence, Union, TypedDict
from datetime import date
import bcrypt
from pony.orm.core import Query  # for typing
from db_models import Tamka, User

Users = Union[Query, Sequence[User]]
Tamkas = Union[Query, Sequence[Tamka]]
UserTransact = TypedDict("UserTransact", {
    "message_or_entity": Users | str,
    "status": bool
})


class TamkaView:
    def set(self, user: str, text: str, level: str,
            language: str, date_of: date = date.today()) -> None:
        with orm.db_session():
            Tamka(user=user, text=text, language=language,
                  level=level, date_of=date_of)

    def get_where(self, condition: Callable[[Tamka], bool]) -> Tamkas:
        with orm.db_session():
            query: Tamkas = Tamka.select(condition)
        return query


class UserView:
    def create(self, username: str, password: str) -> UserTransact:

        try:
            password_encoded = password.encode('utf-8')
            hashed = bcrypt.hashpw(password_encoded, bcrypt.gensalt())
            with orm.db_session():
                User(username=username, password=hashed)
                return {"message_or_entity": "created", "status": True}
        except Exception as e:

            return {"message_or_entity": str(e), "status": False}

    def is_user(self, username: str, password: str) -> bool:
        password_encoded = password.encode("utf-8")
        try:
            with orm.db_session():
                query: Users = User.select(lambda x: x.username == username)
                user = query[:][0]

                return bcrypt.checkpw(password_encoded, user.password)
        except IndexError:
            return False

    def get_user(self, username: str, password: str) -> UserTransact:
        password_encoded = password.encode("utf-8")
        try:
            with orm.db_session():
                query: Users = User.select(lambda x: x.username == username)
                user = query[:][0]
                if bcrypt.checkpw(password_encoded, user.password):
                    return {"message_or_entity": user, "status": True}
                return {
                    "message_or_entity": "Incorrect password",
                    "status": False
                }
        except IndexError:
            return {"message_or_entity": str(IndexError), "status": True}

    def delete(self, username: str, password: str) -> bool:
        if self.is_user(username, password):
            with orm.db_session():
                user = self.get_user(username, password)
                user["message_or_entity"].delete()
                return True
        return False


u = UserView()
# print(u.delete("tom", "test123"))
print("is user", u.is_user("tom", "test123"))
print(u.create("tom", "test123"))
# print(u.delete("tom", "test123"))
print("is user", u.is_user("tom", "test123"))
# print(u.is_user("tom", "test123"))
