import pyautogui
import time
from Brain.personality import jarvis_speak

# Fail-safe: Moving mouse to upper-left corner will abort pyautogui scripts
pyautogui.FAILSAFE = True

def type_text(text: str):
    """
    Types text into the currently active window.
    """
    jarvis_speak("Typing...", mood="neutral")
    pyautogui.write(text, interval=0.05)

def press_key(key: str):
    """
    Presses a specific key (e.g., 'enter', 'space', 'esc').
    """
    valid_keys = ['enter', 'space', 'esc', 'tab', 'backspace', 'up', 'down', 'left', 'right', 'win']
    
    if key.lower() in valid_keys:
        pyautogui.press(key.lower())
    else:
        print(f"Ignored unsanctioned key press request: {key}")

def minimize_window():
    """Minimizes the current window via shortcut."""
    pyautogui.hotkey('win', 'down')

def maximize_window():
    """Maximizes the current window via shortcut."""
    pyautogui.hotkey('win', 'up')
    
def close_window():
    """Closes the current window via Alt+F4."""
    jarvis_speak("Closing window.", mood="neutral")
    pyautogui.hotkey('alt', 'f4')

def take_screenshot():
    """Takes a screenshot and saves it."""
    screenshot = pyautogui.screenshot()
    path = "screenshot.png"
    screenshot.save(path)
    jarvis_speak("Screenshot saved.", mood="success")
