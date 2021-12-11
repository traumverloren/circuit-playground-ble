
# Circuit Playground NeoPixel
import time
import board
import neopixel
import touchio

# Don't forget to update board to latest circuitpython
# https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

# Use Mu editor for easiest IDE experience

# Add reqd libraries to lib/ folder on arduino
# (check serial console for errors ro know which ones)
# https://circuitpython.org/libraries

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

pixels = neopixel.NeoPixel(
    board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

while True:
    if touch_A1.value:
        print("Touched A1!")
        pixels.fill(GREEN)
        pixels.show()
    if touch_A2.value:
        print("A2 touched!")
    if touch_A3.value:
        print("A3 touched!")
    if touch_A4.value:
        print("A4 touched!")
    if touch_A5.value:
        print("A5 touched!")
    if touch_A6.value:
        print("A6 touched!")
    if touch_TX.value:
        print("TX touched!")

    time.sleep(0.01)
    pixels.fill(OFF)
    pixels.show()
