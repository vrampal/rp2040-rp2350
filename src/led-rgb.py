import board
import neopixel
from time import sleep

# Designed for Waveshare RP2040-One
# Should work on any board with NeoPixel

# ----- LED colors ------
BLACK = (  0,   0,   0)
RED   = (  0, 255,   0)
GREEN = (255,   0,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)

# ----- Init -----
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05, auto_write=True)
    
def hue2rgb(hue):
    if hue < 85:
        r = int(hue * 3)
        g = int(255 - hue * 3)
        b = 0
    elif hue < 170:
        hue -= 85
        r = int(255 - hue * 3)
        g = 0
        b = int(hue * 3)
    else:
        hue -= 170
        r = 0
        g = int(hue * 3)
        b = int(255 - hue * 3)
    return (r, g, b)

pixels[0] = RED
sleep(1.0)
pixels[0] = GREEN
sleep(1.0)
pixels[0] = BLUE
sleep(1.0)
while True:
    for hue in range(255):
        pixels[0] = hue2rgb(hue)
        sleep(0.01)    