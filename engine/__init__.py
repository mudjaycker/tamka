# mypy: disable-error-code="no-any-return"
import eel
from pathlib import Path

from copy import deepcopy
import threading
from pony.orm import db_session
from random import shuffle
from datetime import date

from .stt_tts.speech2text import TamkaListener
from .stt_tts.text2speech import TamkaSpeaker
from . models.word_bank_fr import datas, datas_copy
from .models.views import TamkaView, UserView, GameView
from typing import Final
import eel


UI_DIR: Final[Path] = Path(__file__).parent.parent
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
