import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = 'Screenshots images\\{}.png'.format(name)
    time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()