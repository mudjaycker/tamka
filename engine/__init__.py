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

    do_say_thread = threading.Thread(
        target=do_say, args=(language, level, to_say))
    do_say_thread.start()


@eel.expose
def get_datas_length(language: str, level: str) -> int:
    return len(datas_copy[language][level])


@eel.expose
def get_tamka_qty(language: str) -> int:
    with db_session():
        tamka_qty = tamka_view.get_where(
            lambda t: t.language == language).count()  # type: ignore
        return tamka_qty                       # conflict between count methods


@eel.expose
def get_from_tamka(language: str, level: str, success: bool = True,
                   of_today: bool = True) -> int:
    with db_session():
        query = (tamka_view.
                 get_where(
                     lambda t: t.language == language  # type: ignore
                     and t.success == success
                     and t.level == level
                     and t.date_of == date.today()
                 )
                 ) if of_today else (tamka_view.
                                     get_where(
                                         lambda t: t.language == language
                                         and t.success == success
                                         and t.level == level
                                     ))
        return query.count()  # type: ignore
        # conflict between count methods


def do_say(language: str, level: str, text: str) -> None:
    receiveid_msg = threading.Thread(
        target=eel.systemSayToUser, args=(level, text))  # type: ignore

    speaker = TamkaSpeaker(language)
    speak = threading.Thread(target=speaker.say, args=(text,))
    receiveid_msg.start()
    speak.start()
    receiveid_msg.join()
    speak.join()


def start_speaker(language: str, level: str) -> None:
    global datas_copy, challenge_pos
    challenges = datas[language][level]
    len_challenges = len(challenges)
    challenge_pos[language][level] += 1

    if challenge_pos[language][level] > len_challenges:
        say_finished(language, level)

    else:
        shuffle(datas_copy[language][level])
        text = datas_copy[language][level].pop()
        to_say = "dites: "+text if language == 'français' else "say: "+text
        do_say(language, level, to_say)
        listener = TamkaListener(language)
        sayed = listener.run_recognition(eel.sayToSystem)  # type: ignore
        q_paramas = {
            "user_pk": 1,
            "tamka_pk": 1,
            "success": True
        }
        if text.lower() == sayed:  # on sayed well
            game_view.create(**q_paramas)  # type: ignore
            eel.setSuccessPoints()  # type: ignore
        else:  # on sayed bad
            q_paramas["success"] = False
            game_view.create(**q_paramas)  # type: ignore
            eel.setFailedPoints()  # type: ignore


expose_start_speaker = threading.Thread(target=eel.expose(start_speaker))
expose_start_speaker.start()
