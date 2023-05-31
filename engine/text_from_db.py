from random import shuffle
from .models.views import orm, TamkaView

tamka = TamkaView()

texts_by_level = {
    "français": {
        "easy": [None],
        "medium": [None],
        "hard": [None]
    },
    "english": {
        "easy": [None],
        "medium": [None],
        "hard": [None]
    }
}
first_words = {
    "english": "say: ",
    "français": "dites: "
}



def error_msg(language: str, level: str):
    french_levels_map = {
        "easy": "facile",
        "medium": "moyen",
        "hard": "difficile"
    }
    error_msg_by_language = {
        "français": lambda: f"Vous avez terminé le niveau {french_levels_map[level]}",
        "english": lambda: f"You finished the {level} level"
    }
    return error_msg_by_language[language]()


def get_texts(language: str, level: str):
    global texts
    with orm.db_session():
        tamkas = tamka.get_where(lambda t: t.language == language and t.level == level)
        texts = [t.text for t in tamkas]
        shuffle(texts)
        return texts
