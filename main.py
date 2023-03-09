from desktop_ui.init_eel import *
import webview
import threading
from engine.speech2text import TamkaListener
from engine.text2speech import TamkaSpeaker
from engine.word_bank_fr import french_datas, english_datas
from engine.views import TamkaView
from pony.orm import db_session
from datetime import date
from typing import Any


tamka_view = TamkaView()


@eel.expose
def get_datas_length(level):
    if eel.getLanguage()() == "français":
        return len(french_datas[level])
    else:
        return len(english_datas[level])


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



def do_say(level, text):
    receive_msg = threading.Thread(
        target=eel.systemSayToUser, args=(level, text))

    speaker = TamkaSpeaker(eel.getLanguage()())
    speak = threading.Thread(target=speaker.say, args=(text,))
    receive_msg.start()
    speak.start()
    receive_msg.join()
    speak.join()


def start_speaker(level):
    try:
        text = (french_datas[level].pop()
                if eel.getLanguage()() == 'français'
                else english_datas[level].pop()
                )

        to_say = "dites: "+text if eel.getLanguage()() == 'français' else "say: "+text
        do_say(level, to_say)

        listener = TamkaListener(eel.getLanguage()())
        sayed = listener.run_recognition(eel.sayToSystem)
        query_params = {
            "text": text,
            "success": False,
            "level": level,
            "language": eel.getLanguage()()
        }

        if text.lower() == sayed:  # on sayed well
            query_params["success"] = True
            tamka_view.set(**query_params)
            eel.setSuccessPoints()
        else:  # on sayed bad
            tamka_view.set(**query_params)
            eel.setFailedPoints()

    except IndexError:

        french_level_map = {
            "easy": "facile",
            "medium": "moyen",
            "hard": "difficile",
        }

        to_say = ("vous avez finis le niveau " +
                  french_level_map[level]
                  if eel.getLanguage()() == "français"
                  else f"you finish the {level} level"
                  )

        do_say_thread = threading.Thread(target=do_say, args=(level, to_say))
        do_say_thread.start()


expose_start_speaker = threading.Thread(target=eel.expose(start_speaker))
expose_start_speaker.start()


# def start_eel():
    # eel.start("index.html", mode=None)


# eel_thread = threading.Thread(target=start_eel)
# eel_thread.start()

eel.start("index.html", mode="chrome")

# webview.create_window('Tamka', 'http://localhost:8000/index.html')
# webview.start(debug=True)
