import pyautogui
import time
pyautogui.FAILSAFE = False

DESCRIPTION_TEXT = '{index}/1000 of a collection of totally unique, one-of-a-kind abstract art masterpieces.'
TITLE_TEXT = 'Static Scribble #{index}'
FILE_TEXT = 'scribble{index}'
screenWidth, screenHeight = pyautogui.size()
start = 880
total = 1000

# delay start
time.sleep(10)

for index in range(start, total):
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'Creating {index}')
    time.sleep(4)
    pyautogui.click(x=3050, y=410, button='right')
    time.sleep(0.1)
    pyautogui.click(x=3046, y=470, button='left')
    time.sleep(3)
    pyautogui.click(x=1178, y=998, button='left')
    time.sleep(3)
    pyautogui.click(x=642, y=826, button='left')
    time.sleep(0.1)
    pyautogui.typewrite(FILE_TEXT.format(index=index))
    pyautogui.click(x=938, y=898, button='left')
    time.sleep(1)
    pyautogui.click(x=981, y=1690, button='left')
    time.sleep(0.1)
    pyautogui.typewrite(TITLE_TEXT.format(index=index))
    time.sleep(0.5)
    pyautogui.scroll(-250)
    time.sleep(1)
    pyautogui.click(x=1019, y=1924, button='left')
    pyautogui.typewrite(DESCRIPTION_TEXT.format(index=index))
    time.sleep(0.5)
    pyautogui.scroll(-2000)
    time.sleep(1)
    pyautogui.click(x=868, y=1718, button='left')
    time.sleep(6)
    pyautogui.click(x=3239, y=0, button='left')
   