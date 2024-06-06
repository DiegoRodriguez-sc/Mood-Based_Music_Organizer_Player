# Mood-Based Music Organizer and Player

This is a Python application that organizes music files based on their mood and allows you to play the songs. The program categorizes music into different moods (happy, sad, energetic, calm) by analyzing the song's metadata.

## Features

- Organize music files into mood-based folders
- Play, pause, unpause, and stop music
- Simple and intuitive graphical user interface

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries using `pip`.

### Required Libraries

- `mutagen`: For handling music file metadata.
- `textblob`: For analyzing the mood of the song based on its metadata.
- `pygame`: For playing music.
- `pytest`: For test

```sh
pip install mutagen textblob pygame pytest
```

## Project Structure

```sh
mood-based-music-organizer/
├── music/                  # Directory to store music files for testing
│   ├── test.mp3
│   └── test2.mp3
├── file_operations.py      # Module for file operations
├── mood_categorizer.py     # Module for categorizing music by mood
├── music_player.py         # Module for playing music
├── ui.py                   # User interface module
├── main.py                 # Main entry point
├── test/                   # Directory for tests
│   ├── test_file_operations.py
│   └── test_mood_categorizer.py
├── README.md               # This readme file
└── requirements.txt        # List of dependencies

```

## Running the Application
```sh
python main.py
```

## Running Tests
```sh
python -m unittest discover -s test
```