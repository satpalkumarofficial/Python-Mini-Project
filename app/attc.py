import tkinter as tk
from tkinter import filedialog
import threading
import speech_recognition as sr
from pydub import AudioSegment
import pydub.playback
import warnings
import os

class AudioToTextConverter:
    def __init__(self, master):
        self.master = master
        master.title("Audio-to-Text Converter")
        master.resizable(False, False)

        icon_path = "app_icon.ico"
        master.iconbitmap(default=icon_path)

        self.open_button = tk.Button(master, text="Open Audio File", command=self.open_file_dialog)
        self.open_button.pack(pady=10)

        self.file_name_label = tk.Label(master, text="File Name: None")
        self.file_name_label.pack(pady=5)

        self.result_text = tk.Text(master, height=10, width=50, state=tk.DISABLED)
        self.result_text.pack(pady=10)

        self.play_pause_button = tk.Button(master, text="Play", command=self.play_pause_audio)
        self.play_pause_button.pack(pady=10)

        self.audio = None  
        self.playing = False  
        self.audio_thread = None  

    def play_pause_audio(self):
        if self.audio:
            if not self.playing:
                self.play_audio()
            else:
                self.pause_audio()

    def transcribe_audio(self, audio_file_path):
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)

        try:
            transcribed_text = recognizer.recognize_google(audio_data)
            return transcribed_text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Error connecting to the speech recognition service: {e}"

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("Audio Files", "*.wav;*.flac;*.mp3")],
        )
        if file_path:
            self.file_name_label.config(text=f"File Name: {os.path.basename(file_path)}")

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Processing... Please wait.")
            self.result_text.config(state=tk.DISABLED)

            threading.Thread(target=self.process_file, args=(file_path,)).start()

    def process_file(self, file_path):
        try:
            transcribed_text = self.transcribe_audio(file_path)
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, transcribed_text)
            self.result_text.config(state=tk.DISABLED)

            self.audio = AudioSegment.from_file(file_path)

            duration_label_text = f"Duration: {self.get_audio_duration()} seconds"
            duration_label = tk.Label(self.master, text=duration_label_text)
            duration_label.pack(pady=5)

        except (sr.UnknownValueError, sr.RequestError, ValueError, wave.Error) as error:
            print(f"Error: {error}")

    def get_audio_duration(self):
        if self.audio:
            return len(self.audio) / 1000 
        else:
            return 0

    def play_audio(self):
        if self.audio and not self.playing:
            self.playing = True
            self.play_pause_button.config(text="Pause")
            self.audio_thread = threading.Thread(target=self._play_audio)
            self.audio_thread.start()

    def pause_audio(self):
        if self.audio and self.playing:
            self.playing = False
            self.play_pause_button.config(text="Resume")
            pydub.playback.stop()

    def _play_audio(self):
        try:
            pydub.playback.play(self.audio)
            self.playing = False
            self.play_pause_button.config(text="Play")
        except pydub.playback.PlaybackError as e:
            print(f"Error playing audio: {e}")

if __name__ == "__main__":
    warnings.simplefilter("ignore", category=UserWarning)
    root = tk.Tk()
    app = AudioToTextConverter(root)
    root.mainloop()
