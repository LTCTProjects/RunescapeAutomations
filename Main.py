import random
import threading
from datetime import time

from autoclicker import Autoclicker
from pyGUI import pyGUI

if __name__ == '__main__':
    print('lmao')
    print('asshole',threading.active_count())
    ac = Autoclicker()
    ac_thread = threading.Thread(target=ac.start)
    ac_thread.start()

    GUI = pyGUI()
    GUI_thread = threading.Thread(target=GUI.set_main_window)
    GUI_thread.start()
