import pyttsx3
import platform
from . ubuntu_speaker import speaker


class TamkaSpeaker:
    def __init__(self, language: str = "français") -> None:
        self.rate = 130,
        self.language = language
        self.win_lang = language
        self.engine = pyttsx3.init()
        self.engine.setProperty('self.rate', self.rate)

        if platform.system() == "Windows":
            self.set_language()

    def set_language(self) -> bool | None:
        for voice in self.engine.getProperty('voices'):
            if self.language in voice.id:
                self.engine.setProperty('voice', voice.id)
                return True

        raise RuntimeError(f"Language '{self.language}' not supported")

    def say(self, message: str) -> None:
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
