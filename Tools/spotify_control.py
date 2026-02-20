"""
Spotify Desktop Automation Module
=================================
Uses PyAutoGUI to control Spotify Desktop on Windows.
These commands work WITHOUT the "Jarvis" wake word for seamless music control.
"""

import pyautogui
import time
import win32gui
import win32con

# Handle imports for both direct run and module import
try:
    from Tools.window_focus import focus_window
    from Tools.app_launcher import open_app
except ModuleNotFoundError:
    from window_focus import focus_window
    from app_launcher import open_app

SPOTIFY_STATE = {"is_open": False}


def get_spotify_window() -> int | None:
    """Find Spotify window handle."""
    result = None
    
    def callback(hwnd, _):
        nonlocal result
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).lower()
            if "spotify" in title:
                result = hwnd
                return False
        return True
    
    try:
        win32gui.EnumWindows(callback, None)
    except:
        pass
    return result


def ensure_spotify_focused() -> bool:
    """Ensure Spotify is open, focused, and ready for input."""
    hwnd = get_spotify_window()
    
    if not hwnd:
        success, _ = open_app("spotify")
        if not success:
            return False
        time.sleep(4)
        hwnd = get_spotify_window()
        if not hwnd:
            return False
    
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.2)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.3)
        
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0] + (rect[2] - rect[0]) // 2
        y = rect[1] + (rect[3] - rect[1]) // 2
        
        pyautogui.click(x, y)
        time.sleep(0.2)
        
        SPOTIFY_STATE["is_open"] = True
        return True
        
    except Exception as e:
        print(f"Focus error: {e}")
        return False


def activate_search() -> bool:
    """Activates Spotify search bar."""
    try:
        pyautogui.hotkey('ctrl', 'k')
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        return True
    except:
        return False


# ==============================================================================
# PUBLIC API - MUSIC CONTROL (NO WAKE WORD REQUIRED)
# ==============================================================================

def open_spotify_only() -> tuple[bool, str]:
    """Opens and focuses Spotify."""
    if ensure_spotify_focused():
        return True, "Spotify opened."
    return False, ""


def play_song(song_name: str) -> tuple[bool, str]:
    """Searches and plays a song."""
    if not song_name or not song_name.strip():
        return False, ""
    
    song_name = song_name.strip()
    
    if not ensure_spotify_focused():
        return False, ""
    
    try:
        if not activate_search():
            return False, ""
        
        pyautogui.typewrite(song_name, interval=0.03)
        time.sleep(0.8)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(0.3)
        
        return True, f"Playing {song_name}."
        
    except Exception as e:
        print(f"Play song error: {e}")
        return False, ""


def search_song(song_name: str) -> tuple[bool, str]:
    """Searches for a song without playing."""
    if not song_name or not song_name.strip():
        return False, ""
    
    song_name = song_name.strip()
    
    if not ensure_spotify_focused():
        return False, ""
    
    try:
        if not activate_search():
            return False, ""
        
        pyautogui.typewrite(song_name, interval=0.03)
        time.sleep(0.8)
        pyautogui.press('enter')
        
        return True, f"Searching for {song_name}."
        
    except Exception as e:
        print(f"Search error: {e}")
        return False, ""


def play_album(album_name: str) -> tuple[bool, str]:
    """Searches and plays an album."""
    if not album_name or not album_name.strip():
        return False, ""
    
    album_name = album_name.strip()
    
    if not ensure_spotify_focused():
        return False, ""
    
    try:
        if not activate_search():
            return False, ""
        
        pyautogui.typewrite(album_name, interval=0.03)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1.5)
        
        for _ in range(4):
            pyautogui.press('tab')
            time.sleep(0.15)
        
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.press('enter')
        
        return True, f"Playing album {album_name}."
        
    except Exception as e:
        print(f"Play album error: {e}")
        return False, ""


def pause_music() -> tuple[bool, str]:
    """Pauses/stops the current playback."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            pyautogui.press('space')
            return True, "Music stopped."
    except:
        pass
    return False, ""


def resume_music() -> tuple[bool, str]:
    """Resumes the current playback."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            pyautogui.press('space')
            return True, "Music resumed."
    except:
        pass
    return False, ""


def increase_volume() -> tuple[bool, str]:
    """Increases Spotify volume by pressing Ctrl+Up."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            # Press multiple times for ~5% increase
            for _ in range(5):
                pyautogui.hotkey('ctrl', 'up')
                time.sleep(0.05)
            return True, "Volume increased."
    except:
        pass
    return False, ""


def decrease_volume() -> tuple[bool, str]:
    """Decreases Spotify volume by pressing Ctrl+Down."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            # Press multiple times for ~5% decrease
            for _ in range(5):
                pyautogui.hotkey('ctrl', 'down')
                time.sleep(0.05)
            return True, "Volume decreased."
    except:
        pass
    return False, ""


def next_track() -> tuple[bool, str]:
    """Skips to next track."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'right')
            return True, "Next track."
    except:
        pass
    return False, ""


def previous_track() -> tuple[bool, str]:
    """Goes to previous track."""
    try:
        if focus_window("spotify"):
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'left')
            return True, "Previous track."
    except:
        pass
    return False, ""
