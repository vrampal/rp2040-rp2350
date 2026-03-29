import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
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
cc = ConsumerControl(usb_hid.devices)

keyboard.send(Keycode.WINDOWS, Keycode.D)
sleep(0.1)
keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.2)
layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.send(Keycode.ENTER)
for n in range(100):
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)
sleep(0.5)
keyboard.send(Keycode.F11)
sleep(2.0)
keyboard.send(Keycode.F)