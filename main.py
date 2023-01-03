from speech2text import TamkaListener
from text2speech import TamkaSpeaker



TamkaListener().run_recognition(callable=TamkaSpeaker().say)