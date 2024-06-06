import pygame
from pygame import mixer

# Initialize pygame mixer
mixer.init()

current_song = None

def play_song(file_path):
    global current_song
    if current_song:
        mixer.music.stop()
    current_song = file_path
    mixer.music.load(file_path)
    mixer.music.play()

def pause_song():
    mixer.music.pause()

def unpause_song():
    mixer.music.unpause()

def stop_song():
    global current_song
    mixer.music.stop()
    mixer.music.unload() 
    current_song = None
