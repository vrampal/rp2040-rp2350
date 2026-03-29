import usb_hid
from adafruit_hid.keyboard import Keyboard
from time import sleep

# IMPORTANT: Select the different keyboard layout depending of your target
# "us" is for QWERTY, "fr" is for AZERTY, "ge" is for QWERTZ
import keyboard_layout_win_us as keyboard_layout
from keycode_win_us import Keycode

# Designed for Waveshare RP2040-One
# Should work on board with USB

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout.KeyboardLayout(keyboard)

keyboard.send(Keycode.WINDOWS, Keycode.D)
sleep(0.1)
keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.2)
layout.write("https://www.fakeupdate.net/wnc/")
keyboard.send(Keycode.ENTER)
sleep(0.5)
keyboard.send(Keycode.F11)