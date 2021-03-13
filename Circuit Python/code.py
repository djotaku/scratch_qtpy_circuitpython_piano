import time
import board
import touchio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

touch0 = touchio.TouchIn(board.A0)
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A6)
touch5 = touchio.TouchIn(board.A7)

keyboard = Keyboard(usb_hid.devices)

print("waiting for a pin press")

while True:
    if touch0.value:
        print("Pin A0 touched")
        keyboard.press(Keycode.UP_ARROW)
        keyboard.release_all()
    if touch1.value:
        print("Pin A1 touched")
        keyboard.press(Keycode.DOWN_ARROW)
        keyboard.release_all()
    if touch2.value:
        print("Pin A2 touched")
        keyboard.press(Keycode.LEFT_ARROW)
        keyboard.release_all()
    if touch3.value:
        print("Pin A3 touched")
        keyboard.press(Keycode.RIGHT_ARROW)
        keyboard.release_all()
    if touch4.value:
        print("Pin A6 touched")
        keyboard.press(Keycode.SPACEBAR)
        keyboard.release_all()
    if touch5.value:
        print("Pin A7 touched")
        keyboard.press(Keycode.Z)
        keyboard.release_all()
    else:
        print("No key being pressed")
    time.sleep(0.5)