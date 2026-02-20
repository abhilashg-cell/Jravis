import pyautogui
import time
from Tools.app_launcher import open_app
from Tools.app_closer import close_app

# CONFIGURATION (1920x1080)
# Adjust these based on actual screen resolution and app layout
COORDS = {
    "shutter": (1830, 540), 
    "video_mode": (1850, 480),
    "photo_mode": (1850, 600), 
}

# STATE MANAGEMENT
CAMERA_STATE = {
    "is_open": False,
    "is_recording": False
}

def open_camera_interface() -> tuple[bool, str]:
    """Opens the camera and updates state."""
    if CAMERA_STATE["is_open"]:
        return True, "Camera is already open."
    
    success, msg = open_app("camera")
    if success:
        CAMERA_STATE["is_open"] = True
        time.sleep(2) # Wait for app to load
        return True, "Camera is open."
    return False, msg

def close_camera_interface() -> tuple[bool, str]:
    """Closes camera and resets state."""
    success, msg = close_app("camera")
    if success:
        CAMERA_STATE["is_open"] = False
        CAMERA_STATE["is_recording"] = False
        return True, "Camera closed."
    return False, msg

def click_photo() -> tuple[bool, str]:
    """Clicks photo only if open."""
    if not CAMERA_STATE["is_open"]:
        return False, "" # Silent failure
    
    # Ensure correct mode if needed? 
    # Usually clicking shutter works, but let's just click
    pyautogui.click(COORDS["shutter"])
    return True, "Picture captured."

def start_recording() -> tuple[bool, str]:
    """Starts video recording if open."""
    if not CAMERA_STATE["is_open"]:
        return False, "" # Silent
        
    if CAMERA_STATE["is_recording"]:
        return True, "Already recording."

    # Switch to video mode first? Assuming toggle is needed
    # For simplicity, let's assume we just click shutter in video mode
    # Or click specific mode button. 
    # Let's try to click 'video_mode' first to ensure we are in video mode
    pyautogui.click(COORDS["video_mode"]) 
    time.sleep(0.5)
    
    # Click shutter/record
    pyautogui.click(COORDS["shutter"])
    CAMERA_STATE["is_recording"] = True
    return True, "Recording started."

def stop_recording() -> tuple[bool, str]:
    """Stops recording."""
    if not CAMERA_STATE["is_open"]:
        return False, ""
        
    if not CAMERA_STATE["is_recording"]:
        return False, "Not currently recording." # Optional: silent? Prompt says "Works ONLY if recording is active"
        
    pyautogui.click(COORDS["shutter"]) # Click stop
    CAMERA_STATE["is_recording"] = False
    return True, "Recording stopped."
