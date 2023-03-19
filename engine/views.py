from pony import orm
from . db_models import Tamka


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