from desktop_ui.init_eel import *
# from engine.speech2text import TamkaListener
# from engine.text2speech import TamkaSpeaker

if __name__ == "__main__":
    @eel.expose
    def test(name):
        return "Hi "+name
    eel.start("index.html")