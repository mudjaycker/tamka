# mypy: disable-error-code="no-any-return"
import eel
from pathlib import Path
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
