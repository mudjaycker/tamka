# mypy: disable-error-code="no-any-return"
import eel
from pathlib import Path

from copy import deepcopy
import threading
from pony.orm import db_session
from random import shuffle
from datetime import date

from .stt_tts.speech2text import TamkaListener
from .stt_tts.text2speech import TamkaSpeaker
from . models.word_bank_fr import datas, datas_copy
from .models.views import TamkaView, UserView, GameView
from typing import Final


UI_DIR: Final[Path] = Path(__file__).parent.parent
eel.init(str(Path(UI_DIR, "desktop_ui")))

user_view = UserView()
game_view = GameView()
tamka_view = TamkaView()


challenge_pos = {
    "français": {
        "easy": 0,
        "medium": 0,
        "hard": 0,
    },
    "english": {
        "easy": 0,
        "medium": 0,
        "hard": 0,
    },

}


@eel.expose
def restart(language: str, level: str) -> None:
    global datas_copy, challenge_pos
    challenge_pos[language][level] = 0
    datas_copy = deepcopy(datas)
    # print("===>", challenge_pos[language][level])
    # print("===>", datas_copy)


def say_finished(language: str, level: str) -> None:
    french_level_map = {
        "easy": "facile",
        "medium": "moyen",
        "hard": "difficile",
    }

    to_say = ("vous avez finis le niveau " +
              french_level_map[level]
              if language == "français"
              else f"You have finished the {level} level"
              )
