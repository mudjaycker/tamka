# mypy: disable-error-code="no-any-return"
import eel
from pathlib import Path
from .models.views import TamkaView, UserView, GameView
from .stt_tts.speech2text import TamkaListener


UI_DIR = Path(__file__).parent.parent
eel.init(str(Path(UI_DIR, "desktop_ui")))

@eel.expose
def do_authentication(username: str, password: str, action: str):
    user = UserView(username=username, password=password)

    actions_map = {
        "login": user.is_user,
        "signup": user.create,
        "delete": user.delete,
    }
    
    return actions_map[action]()

@eel.expose
def do_recognition(language):
    listener = TamkaListener(language)
    text = listener.run_recognition()
    eel.sayToSystem(text)