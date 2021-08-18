import pyautogui
import time
pyautogui.FAILSAFE = False

PRICE_TEXT='0.01'
screenWidth, screenHeight = pyautogui.size()
to_ignore = [2, 245, 784, 154, 50, 141, 3, 193, 691, 40]

# delay start
time.sleep(10)

for index in range(883, 1001):
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'Pricing {index}')
    if index in to_ignore:
        print('Skipping')
        continue
    time.sleep(1)
    pyautogui.click(x=1119, y=503, button='left')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(index))
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(x=1078, y=1064, button='right')
    time.sleep(0.5)
    pyautogui.click(x=1144, y=1126, button='left')
    time.sleep(3)
    pyautogui.click(x=2557, y=439, button='left')
    time.sleep(3)
    pyautogui.click(x=1757, y=1000, button='left')
    time.sleep(0.1)
    pyautogui.typewrite(PRICE_TEXT)
    time.sleep(0.5)
    pyautogui.click(x=2255, y=1048, button='left')
    time.sleep(3)
    pyautogui.click(x=3047, y=1104, button='left')
    time.sleep(2)
    pyautogui.click(x=3174, y=28, button='left')
   