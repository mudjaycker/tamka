from vosk import Model, KaldiRecognizer
import pyaudio
from functools import lru_cache
from pathlib import Path
from queue import Queue
from text2speech import TamkaSpeaker
import random as rd
from word_bank_fr import simples

q = Queue()

class TamkaListener:
    def __init__(self,):
        model = Model(str(Path("models").absolute().resolve()))
        self.__recognizer = KaldiRecognizer(model, 16000)
        self.result = ""

    def __start_microphone(self):
        mic = pyaudio.PyAudio()
        self.__stream = mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000, input=True,
            frames_per_buffer=8192
        )
        self.__stream.start_stream()

    @lru_cache
    def __print_text(self, text):
        print(f"\n{text}")
    
    def run_recognition(self, callable):
        self.__start_microphone()
        to_say = rd.choice(simples)
        print("Say: ==> ", to_say)
        test = 1
        callback = callable
        callback(to_say)
        
        while True:
                test = 0 
                data = self.__stream.read(4096,  exception_on_overflow=False)

                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.Result()[14: -3] #slicing the string result
                    self.__print_text(text)
                    if text != "" and text == to_say:
                        print("Success ... ", text)
                        test = int(input("Apprendre ==> "))
                    if text != "" and text != to_say:
                        print("Failed ... ", text)
                        test = int(input("Apprendre ==> "))
                    
                if test == 1:
                    to_say = rd.choice(simples)
                    self.run_recognition(callback)
               


