from Automation.Automation_Brain import Auto_main_brain, clear_file
from NetHyTechSTT.listen import listen
from Brain.personality import jarvis_speak
import threading
from Brain.brain import Main_Brain
from Tools.app_launcher import open_app
from Tools.app_closer import close_app
from Tools.screen_control import handle_screen_command
from Tools.camera_control import open_camera_interface, close_camera_interface, click_photo, start_recording, stop_recording
from Tools.window_control import minimize_window, minimize_active_window, show_all_windows, open_start_menu
from Tools.browser_control import search_youtube, search_google, open_youtube
from Tools.notes_control import is_notes_mode, start_notes, stop_notes, type_text
from Tools.clipboard_control import copy_selection, paste
from Tools.spotify_control import (
    play_song, play_album, search_song, open_spotify_only,
    pause_music, resume_music, increase_volume, decrease_volume,
    next_track, previous_track
)

WAKE_WORD = "jarvis"

def check_inputs():
    import time
    output_text = ""
    while True:
        time.sleep(0.1)  # Small delay for reliable input processing
        with open("input.txt","r") as file:
            input_text = file.read().lower().strip()
        
        if input_text != output_text and input_text:
            output_text = input_text
            print(f"[DEBUG] Raw input: {output_text}")
            
            # ============================================
            # MUSIC COMMANDS (NO WAKE WORD REQUIRED)
            # These run BEFORE the wake word gate for seamless control
            # ============================================
            
            # Play song: "play believer" or "play shape of you"
            if output_text.startswith("play "):
                song_name = output_text.replace("play ", "").strip()
                if song_name:
                    success, msg = play_song(song_name)
                    if success:
                        jarvis_speak(msg, mood="success")
                continue
            
            # Stop music: "stop" or "stop song" or "stop the song"
            if output_text in ["stop", "stop song", "stop the song", "stop music", "stop the music"]:
                success, msg = pause_music()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # Resume: "resume" or "continue music"
            if output_text in ["resume", "continue", "continue music", "resume music"]:
                success, msg = resume_music()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # Volume up: "increase volume" or "volume up"
            if output_text in ["increase volume", "volume up", "louder", "increase the volume"]:
                success, msg = increase_volume()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # Volume down: "decrease volume" or "lower volume"
            if output_text in ["decrease volume", "lower volume", "volume down", "lower the volume", "decrease the volume"]:
                success, msg = decrease_volume()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # Search: "search believer"
            if output_text.startswith("search "):
                song_name = output_text.replace("search ", "").strip()
                if song_name:
                    success, msg = search_song(song_name)
                    if success:
                        jarvis_speak(msg, mood="success")
                continue
            
            # Next/Previous (no wake word)
            if output_text in ["next", "next song", "skip"]:
                success, msg = next_track()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if output_text in ["previous", "previous song", "go back"]:
                success, msg = previous_track()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # NOTES MODE (NO WAKE WORD)
            # ============================================
            if is_notes_mode():
                type_text(output_text)
                continue
            
            # ============================================
            # WAKE WORD GATE (FOR OTHER COMMANDS)
            # ============================================
            if not output_text.startswith(WAKE_WORD):
                print(f"[DEBUG] No wake word, ignoring.")
                continue
            
            # Strip wake word
            cmd = output_text.replace(WAKE_WORD, "", 1).strip()
            print(f"[DEBUG] Command after stripping wake word: {cmd}")
            
            # ============================================
            # PRIORITY 1: EXIT
            # ============================================
            if cmd in ["exit", "stop", "quit", "terminate", "shutdown"]:
                jarvis_speak("Shutting down.", mood="neutral")
                break
            
            # ============================================
            # PRIORITY 2: NOTES MODE TOGGLE
            # ============================================
            if cmd in ["start taking notes", "start notes", "take notes"]:
                success, msg = open_app("notepad")
                if success:
                    start_notes()
                    jarvis_speak("Notes mode started.", mood="success")
                continue
            
            if cmd in ["stop taking notes", "stop notes"]:
                stop_notes()
                jarvis_speak("Notes mode stopped.", mood="success")
                continue
            
            # ============================================
            # PRIORITY 3: CLOSE APP
            # ============================================
            if cmd == "close camera":
                success, msg = close_camera_interface()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd.startswith("close "):
                app_name = cmd.replace("close ", "").strip()
                if "window" not in app_name:
                    success, msg = close_app(app_name)
                    if success:
                        jarvis_speak(msg, mood="success")
                    continue
            
            # ============================================
            # PRIORITY 4: MINIMIZE
            # ============================================
            if cmd in ["minimize window", "minimize this", "minimize"]:
                success, msg = minimize_active_window()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd.startswith("minimize "):
                app_name = cmd.replace("minimize ", "").strip()
                success, msg = minimize_window(app_name)
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 5: OPEN APP
            # ============================================
            if cmd == "open camera":
                success, msg = open_camera_interface()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd in ["open start menu", "start menu"]:
                success, msg = open_start_menu()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd in ["open youtube", "youtube"]:
                success, msg = open_youtube()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd.startswith("open "):
                app_name = cmd.replace("open ", "").strip()
                success, msg = open_app(app_name)
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 6: SYSTEM CONTROLS
            # ============================================
            if cmd in ["show all windows", "show all tabs", "task view"]:
                success, msg = show_all_windows()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 7: BROWSER SEARCH
            # ============================================
            if cmd.startswith("search youtube for "):
                query = cmd.replace("search youtube for ", "").strip()
                success, msg = search_youtube(query)
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd.startswith("search google for "):
                query = cmd.replace("search google for ", "").strip()
                success, msg = search_google(query)
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 8: SPOTIFY (WAKE WORD REQUIRED)
            # ============================================
            if cmd in ["open spotify"]:
                success, msg = open_spotify_only()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd.startswith("play album "):
                album_name = cmd.replace("play album ", "").strip()
                if album_name:
                    success, msg = play_album(album_name)
                    if success:
                        jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 9: CAMERA ACTIONS
            # ============================================
            if cmd in ["click", "take picture", "capture photo"]:
                success, msg = click_photo()
                if success:
                    jarvis_speak(msg, mood="success")
                    continue
                elif cmd != "click":
                    continue  # Silent for camera-specific commands
            
            if cmd in ["start recording", "record video"]:
                success, msg = start_recording()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd in ["stop recording", "stop video"]:
                success, msg = stop_recording()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 9: SCREEN CONTROL
            # ============================================
            success, msg = handle_screen_command(cmd)
            if success:
                jarvis_speak(msg, mood="success")
                continue
            
            # ============================================
            # PRIORITY 10: CLIPBOARD
            # ============================================
            if cmd in ["copy", "copy this"]:
                success, msg = copy_selection()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            
            if cmd in ["paste", "paste this"]:
                success, msg = paste()
                if success:
                    jarvis_speak(msg, mood="success")
                continue
            # ============================================
            # PRIORITY 11: AUTOMATION
            # ============================================
            if "play music" in cmd or "weather" in cmd:
                Auto_main_brain(cmd)
                continue

            # ============================================
            # PRIORITY 12: GPT FALLBACK (Default)
            # ============================================
            print("[DEBUG] Sending to GPT brain")

            try:
                response = Main_Brain(cmd)
                jarvis_speak(response)
            except Exception as e:
                print(f"[ERROR] GPT brain failed: {e}")

            continue

def Jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
