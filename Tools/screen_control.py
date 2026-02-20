import pyautogui
import os
from Brain.personality import jarvis_speak

# Failsafe
pyautogui.FAILSAFE = True

def handle_screen_command(command: str) -> tuple[bool, str]:
    """
    Parses and executes screen/mouse commands.
    Returns (success, message).
    """
    cmd = command.lower()
    
    try:
        if "screenshot" in cmd:
            im = pyautogui.screenshot()
            im.save("screenshot.png")
            return True, "Screenshot saved."
            
        elif "double click" in cmd:
            pyautogui.doubleClick()
            return True, "Double clicked."
            
        elif "right click" in cmd:
            pyautogui.rightClick()
            return True, "Right clicked."
            
        elif "left click" in cmd or cmd == "click":
             pyautogui.click()
             return True, "Clicked."
             
        elif "move mouse" in cmd:
            # Basic relative movement
            offset = 200
            if "left" in cmd:
                pyautogui.moveRel(-offset, 0)
            elif "right" in cmd:
                pyautogui.moveRel(offset, 0)
            elif "up" in cmd:
                pyautogui.moveRel(0, -offset)
            elif "down" in cmd:
                pyautogui.moveRel(0, offset)
            return True, "Moved mouse."
            
        elif "scroll up" in cmd:
            pyautogui.scroll(500)
            return True, "Scrolled up."
            
        elif "scroll down" in cmd:
            pyautogui.scroll(-500)
            return True, "Scrolled down."
            
        return False, "" # Not a screen command
        
    except Exception as e:
        print(f"Screen control error: {e}")
        return False, "Error controlling screen."
