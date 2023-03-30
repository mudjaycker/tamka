from pony import orm
from . db_models import Tamka, User
import bcrypt

class TamkaView:
    def set(self, **kwargs):
        """text: str, success: Optional[bool], language: str, 
            level: str, date_of: Optional[datetime]"""
        
        with orm.db_session():
            Tamka(**kwargs)

    def get_where(self, condition) -> Tamka:
        with orm.db_session():
            querry = Tamka.select(condition)
        return querry


class UserView:
    def set(self, username, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        
        with orm.db_session():
            User(username=username, password=hashed)
    
    def is_user(self, username, password):
        password = password.encode("utf-8")
        with orm.db_session():
            querry = User.select(lambda x: x.username == username)
            user = querry[:][0]
            
            return bcrypt.checkpw(password, user.password)
            


# u = UserView()

# u.set("tom", "test123")
# print(u.is_user("tom", "test1234"))