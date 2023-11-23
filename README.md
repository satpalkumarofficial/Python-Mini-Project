# Python-Mini-Project

## Audio-to-Text Converter
by-
Satpal CUSB2302332010;
Rishabh Raj CUSB2302332007; 
Nishat Raj CUSB2302332006

## Overview

The **Audio-to-Text Converter** is a Python application that allows users to transcribe audio files into text. It leverages the SpeechRecognition library for audio processing and the Pydub library for audio playback. This tool is designed to provide a simple and user-friendly interface for converting various audio formats, including WAV, FLAC, and MP3, into text.

## Features

- **Audio Transcription:** Convert spoken words from audio files into written text.
- **Supported Formats:** Process audio files in WAV, FLAC, and MP3 formats.
- **Playback Functionality:** Play and pause audio files directly within the application.
- **User-Friendly Interface:** Intuitive buttons and displays for a seamless user experience.

## How to Use

1. **Open Audio File:** Click the "Open Audio File" button to select the audio file you want to transcribe.
2. **Processing:** The application will display a "Processing..." message while transcribing the audio. Please wait.
3. **Result Display:** Once processed, the transcribed text will be displayed in the result text area.
4. **Playback:** Use the "Play" button to listen to the audio. The "Pause" button can be used to pause/resume playback.

## Requirements

- Python 3.x
- Required Python libraries: tkinter, filedialog, threading, speech_recognition, pydub, warnings, os, wave

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/satpalkumarofficial/Python-Mini-Project.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python attc.py
    ```
