# mypy: disable-error-code="name-defined"
# mypy: disable-error-code="union-attr"
from pony import orm
from typing import Callable, Iterable, Union, TypedDict, Optional
from datetime import date
import bcrypt
from pony.orm.core import Query  # for typing
from . db_models import Tamka, User, GameSession
from pydantic import BaseModel, validator, StrictStr

Users = Union[Query, Iterable[User]]
Tamkas = Union[Query, Iterable[Tamka]]
GameSessions = Union[Query, Iterable[GameSession]]
GameSessionState = TypedDict("GameSessionState", {
    "message_or_entity": GameSessions | str,
    "status": bool
})

# Not to be used explicitly

class TamkaView:
    def set(self,
            text: StrictStr,
            level: StrictStr,
            language: StrictStr,
            date_of: date = date.today()) -> None:
        with orm.db_session():
            Tamka(text=text, language=language,
                  level=level, date_of=date_of)

    # has to be deleted
    def get_where(self, condition: Callable[[Tamka], bool]) -> Tamkas:
        with orm.db_session():
            query: Tamkas = Tamka.select(condition)
        return query


class UserView(BaseModel):
    username: StrictStr
    password: StrictStr
    encrypted_password: Optional[str] = None

    @validator("password")
    def encode_password(cls, password):
        return password.encode('utf-8')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encrypted_password: Optional[bytes] = bcrypt.hashpw(self.password, bcrypt.gensalt())

    def create(self) -> bool:
        try:
            with orm.db_session():
                User(username=self.username, password=self.encrypted_password)
                return True
        except:
            return False

    def is_user(self) -> bool:
        try:
            with orm.db_session():
                query: Users = User.select(lambda x: x.username == self.username)
                user = query[:][0]

                return bcrypt.checkpw(self.password, user.password)
        except:
            return False

    def get_user(self) -> User | str:
            if self.is_user():
                query: Users = User.select(lambda x: x.username == self.username)
                user = query[:][0]
                return user
            return "User does not exist"

    def delete(self) -> bool:
        if self.is_user():
            with orm.db_session():
                user = self.get_user()

                user["message_or_entity"].delete()
                return True
        return False


class GameView:
    def create(self, user_pk: int, text: str, success: bool,
               date_of: date = date.today()) -> GameSessionState:
        try:
            with orm.db_session():
                tamka = TamkaView().get_where(lambda x: x.text == text)
                tamka_pk = tamka[:][0].id
                GameSession(user=user_pk, tamka=tamka_pk, success=success,
                            date_of=date_of)

            return {"message_or_entity": "created", "status": True}
        except Exception as e:
            return {"message_or_entity": str(e), "status": False}

    def get_all(self, user_pk: int) -> GameSessionState:
        try:
            with orm.db_session():
                res: GameSessions
                res = GameSession.select(lambda g: g.user == user_pk)
                return {"message_or_entity": res, "status": True}
        except Exception as e:
            return {"message_or_entity": str(e), "status": False}


# g = GameView()
# print(g.create(user_pk=1, tamka_pk=1, success=True))


# user_args = {"username": "tom2", "password": "test1234"}
# u = UserView(**user_args)
# print(u.create())
# print(u.delete(**user_args))
# print("is user", u.is_user(**user_args))
# print(u.create(**user_args))
