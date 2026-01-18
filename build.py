import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies."""
    print("Installing required dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Build the executable using PyInstaller."""
    install_dependencies()
    install_pyinstaller()
    
    # Build command for Windows executable
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--windowed",          # Don't open console window (for GUI apps)
        "--name=AudioPlayer",  # Name of the executable
        "--icon=None",         # No specific icon
        "audio_player.py"
    ]
    
    try:
        print("Building executable...")
        subprocess.check_call(cmd)
        print("Executable built successfully! Check the 'dist' folder.")
        print("The executable is located at: dist/AudioPlayer.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error building executable: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_executable()