import wmi
from Brain.personality import jarvis_speak
def get_brightness_windows():
    try:
        w = wmi.WMI(namespace='wmi')
        brightness_methods = w.WmiMonitorBrightness()
        brightness_percentage = brightness_methods[0].CurrentBrightness
        return brightness_percentage
    except Exception as e:
        return f"Error: {e}"

def check_br_persentage():
    brightness = get_brightness_windows()
    jarvis_speak(f"Current Brightness: {brightness}%")

