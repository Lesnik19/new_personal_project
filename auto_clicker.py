import mouse
import time
import keyboard


def clicker():
    mouse.click('left')
    time.sleep(0.01)


keyboard.add_hotkey('p', lambda: clicker())
keyboard.wait()
