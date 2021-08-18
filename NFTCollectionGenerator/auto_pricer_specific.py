import pyautogui
import time
pyautogui.FAILSAFE = False

PRICE_TEXT='0.01'

screenWidth, screenHeight = pyautogui.size()
to_add = [61, 81, 59, 231, 205, 198, 174, 134, 132, 128, 126, 100, 97, 90, 60, 58, 46, 45, 32, 10]

# delay start
time.sleep(10)

for index in to_add:
    currentMouseX, currentMouseY = pyautogui.position()
    print ('Pricing {index}')
    time.sleep(1)
    pyautogui.click(x=980, y=10, button='left')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(index))
    pyautogui.press('enter')
    time.sleep(7)
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
    time.sleep(5)
    pyautogui.click(x=3047, y=1104, button='left')
    time.sleep(2)
    pyautogui.click(x=3174, y=28, button='left')
   