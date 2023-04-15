import os

# install pico => #sudo apt-get install libttspico-utils


def speaker(text: str, language: str) -> None:
    """French speaker"""
    if language == "français":
        cmd_speaker = f"""pico2wave -l fr-FR -w tempo.wav "{text}" &&
        play -qV0 tempo.wav treble 20 gain -l 6 tempo 0.7 """
    else:
        cmd_speaker = f"""pico2wave -l en-US -w tempo.wav "{text}"&&
        play -qV0 tempo.wav treble 5 gain -l 5 tempo 0.85 """
        os.system(cmd_speaker)
