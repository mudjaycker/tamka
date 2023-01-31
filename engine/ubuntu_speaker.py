import shlex, subprocess
import os

# install pico => #sudo apt-get install libttspico-utils

def french_speaker(text: str):
    """French speaker"""
    cmd_speaker = f"pico2wave -l fr-FR -w tempo.wav '{text}'" 
    player_command = ["play", "tempo.wav"]
    run_command = subprocess.Popen(shlex.split(cmd_speaker))
    speak = subprocess.Popen(player_command)
    
    run_command.wait()
    speak.wait()
    
    os.remove("tempo.wav")

    
# french_speaker("Quelle est la différence entre un chrétien et un crétin: juste une consonne")