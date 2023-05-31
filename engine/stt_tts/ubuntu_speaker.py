import os

# install pico => #sudo apt-get install libttspico-utils


def speaker(text: str, language: str) -> None:
    """Linux speaker"""
    target_file = "tempo.wav"
    speaker_lang_map = {
        "français": f"""pico2wave -l fr-FR -w {target_file} "{text}" &&                              ─╯
                        play -qV0 {target_file} treble 20 gain -l 6 tempo 0.7
                     """,

        "english": f"""pico2wave -l en-US -w {target_file} "{text}" &&
                       play -qV0 {target_file} treble 5 gain -l 5 tempo 0.85
                    """,
    }
    os.system(speaker_lang_map[language])
