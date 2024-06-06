import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from file_operations import organize_music_by_mood
from mood_categorizer import categorize_by_mood
from music_player import play_song, pause_song, unpause_song, stop_song
import os

class MoodMusicOrganizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mood-Based Music Organizer and Player")
        self.geometry("600x400")
        self.configure(bg="#2c3e50")
        
        self.create_menu()

        self.main_frame = tk.Frame(self, bg="#34495e")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.title_label = tk.Label(
            self.main_frame, text="Mood-Based Music Organizer and Player",
            font=("Helvetica", 16, "bold"), bg="#34495e", fg="white"
        )
        self.title_label.pack(pady=10)

        self.organize_button = ttk.Button(
            self.main_frame, text="Organize Music by Mood", command=self.choose_directory
        )
        self.organize_button.pack(pady=10)

        self.play_button = ttk.Button(
            self.main_frame, text="Play a Song", command=self.play_song_ui
        )
        self.play_button.pack(pady=10)

        self.pause_button = ttk.Button(
            self.main_frame, text="Pause", command=self.pause_song_ui
        )
        self.pause_button.pack(pady=10)

        self.unpause_button = ttk.Button(
            self.main_frame, text="Unpause", command=self.unpause_song_ui
        )
        self.unpause_button.pack(pady=10)

        self.stop_button = ttk.Button(
            self.main_frame, text="Stop", command=self.stop_song_ui
        )
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(
            self.main_frame, text="", font=("Helvetica", 12), bg="#34495e", fg="white"
        )
        self.status_label.pack(pady=10)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Organize Music", command=self.choose_directory)
        file_menu.add_command(label="Play Song", command=self.play_song_ui)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)
    
    def choose_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.status_label.config(text="Organizing music by mood...")
            self.update()
            organize_music_by_mood(directory, categorize_by_mood)
            self.status_label.config(text="Music organized by mood successfully!")
    
    def play_song_ui(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            play_song(file_path)
    
    def pause_song_ui(self):
        pause_song()
    
    def unpause_song_ui(self):
        unpause_song()
    
    def stop_song_ui(self):
        stop_song()
        self.status_label.config(text="")

    def show_about(self):
        messagebox.showinfo("About", "Mood-Based Music Organizer and Player\nVersion 1.0")

def create_ui():
    app = MoodMusicOrganizerApp()
    app.mainloop()
