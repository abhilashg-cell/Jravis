import threading
import pyttsx3
import pythoncom

# Global lock to prevent overlapping audio
_audio_lock = threading.Lock()

def speak(text: str):
    """
    Converts text to speech and plays it locally using pyttsx3.
    Thread-safe implementation with COM initialization.
    """
    if not text or not text.strip():
        return

    # Use lock to ensure only one sentence is spoken at a time
    with _audio_lock:
        try:
            # Initialize COM library for this thread
            pythoncom.CoInitialize()
            
            engine = pyttsx3.init()
            
            # Configure voice (Try to select a good English voice)
            voices = engine.getProperty('voices')
            for voice in voices:
                if "Zira" in voice.name or "English" in voice.name:
                    engine.setProperty('voice', voice.id)
                    break
            
            engine.setProperty('rate', 170)
            engine.say(text)
            engine.runAndWait()
            
        except Exception as e:
            print(f"Error during speech playback: {e}")
        finally:
            try:
                # Uninitialize COM library to free resources
                pythoncom.CoUninitialize()
            except:
                pass

if __name__ == "__main__":
    print("Testing TTS Engine...")
    speak("System initialization complete. Jarvis is ready.")

if __name__ == "__main__":
    print("Testing TTS Engine...")
    speak("System initialization complete. Jarvis is ready.")
