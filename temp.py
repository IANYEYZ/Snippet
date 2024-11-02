import pyautogui
import keyboard

def setPause(time):
    pyautogui.PAUSE = time

class Mouse:
    def getPos(self):
        return pyautogui.position
    def move(self, x, y):
        pyautogui.moveTo(x, y)
        return
    def moveRel(self, x, y):
        pyautogui.move(x, y)
        return
    def drag(self, x, y, duration=0, button='left'):
        if duration: pyautogui.dragTo(x, y, duration, button=button)
        else: pyautogui.dragTo(x, y, button=button)
    def click(self, x=-1, y=-1):
        if x != -1 and y != -1: pyautogui.click(x, y)
        else: pyautogui.click()