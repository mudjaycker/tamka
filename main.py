from desktop_ui.init_eel import *
from jinja2 import Environment, FileSystemLoader
from copy import deepcopy
import threading
from engine.stt_tts.text2speech import TamkaSpeaker
from engine.stt_tts.speech2text import TamkaListener
from engine.models.word_bank_fr import datas, datas_copy
from engine.models.views import TamkaView
from pony.orm import db_session
from datetime import date
from pathlib import Path
from random import shuffle

tamka_view = TamkaView()
CHALLENGE_POS = {
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
def restart(language, level):
    global datas_copy, CHALLENGE_POS
    CHALLENGE_POS[language][level] = 0
    datas_copy = deepcopy(datas)
    print("===>", CHALLENGE_POS[language][level])
    print("===>", datas_copy)


def say_finished(language, level):
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
def get_datas_length(language, level):
    return len(datas_copy[language][level])


@eel.expose
def get_tamka_qty(language):
    with db_session():
        tamka_qty = tamka_view.get_where(
            lambda t: t.language == language).count()
        return tamka_qty


@eel.expose
def get_from_tamka(language, level: str, success: bool = True, of_today: bool = True):
    with db_session():
        query = (tamka_view.get_where(lambda t: t.language == language
                                      and t.success == success
                                      and t.level == level
                                      and t.date_of == date.today()
                                      )
                 ) if of_today else (tamka_view.get_where(lambda t: t.language == language
                                                          and t.success == success
                                                          and t.level == level
                                                          ))
        return query.count()


def do_say(language, level, text):
    receiveid_msg = threading.Thread(
        target=eel.systemSayToUser, args=(level, text))

    speaker = TamkaSpeaker(language)
    speak = threading.Thread(target=speaker.say, args=(text,))
    receiveid_msg.start()
    speak.start()
    receiveid_msg.join()
    speak.join()


def start_speaker(language, level):
    global datas_copy, CHALLENGE_POS
    challenges = datas[language][level]
    len_challenges = len(challenges)
    CHALLENGE_POS[language][level] += 1

    if CHALLENGE_POS[language][level] > len_challenges:
        say_finished(language, level)

    else:
        shuffle(datas_copy[language][level])
        text = datas_copy[language][level].pop()
        to_say = "dites: "+text if language == 'français' else "say: "+text
        do_say(language, level, to_say)
        listener = TamkaListener(language)
        sayed = listener.run_recognition(eel.sayToSystem)
        query_params = {
            "text": text,
            "success": False,
            "level": level,
            "language": language
        }

        if text.lower() == sayed:  # on sayed well
            query_params["success"] = True
            tamka_view.set(**query_params)
            eel.setSuccessPoints()
        else:  # on sayed bad
            tamka_view.set(**query_params)
            eel.setFailedPoints()


expose_start_speaker = threading.Thread(target=eel.expose(start_speaker))
expose_start_speaker.start()


root = Path(__file__).parent
templates_dir = Path(root, 'desktop_ui')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('base.jinja')

# Save the compiled html to a file
filename = Path(root, 'desktop_ui', 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render())


eel.start("index.html", mode="chrome", jinja_templates='/')
