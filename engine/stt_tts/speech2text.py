from vosk import Model, KaldiRecognizer
import pyaudio
from pathlib import Path
import os
from typing import Callable


song_path: str = str(Path(Path(__file__).parent, "ROBTVox_Notification.wav"))


def play(song_path: str) -> None:
    cmd = "play " + song_path
    os.system(cmd)


class TamkaListener:
    def __init__(self, language: str = "français") -> None:
        MODEL_PATH = str(Path(Path(__file__).parent, "model", language+"_model"))
        model = Model(MODEL_PATH)

        self.__recognizer = KaldiRecognizer(model, 16000)
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8192
        )

    def run_recognition(self) -> str:

        self.stream.start_stream()
        play(song_path)

        while True:
            data = self.stream.read(4096,  exception_on_overflow=False)

            if self.__recognizer.AcceptWaveform(data):
                # slicing the resulted string
                text: str = self.__recognizer.Result()[14: -3]

                if len(text) > 0:
                    self.mic.close(stream=self.stream)
                    self.mic.terminate()
                    return text
