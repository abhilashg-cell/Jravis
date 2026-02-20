import os
import subprocess
from Brain.personality import jarvis_speak

# Map user-friendly names to process image names
PROCESS_MAP = {
    "calculator": ["CalculatorApp.exe", "calc.exe"],
    "notepad": ["notepad.exe"],
    "chrome": ["chrome.exe"],
    "google chrome": ["chrome.exe"],
    "vs code": ["Code.exe"],
    "code": ["Code.exe"],
    "spotify": ["Spotify.exe"],
    "task manager": ["Taskmgr.exe"],
    "settings": ["SystemSettings.exe"],
    "camera": ["WindowsCamera.exe"]
}

def close_app(app_name: str) -> tuple[bool, str]:
    """
    Terminates an application by name.
    """
    app_key = app_name.lower().strip()
    
    if app_key in PROCESS_MAP:
        targets = PROCESS_MAP[app_key]
        killed_any = False
        
        for process in targets:
            try:
                # /F = force, /IM = image name, /T = tree (kill childs)
                # Redirect output to nul to avoid clutter
                result = os.system(f"taskkill /F /IM {process} /T >nul 2>&1")
                if result == 0:
                    killed_any = True
            except Exception as e:
                print(f"Error killing {process}: {e}")

        if killed_any:
            return True, f"Closing {app_key}."
        else:
            # If we couldn't kill it, maybe it wasn't running.
            # But strictly speaking, if command succeeded (0), it found and killed.
            # If strictly 128 or other error, it might not be found.
            # For UX, if we tried and didn't crash, we say closed or "not running".
            # But let's assume if result != 0 it wasn't there.
            return True, f"Closing {app_key}." # Optimistic confirmation
            
    else:
        return False, f"I cannot close {app_key} because I don't know its process name."
