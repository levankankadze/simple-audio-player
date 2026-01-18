import tkinter as tk
from tkinter import ttk, filedialog, Scale
import pygame
import os
import threading
import time

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Audio Player")
        self.root.geometry("400x200")
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Variables
        self.current_file = None
        self.is_playing = False
        self.paused = False
        
        # Create GUI elements
        self.create_widgets()
        
        # Start update thread for volume control
        self.update_thread = threading.Thread(target=self.update_volume, daemon=True)
        self.update_thread.start()
    
    def create_widgets(self):
        # File selection frame
        file_frame = ttk.Frame(self.root)
        file_frame.pack(pady=10)
        
        self.file_label = ttk.Label(file_frame, text="No file selected")
        self.file_label.pack(side=tk.LEFT, padx=(0, 10))
        
        select_button = ttk.Button(file_frame, text="Choose File", command=self.select_file)
        select_button.pack(side=tk.LEFT)
        
        # Control buttons frame
        controls_frame = ttk.Frame(self.root)
        controls_frame.pack(pady=20)
        
        self.play_button = ttk.Button(controls_frame, text="Play", command=self.toggle_play)
        self.play_button.pack(side=tk.LEFT, padx=5)
        
        stop_button = ttk.Button(controls_frame, text="Stop", command=self.stop_audio)
        stop_button.pack(side=tk.LEFT, padx=5)
        
        # Volume control
        volume_frame = ttk.Frame(self.root)
        volume_frame.pack(pady=10)
        
        ttk.Label(volume_frame, text="Volume:").pack()
        
        self.volume_scale = Scale(
            volume_frame, 
            from_=0, 
            to=100, 
            orient=tk.HORIZONTAL, 
            length=200,
            command=self.change_volume
        )
        self.volume_scale.set(70)  # Default volume
        self.volume_scale.pack()
        
        # Status label
        self.status_label = ttk.Label(self.root, text="Ready")
        self.status_label.pack(pady=10)
    
    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[
                ("Audio Files", "*.mp3 *.flac *.wav *.ogg *.m4a"),
                ("MP3 Files", "*.mp3"),
                ("FLAC Files", "*.flac"),
                ("WAV Files", "*.wav"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            self.current_file = file_path
            filename = os.path.basename(file_path)
            self.file_label.config(text=filename)
            self.status_label.config(text=f"Loaded: {filename}")
    
    def toggle_play(self):
        if not self.current_file:
            self.status_label.config(text="Please select a file first!")
            return
        
        if not self.is_playing:
            self.play_audio()
        elif self.paused:
            self.resume_audio()
        else:
            self.pause_audio()
    
    def play_audio(self):
        try:
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
            self.is_playing = True
            self.paused = False
            self.play_button.config(text="Pause")
            self.status_label.config(text="Playing...")
        except pygame.error as e:
            self.status_label.config(text=f"Error: {str(e)}")
    
    def pause_audio(self):
        pygame.mixer.music.pause()
        self.paused = True
        self.play_button.config(text="Resume")
        self.status_label.config(text="Paused")
    
    def resume_audio(self):
        pygame.mixer.music.unpause()
        self.paused = False
        self.play_button.config(text="Pause")
        self.status_label.config(text="Playing...")
    
    def stop_audio(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.paused = False
        self.play_button.config(text="Play")
        self.status_label.config(text="Stopped")
    
    def change_volume(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)
    
    def update_volume(self):
        """Continuously update volume to handle real-time changes"""
        while True:
            time.sleep(0.1)  # Small delay to prevent excessive CPU usage

def main():
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()