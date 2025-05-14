import pyautogui
import time

time.sleep(2)  # Wait to switch windows
pyautogui.write('Hello!', interval=0.1)
pyautogui.press('enter')