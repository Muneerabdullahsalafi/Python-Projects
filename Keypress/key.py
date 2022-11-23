# install the pynput module to run this Code
# Command = pip install pynput

import pynput
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

keyboard.press('a')
keyboard.release('a')