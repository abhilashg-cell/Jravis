import pyautogui

def copy_selection() -> tuple[bool, str]:
    """Copies current selection (Ctrl+C)."""
    try:
        pyautogui.hotkey('ctrl', 'c')
        return True, "Copied."
    except:
        pass
    return False, ""

def paste() -> tuple[bool, str]:
    """Pastes from clipboard (Ctrl+V)."""
    try:
        pyautogui.hotkey('ctrl', 'v')
        return True, "Pasted."
    except:
        pass
    return False, ""

def select_all() -> tuple[bool, str]:
    """Selects all (Ctrl+A)."""
    try:
        pyautogui.hotkey('ctrl', 'a')
        return True, "Selected all."
    except:
        pass
    return False, ""
