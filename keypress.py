import pyautogui
import time

try:
    while True:
        pyautogui.press('shift')  # Simulates a key press
        print("Pressed Shift to prevent idling.")
        time.sleep(300)  # Waits 5 minutes (300 seconds)
except KeyboardInterrupt:
    print("Stopped.")