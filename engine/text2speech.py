import pyttsx3
import platform
from pathlib import Path
from tumiaji import require
from . ubuntu_speaker import french_speaker

eel_path = str(Path(__file__).parent.parent)+"/desktop_ui/init_eel.py"
eel = require(eel_path).eel

class TamkaSpeaker:
    def __init__(self, rate=130):
        self.language = "fr-fr".upper()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)

        if platform.system() == "Windows":
            self.set_language()


    def set_language(self):
        for voice in self.engine.getProperty('voices'):
            if self.language in voice.id:
                self.engine.setProperty('voice', voice.id)
                return True

        raise RuntimeError(f"Language '{self.language}' not supported")

    def say(self, message):
        eel.receiveMsg(message[7:])
        if platform.system() == "Linux":
            french_speaker(message)
        else:
            self.engine.say(message)
            self.engine.runAndWait()
        # self.engine.stop()


