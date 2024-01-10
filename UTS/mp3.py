import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("https://www.youtube.com/watch?v=vYSyW_wb70w")

        self.mixer = mixer
        self.mixer.init()

        self.music_dir = None
        self.music_list = []
        self.current_track = 0

        self.create_widgets()

    def create_widgets(self):
        # Button untuk memilih folder musik
        self.select_folder_button = tk.Button(self.master, text="Select Music Folder", command=self.select_music_folder)
        self.select_folder_button.pack(pady=10)

        # Button untuk memutar musik
        self.play_button = tk.Button(self.master, text="Play", state=tk.DISABLED, command=self.play_music)
        self.play_button.pack(pady=5)

        # Button untuk menghentikan musik
        self.stop_button = tk.Button(self.master, text="Stop", state=tk.DISABLED, command=self.stop_music)
        self.stop_button.pack(pady=5)

        # Button untuk melompat ke trek berikutnya
        self.next_button = tk.Button(self.master, text="Next", state=tk.DISABLED, command=self.next_track)
        self.next_button.pack(pady=5)

        # Label untuk menampilkan nama trek yang sedang diputar
        self.track_label = tk.Label(self.master, text="")
        self.track_label.pack(pady=10)

    def select_music_folder(self):
        self.music_dir = filedialog.askdirectory()
        if self.music_dir:
            self.music_list = [file for file in os.listdir(self.music_dir) if file.endswith('.mp3')]
            self.current_track = 0
            self.update_track_label()
            self.update_buttons_state()

    def play_music(self):
        if self.music_dir and self.music_list:
            music_path = os.path.join(self.music_dir, self.music_list[self.current_track])
            self.mixer.music.load(music_path)
            self.mixer.music.play()
            self.update_track_label()

    def stop_music(self):
        self.mixer.music.stop()

    def next_track(self):
        if self.music_dir and self.music_list:
            self.current_track = (self.current_track + 1) % len(self.music_list)
            self.play_music()

    def update_track_label(self):
        if self.music_dir and self.music_list:
            current_track_name = self.music_list[self.current_track]
            self.track_label.config(text=f"Now Playing: {current_track_name}")

    def update_buttons_state(self):
        if self.music_dir and self.music_list:
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.NORMAL)
        else:
            self.play_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
