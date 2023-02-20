import shlex, subprocess
import os

# install pico => #sudo apt-get install libttspico-utils

def french_speaker(text: str):
    """French speaker"""
    cmd_speaker = f"""pico2wave -l fr-FR -w tempo.wav "{text}" && play -qV0 tempo.wav treble 20 gain -l 6 tempo 0.7 """ 
    # player_command = ["play", "tempo.wav"]
    # run_command = subprocess.Popen(shlex.split(cmd_speaker))
    # speak = subprocess.Popen(player_command)
    os.system(cmd_speaker)
    # run_command.wait()
    # speak.wait()
    
    #os.remove("tempo.wav")

    
#french_speaker("Bienvenue au bouroundi mon pays")
