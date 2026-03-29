import usb_hid
from adafruit_hid.keyboard import Keyboard
from time import sleep

# IMPORTANT: Select the different keyboard layout depending of your target
# "us" is for QWERTY, "fr" is for AZERTY, "ge" is for QWERTZ
import keyboard_layout_win_fr as keyboard_layout
from keycode_win_fr import Keycode

# Designed for Waveshare RP2040-One
# Should work on board with USB

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout.KeyboardLayout(keyboard)

keyboard.send(Keycode.WINDOWS, Keycode.D)
sleep(0.1)
keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.2)
layout.write("notepad")
keyboard.send(Keycode.ENTER)
sleep(0.5)
keyboard.send(Keycode.ENTER)
layout.write("Bonjour,")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
layout.write("Ceci est une démonstration d'une attaque par clé USB malveillante.")
keyboard.send(Keycode.ENTER)
layout.write("J'ai lancé un programme sur votre ordinateur,")
keyboard.send(Keycode.ENTER)
layout.write("et je suis en train d'écrire ce fichier sur votre bureau.")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.CONTROL, Keycode.S)
sleep(0.5)
layout.write("%userprofile%\\Desktop")
sleep(0.3)
keyboard.send(Keycode.ENTER)
sleep(0.3)
layout.write("EFFACEZ-MOI.txt")
sleep(0.3)
keyboard.send(Keycode.ENTER)