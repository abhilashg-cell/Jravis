import win32gui
import win32con
import win32com.client

def focus_window(app_name: str) -> bool:
    """
    Attempts to find a window matching the app_name and bring it to foreground.
    Case insensitive partial match on window title.
    """
    app_key = app_name.lower().strip()
    
    found_hwnd = None
    
    def callback(hwnd, extra):
        nonlocal found_hwnd
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).lower()
            if app_key in title:
                # Prioritize windows that look like main app windows
                if found_hwnd is None:
                    found_hwnd = hwnd
                # If exact match or close to it, prefer that? 
                # For now, take first partial match that is visible.
                
    try:
        win32gui.EnumWindows(callback, None)
        
        if found_hwnd:
            # Restore if minimized
            win32gui.ShowWindow(found_hwnd, win32con.SW_RESTORE)
            
            # Bring to front safely
            try:
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%') # Dummy key to wake up input
                win32gui.SetForegroundWindow(found_hwnd)
            except Exception as e:
                print(f"Error focussing window: {e}")
                
            return True
            
    except Exception as e:
        print(f"Window enumeration error: {e}")
        
    return False
