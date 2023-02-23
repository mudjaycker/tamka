from vosk import Model, KaldiRecognizer
from tumiaji import require
import pyaudio
from functools import lru_cache
from pathlib import Path

eel_path = str(Path(__file__).parent.parent)+"/desktop_ui/init_eel.py"
eel = require(eel_path).eel


MODEL_PATH = str(Path(Path(__file__).parent, "model"))

class TamkaListener:
    def __init__(self,):
        model = Model(MODEL_PATH)

        self.__recognizer = KaldiRecognizer(model, 16000)
        self.result = ""
        self.is_running = False
        self.is_said_well = False
        self.said = ""
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000, 
            input=True,
            frames_per_buffer=8192
        )

    
    @lru_cache
    def __print_text(self, text):
        print(f"\n{text}")
    
    def run_recognition(self, ui_function):    
        
        self.stream.start_stream()

        while True:
                data = self.stream.read(4096,  exception_on_overflow=False)

                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.Result()[14: -3] #slicing the string result
                    
                    if len(text) > 0:
                        self.__print_text(text)
                        ui_function(text)
                        
                        self.mic.close(stream=self.stream)
                        self.mic.terminate()
                        break 
                        
                            
