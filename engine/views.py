from pony import orm
from . db_models import Tamka
from typing import List


class TamkaView:
    def set(self, **kwargs):
        """text: str, success: Optional[bool], language: str, 
            level: str, date_of: Optional[datetime]"""
        
        with orm.db_session():
            Tamka(**kwargs)

    def get_by_level(self, level: str) -> List[Tamka]:
        with orm.db_session():
            t = Tamka.select(lambda t: t.level == level)[:]
        return t
    
    # def update(self, text:str, success:bool, date_of:datetime):
        # with orm.db_session():
            # tamka = Tamka.select(lambda t: t.text == text).first()
            # tamka.set(success=success, date_of=date_of)


#Full database
# view = TamkaView()

# orm.set_sql_debug(True)
# view.update(text="Unité Travail Progrès", success=True, date_of=datetime.now())
# for texts in datas.items():
    # for text in texts[1]:
        # view.set(text=text, language="French", level=texts[0])