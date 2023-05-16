import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo
import threading
from autoclicker import Autoclicker

#TODO:
# Add hotkeys to stop program
# Make executable
# Default values on slider = class variables (min/max delays)


class pyGUI:
    def __init__(self):
        dpg.create_context()

    def setDoubleClickDelay(sender,appdata, userdata):
        # print("appdata: ", appdata, "userdata:", userdata)
        ac._doubleClickSleep = userdata

    def setClickMaxDelay(sender,appdata, userdata):
        # print("appdata: ", appdata, "userdata:", userdata)
        ac._clickMaxTime = userdata

    def set_main_window(self):
        dpg.create_viewport(title='Custom Title', width=600, height=600)
        with dpg.window(label='jlrewj', no_title_bar=True, no_move=True, width=600, height=600):
            # double click delay slider
            dpg.add_button(label='Max delay between double clicks. Default: 0.3s')
            slider = dpg.add_slider_float(min_value=0.03, max_value=1.5, callback=self.setDoubleClickDelay)

            # regular click delay slider
            dpg.add_button(label='Max delay between regular clicks. Default: 0.6s')
            dpg.add_slider_float(min_value=1, max_value=5, callback=self.setClickMaxDelay)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()

if __name__ == '__main__':
    print('nr active threads: ',threading.active_count())
    ac = Autoclicker()
    ac_thread = threading.Thread(target=ac.start)
    ac_thread.start()

    GUI = pyGUI()
    GUI_thread = threading.Thread(target=GUI.set_main_window)
    GUI_thread.start()

    # clean up the dearpygui context
    # dpg.destroy_context()


