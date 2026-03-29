import board
import digitalio
from time import sleep

# Designed for Raspberri Pi Pico
# Should work on any board with LED

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    sleep(0.5)
    led.value = False
    sleep(0.5)
