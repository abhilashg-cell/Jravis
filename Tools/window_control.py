import pyautogui
import win32gui
import win32con

def minimize_window(app_name: str) -> tuple[bool, str]:
    """Minimizes a window by app name."""
    app_key = app_name.lower().strip()
    found_hwnd = None
    
    def callback(hwnd, extra):
        nonlocal found_hwnd
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).lower()
            if app_key in title:
                found_hwnd = hwnd
                
    try:
        win32gui.EnumWindows(callback, None)
        if found_hwnd:
            win32gui.ShowWindow(found_hwnd, win32con.SW_MINIMIZE)
            return True, "Window minimized."
    except Exception as e:
        print(f"Minimize error: {e}")
    return False, ""

def minimize_active_window() -> tuple[bool, str]:
    """Minimizes the currently focused window."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            return True, "Window minimized."
    except Exception as e:
        print(f"Minimize active error: {e}")
    return False, ""

def show_all_windows() -> tuple[bool, str]:
    """Opens Task View (Win+Tab)."""
    try:
        pyautogui.hotkey('win', 'tab')
        return True, "Showing all windows."
    except Exception as e:
        print(f"Task view error: {e}")
    return False, ""

def open_start_menu() -> tuple[bool, str]:
    """Presses Windows key."""
    try:
        pyautogui.press('win')
        return True, "Start menu opened."
    except:
        pass
    return False, ""
