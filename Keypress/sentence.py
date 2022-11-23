# install the pynput module to run this Code
# Command = pip install pynput

import pynput
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "this is a sentece typed by ninja technique!!!!!":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)