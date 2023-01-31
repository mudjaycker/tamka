from desktop_ui.init_eel import *
# import webview
import threading
from engine.speech2text import TamkaListener
from engine.text2speech import TamkaSpeaker



def start_speaker():
    TamkaListener().run_recognition(TamkaSpeaker().say)

def start_eel():
    eel.start("index.html", mode="chrome")
    
# eel_thread = threading.Thread(target=start_eel)
speaker_thread = threading.Thread(target=start_speaker)

speaker_thread.start()
# eel_thread.start()
eel.start("index.html", mode="chrome")

# webview.create_window('Tamka', 'http://localhost:8000/index.html')
# webview.start()