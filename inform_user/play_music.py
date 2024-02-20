import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import re

def play_song(song):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.quit()

def song_is_valid(song):
    if re.search(r"^.+\.mp3$", song, re.IGNORECASE):
        if os.path.exists(song):
            return True
        else:
            print("There's no sunch song in this folder")
            return False
    else:
        print("Incorrect song format. It needs to end with '.mp3', try again")
        return False

def get_song():
    while True:
        song = input("Type in a song name that's in this folder: ")
        if song_is_valid(song):
            return song
        else:
            continue

def record_song(song, file_path):
    with open(file_path, "w") as file:
        file.write(song)

def set_song(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            song = file.read()
            if song_is_valid(song):
                print(f"Song is {song}")
                return song
            else:
                print("Recorded song in invalid format or doesn't exists in the folder. Input a correct song")
                song = get_song()
    else:
        print("There is no recorder song.")
        song = get_song()
    record_song(song, file_path)
    return song