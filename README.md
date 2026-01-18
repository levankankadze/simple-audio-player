# Simple Audio Player

A simple audio player application with the following features:
- Play/Pause functionality
- Stop button
- File selection (supports MP3, FLAC, WAV, OGG, M4A)
- Volume control slider
- GUI interface

## Features

- **Play/Pause**: Toggle between playing and pausing audio
- **Stop**: Stop the currently playing audio
- **File Selection**: Choose audio files to play (supports MP3, FLAC, WAV, OGG, M4A formats)
- **Volume Control**: Adjust audio volume with a slider

## Requirements

- Python 3.x
- pygame library
- tkinter (usually comes with Python)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python audio_player.py
```

1. Click "Choose File" to select an audio file
2. Use "Play" to start playback (changes to "Pause" when playing)
3. Use "Stop" to stop playback
4. Adjust volume using the volume slider

## Building Executable for Windows

To create a standalone .exe file for Windows:

1. Make sure you have PyInstaller installed:
   ```
   pip install pyinstaller
   ```

2. Run the build script:
   ```
   python build.py
   ```

This will create an executable file named `AudioPlayer.exe` in the `dist` folder, which can be distributed as a standalone application.

## Creating Windows Installer

After building the executable, you can create a Windows installer using tools like:
- NSIS (Nullsoft Scriptable Install System)
- Inno Setup
- Advanced Installer

These tools allow you to package the executable along with any required dependencies into a professional installer (.msi or .exe).

## Supported Formats

The audio player supports these formats through pygame:
- MP3
- FLAC
- WAV
- OGG
- M4A

Note: Support for certain formats may depend on system libraries and pygame version.