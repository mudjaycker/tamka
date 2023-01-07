import pyttsx3
import platform

class TamkaSpeaker:
    def __init__(self, rate=130):
        self.language = "fr-fr".upper()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)

        if platform.system() == "Windows":
            self.set_language()
        else:
            self.engine.setProperty('voice', "french") # for ubuntu

    def set_language(self):
        for voice in self.engine.getProperty('voices'):
            if self.language in voice.id:
                self.engine.setProperty('voice', voice.id)
                return True

        raise RuntimeError(f"Language '{self.language}' not supported")

    def say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
        # self.engine.stop()


