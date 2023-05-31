from vosk import Model, KaldiRecognizer
import pyaudio
from pathlib import Path
import os


song_path: str = str(Path(Path(__file__).parent, "ROBTVox_Notification.wav"))


def play(song_path: str) -> None:
    cmd = "play " + song_path
    os.system(cmd)


class TamkaListener:
    def __init__(self, language: str = "français") -> None:
        MODEL_PATH = str(Path(Path(__file__).parent, "model", language+"_model"))
        self.__model = Model(MODEL_PATH)

    def __run_mic(self,):
        self.__recognizer = KaldiRecognizer(self.__model, 16000)
        self.__mic = pyaudio.PyAudio()
        self.__stream = self.__mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8192
        )

    def run_recognition(self) -> str:
        play(song_path)
        self.__run_mic()
        self.__stream.start_stream()

        while True:
            data = self.__stream.read(4096,  exception_on_overflow=False)

            if self.__recognizer.AcceptWaveform(data):
                # slicing the resulted string
                text: str = self.__recognizer.Result()[14: -3]

                if len(text) > 0:
                    self.__mic.close(stream=self.__stream)
                    self.__mic.terminate()
                    return text
