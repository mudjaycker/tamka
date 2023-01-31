from vosk import Model, KaldiRecognizer
from tumiaji import require
import pyaudio
from functools import lru_cache
import random as rd
from  . word_bank_fr import simples

from  . text2speech import TamkaSpeaker
from pathlib import Path

eel_path = str(Path(__file__).parent.parent)+"/desktop_ui/init_eel.py"
eel = require(eel_path).eel

MODEL_PATH = str(Path(Path(__file__).parent, "model"))

class TamkaListener:
    def __init__(self,):
        model = Model(MODEL_PATH)

        self.__recognizer = KaldiRecognizer(model, 16000)
        self.result = ""
        self.re_run = False
        self.is_said_well = False
        self.said = ""

    def __start_microphone(self):
        mic = pyaudio.PyAudio()
        self.__stream = mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000, 
            input=True,
            frames_per_buffer=8192
        )
        self.__stream.start_stream()

    @lru_cache
    def __print_text(self, text):
        print(f"\n{text}")
    
    def run_recognition(self, callable):        
        to_say = (rd.choice(simples)).lower()
        callback = callable
        callback("dites " + to_say)
        
        self.__start_microphone()
        print(f"Say: ==> {to_say}")
        
        while True:
                data = self.__stream.read(4096,  exception_on_overflow=False)

                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.Result()[14: -3] #slicing the string result
                    
                    if len(text) > 0:
                        
                        self.__print_text(text)
                        eel.sendMessage(text)

                        if text != "" and text == to_say:
                            self.is_said_well = True
                            self.said = to_say
                            print("Success ... ", text)

                        if text != "" and text != to_say:
                            self.is_said_well = False
                            print("Failed ... ", text)
                    
                if self.re_run is True:
                    to_say = rd.choice(simples)
                    self.run_recognition(callback)
