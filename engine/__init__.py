# mypy: disable-error-code="no-any-return"
import eel
from pathlib import Path
from .models.views import TamkaView, UserView, GameView
from .stt_tts.speech2text import TamkaListener
from .stt_tts.text2speech import TamkaSpeaker
from .text_from_db import get_texts, error_msg, texts_by_level, first_words


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
def do_recognition(language: str):
    listener = TamkaListener(language)
    text = listener.run_recognition()
    eel.sayToSystem(text)


@eel.expose
def do_speak_challenge(language: str, level: str):
    global texts_by_level
    try:
        if texts_by_level[language][level][0] == None:
            texts_by_level[language][level] = get_texts(language, level)
        message = texts_by_level[language][level].pop()
        message = first_words[language]+message

        return len(texts_by_level[language][level])

    except IndexError:
        message = error_msg(language, level)
        return -1

    finally:
        speaker = TamkaSpeaker(
            message=message,
            language=language
        )
        eel.systemSayToUser(message)
        speaker.speak()