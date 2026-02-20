import os
import subprocess
from Tools.app_resolver import resolve_and_launch

# Whitelist of allowed applications
ALLOWED_APPS = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd",
    "terminal": "powershell",
    "vs code": "code",
    "code": "code",
    "spotify": "spotify", 
    "file explorer": "explorer",
    "settings": "start ms-settings:", # Exception: Shell command needed for settings URI
    "word": "winword", 
    "excel": "excel",
    "powerpoint": "powerpnt",
    "task manager": "taskmgr",
    "camera": "start microsoft.windows.camera:",
}

def open_app(app_name: str) -> tuple[bool, str]:
    """
    Safely launches an application.
    Prioritizes Whitelist -> Dynamic Discovery -> Start Menu.
    """
    app_key = app_name.lower().strip()
    
    # 1. Whitelist Check (Fast & Known Good)
    if app_key in ALLOWED_APPS:
        command = ALLOWED_APPS[app_key]
        try:
            if command.startswith("start "):
                 os.system(command)
            else:
                 subprocess.Popen(command, shell=True) 
            return True, f"Opening {app_key} now, sir."
        except Exception as e:
            print(f"Error launching app: {e}")
            # Do not return False yet, try resolver as fallback? No, whitelist failure is usually hard error.
            return False, f"I attempted to open {app_key}, but encountered an error."

    # 2. Dynamic Resolution (Process Check -> Shell -> Start Menu)
    success, msg = resolve_and_launch(app_name)
    if success:
        return True, msg
        
    # 3. Final Silent Failure
    return False, ""
