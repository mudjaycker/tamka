from desktop_ui.init_eel import *
from engine.speech2text import TamkaListener
from engine.text2speech import TamkaSpeaker

if __name__ == "__main__":
    listener = TamkaListener()
    speaker = TamkaSpeaker()
    run_recognition = listener.run_recognition
    say = speaker.say

    eel.expose(run_recognition)
    eel.expose(say)


    @eel.expose
    def get_said():
        return listener.said

    @eel.expose
    def listener_get_re_run():
        return listener.re_run

    @eel.expose
    def listener_get_is_said_well():
        return listener.is_said_well

    eel.start("index.html")