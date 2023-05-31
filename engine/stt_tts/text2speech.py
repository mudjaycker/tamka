import pyttsx3
import platform
from . ubuntu_speaker import speaker


class TamkaSpeaker:
    def __init__(self, message: str, language: str = "français") -> None:
        self.rate = 130,
        self.message = message
        self.language = language
        self.engine = pyttsx3.init()
        self.engine.setProperty('self.rate', self.rate)

    def __set_language_windows(self, language: str) -> bool | None:
        for voice in self.engine.getProperty('voices'):
            if language in voice.id:
                self.engine.setProperty('voice', voice.id)
                return True

        raise RuntimeError(f"Language '{self.language}' not supported")

    def __winows_say(self):
        lang_map = {
            "français": "FR-FR",
            "english": "EN-US",
        }
        self.__set_language_windows(lang_map[self.language])
        self.engine.say(self.message)
        self.engine.runAndWait()

    def __linux_say(self) -> None:
        speaker(self.message, self.language)

    def speak(self):
        speaker_map = {
            "Linux":  self.__linux_say,
            "Windows": self.__winows_say
        }
        operating_system = platform.system()
        speaker_map[operating_system]()
