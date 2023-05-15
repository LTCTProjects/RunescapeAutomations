import random
import threading

import mouse
import time
import tkinter
import kivy_venv

# from pyGUI import pyGUI
# gui = pyGUI()

#TODO
# Tkinter GUI
# More anti-ban measures?
# If misclicks, detect and go back to magic spellbook and restart (screen detection/recognition)
# Mouse movement macro, add variation to coordinates

class Autoclicker:
    def __init__(self):
        self._clickMinTime = 0.3
        self._clickMaxTime = 0.6
        self._doubleClickSleep = 0.3

    @property
    def clickMinTime(self):
        return self._clickMinTime

    @clickMinTime.setter
    def clickMinTime(self, value):
        self._clickMinTime = value

    def doubleClick(self):
        mouse.click("left")

        sleep = random.uniform(0.05, self._doubleClickSleep)
        # print('doubleClickDelay sleep time:', sleep )
        seconds = time.time() % 60
        print(f'Click      {seconds:.1f} s')
        print(f'Sleeping:  {sleep:.1f}  s')
        time.sleep(sleep)
        seconds = time.time() % 60
        print(f"Click      {seconds:.1f} s")
        print('-------------------------')
        mouse.click("left")

        # Random wait 5% of time for 3-8 seconds
        if(random.randint(0,100) <= 5):
            x = random.uniform(3, 8)
            print(f'Waiting {x:2.1f} seconds')
            time.sleep(x)

        # Random wait 1% of time for 20-45 seconds
        # randInt = random.randint(0, 100)
        # if(randInt <= 1):
        #     print('randomInt between 0 and 100:', randInt)
        #     x = random.uniform(20, 45)
        #     print(f'Waiting {x} seconds')
        #     time.sleep(x)

        # Random wait 0.1% of time for 70-300 seconds
        # randInt = random.randint(0, 1000)
        # if(randInt <= 1):
        #     print('randomInt between 0 and 1000:', randInt)
        #     x = random.uniform(70, 300)
        #     print(f'Waiting {x} seconds')
        #     time.sleep(x)

    def autoclick(self, minTime, maxTime):
        self.clickMinTime = minTime
        self._clickMaxTime = maxTime

    def start(self):
        while True:
            # print('raw dog ',threading.active_count())
            time.sleep(random.uniform(self.clickMinTime, self._clickMaxTime))
            self.doubleClick()
