import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'{currentMouseX} {currentMouseY}')
    time.sleep(1)