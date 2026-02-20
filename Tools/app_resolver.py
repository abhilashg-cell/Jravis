import os
import subprocess
import glob
import psutil
from Tools.window_focus import focus_window

# Standard Start Menu Paths
SHORTCUT_PATHS = [
    os.path.expandvars(r"%ProgramData%\Microsoft\Windows\Start Menu\Programs"),
    os.path.expandvars(r"%AppData%\Microsoft\Windows\Start Menu\Programs")
]

def search_start_menu(app_name: str) -> str | None:
    """Recursively search for logical shortcuts in Start Menu."""
    app_key = app_name.lower()
    
    for base_path in SHORTCUT_PATHS:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith(".lnk"):
                    name_without_ext = file.lower().replace(".lnk", "")
                    if app_key == name_without_ext or app_key in name_without_ext:
                        return os.path.join(root, file)
    return None

def resolve_and_launch(app_name: str) -> tuple[bool, str]:
    """
    Robust discovery strategy:
    1. Check Running -> Focus
    2. Shell Direct (PATH apps)
    3. Start Menu Search
    """
    app_key = app_name.lower().strip()

    # Step 1: Running Process Check
    if focus_window(app_key):
        return True, f"{app_key} is already running."

    # Step 2: Shell Direct (PATH apps like 'calc', 'notepad')
    try:
        # Check if exists in path using 'where'
        result = subprocess.run(f"where {app_key}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        if result.returncode == 0:
            subprocess.Popen(app_key, shell=True)
            return True, f"Opening {app_key}."
    except:
        pass

    # Step 3: Start Menu Deep Search (The heavy lifter)
    shortcut = search_start_menu(app_key)
    if shortcut:
        try:
            os.startfile(shortcut)
            return True, f"Opening {app_key}."
        except Exception as e:
            print(f"Error launching shortcut: {e}")
            
    return False, "" # Silent failure
