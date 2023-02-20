from desktop_ui.init_eel import *
import webview
import threading
from engine.speech2text import TamkaListener
from engine.text2speech import TamkaSpeaker
from engine.word_bank_fr import datas
from unsync import unsync


def do_say(to_say):
    receive_msg = threading.Thread(target=eel.receiveMsg, args=(to_say,))
    speak = threading.Thread(target=TamkaSpeaker().say, args=(to_say,))
    receive_msg.start()
    speak.start()
    receive_msg.join()
    speak.join()
                 
    
@unsync    
def start_speaker(level):
    try:
        text = datas[level].pop()
        to_say = "dites: "+text
        # do_say_thread = threading.Thread(target=do_say, args=(to_say,))
        # recognize = threading.Thread(target=TamkaListener().run_recognition)
        do_say(to_say)
        TamkaListener().run_recognition()

        
    except IndexError:
        to_say = "vous avez finis le niveau "+level
        do_say_thread = threading.Thread(target=do_say, args=(to_say,))
        do_say_thread.start()


eel.expose(start_speaker)
def start_eel():
    eel.start("index.html", mode=None)


eel_thread = threading.Thread(target=start_eel)

eel_thread.start()
# eel.start("index.html", mode="chrome")

webview.create_window('Tamka', 'http://localhost:8000/index.html')
webview.start()
