import pyttsx3
import platform
from pathlib import Path
from tumiaji import require
from . ubuntu_speaker import speaker

eel_path = str(Path(__file__).parent.parent)+"/desktop_ui/init_eel.py"
eel = require(eel_path).eel


class TamkaSpeaker:
    def __init__(self, language="français"):
        self.rate=130,
        self.language = language
        self.win_lang = language
        self.engine = pyttsx3.init()
        self.engine.setProperty('self.rate', self.rate)

        if platform.system() == "Windows":
            self.set_language()

    def set_language(self):
        for voice in self.engine.getProperty('voices'):
            if self.language in voice.id:
                self.engine.setProperty('voice', voice.id)
                return True

        raise RuntimeError(f"Language '{self.language}' not supported")

    def say(self, message):
        if platform.system() == "Linux":
            speaker(message, self.language)
        else:
            if self.language == "français":
                self.win_lang = "fr-fr".upper()
            else:
                self.win_lang = "eng-us".upper()

            self.engine.say(message)
            self.engine.runAndWait()
        # self.engine.stop()
