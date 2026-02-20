import pyautogui
import time

# STATE
NOTES_STATE = {
    "active": False
}

def is_notes_mode() -> bool:
    return NOTES_STATE["active"]

def start_notes() -> tuple[bool, str]:
    """Starts notes dictation mode."""
    NOTES_STATE["active"] = True
    return True, "Notes mode started. I'm listening."

def stop_notes() -> tuple[bool, str]:
    """Stops notes dictation mode."""
    NOTES_STATE["active"] = False
    return True, "Notes mode stopped."

def type_text(text: str) -> tuple[bool, str]:
    """Types text into focused window."""
    try:
        pyautogui.write(text, interval=0.02)
        pyautogui.press('enter')
        return True, ""
    except Exception as e:
        print(f"Type error: {e}")
    return False, ""
