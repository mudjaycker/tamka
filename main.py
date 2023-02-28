from desktop_ui.init_eel import *
import webview
import threading
from engine.speech2text import TamkaListener
from engine.text2speech import TamkaSpeaker
from engine.word_bank_fr import datas
from engine.views import TamkaView
from unsync import unsync
from pony.orm import db_session
from datetime import date
from typing import Any


tamka_view = TamkaView()


def get_from_tamka(type: str, when_is: Any, of_today: bool = True):
    map_query = {
        "level": lambda: tamka_view.get_where(lambda t: t.level == when_is
                                              and t.date_of == date.today()),
        "success": lambda: tamka_view.get_where(lambda t: t.success == when_is
                                                and t.date_of == date.today()),
    } if of_today else {
        "level": lambda: tamka_view.get_where(lambda t: t.level == when_is),
        "success": lambda: tamka_view.get_where(lambda t: t.success == when_is),
    }

    with db_session():
        query = map_query.get(type)()
        return query.count() if of_today else [{"text": q.text,
                                                "level": q.level,
                                                "success": q.success,
                                                "date_of": q.date_of
                                                } for q in query[:]]

# print(get_from_tamka("success", when_is=True, of_today=False))


def do_say(level, text):
    receive_msg = threading.Thread(
        target=eel.systemSayToUser, args=(level, text))
    speak = threading.Thread(target=TamkaSpeaker().say, args=(text,))
    receive_msg.start()
    speak.start()
    receive_msg.join()
    speak.join()


@unsync
def start_speaker(level):
    try:
        text = datas[level].pop()
        to_say = "dites: "+text
        do_say(level, to_say)
        sayed = TamkaListener().run_recognition(eel.sayToSystem)
        query_params = {
            "text": text,
            "success": False,
            "level": level
        }

        if text.lower() == sayed:
            query_params["success"] = True
            tamka_view.set(**query_params)
        else:
            tamka_view.set(**query_params)

    except IndexError:
        to_say = "vous avez finis le niveau "+"facile"
        do_say_thread = threading.Thread(target=do_say, args=(level, to_say))
        do_say_thread.start()


eel.expose(start_speaker)


def start_eel():
    eel.start("index.html", mode=None)


# eel_thread = threading.Thread(target=start_eel)
# eel_thread.start()

eel.start("index.html", mode="chrome")

# webview.create_window('Tamka', 'http://localhost:8000/index.html')
# webview.start(debug=True)
