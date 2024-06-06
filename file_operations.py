import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def scan_music_directory(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]

def get_song_metadata(file_path):
    try:
        return EasyID3(file_path)
    except ID3NoHeaderError:
        return {}

def move_song_to_mood_folder(file_path, mood):
    mood_directory = os.path.join(os.path.dirname(file_path), mood)
    if not os.path.exists(mood_directory):
        os.makedirs(mood_directory)
    shutil.move(file_path, os.path.join(mood_directory, os.path.basename(file_path)))

def organize_music_by_mood(directory, categorize_by_mood):
    files = scan_music_directory(directory)
    for file in files:
        metadata = get_song_metadata(file)
        mood = categorize_by_mood(metadata)
        move_song_to_mood_folder(file, mood)
