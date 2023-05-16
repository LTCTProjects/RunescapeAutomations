import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo
import threading
from autoclicker import Autoclicker

#TODO:
# Add hotkeys to stop program
# Make executable
# Default values on slider = class variables (min/max delays)
# Add library installation to readme (freeze venv??)

class pyGUI:
    def __init__(self):
        dpg.create_context()

    def setDoubleClickDelay(sender,appdata, userdata):
        # print("appdata: ", appdata, "userdata:", userdata)
        ac._doubleClickSleep = userdata

    def setClickMaxDelay(sender,appdata, userdata):
        # print("appdata: ", appdata, "userdata:", userdata)
        ac._clickMaxTime = userdata

    def setOnOff(sender,appdata, userdata):
        ac.isOn = userdata
        print(dpg.get_item_state(appdata))
        # dpg.get_item
        # print(dpg.get_item_state(sender))
        widgetState = dpg.get_item_state(appdata)
        print('initial state',widgetState['active'])
        # widgetState['active']=True
        print('widget state:',widgetState['active'])
        widgetLabel = dpg.get_item_label(appdata)
        dpg.configure_item(appdata, label='Script is ON') if widgetLabel == 'Script is OFF' else dpg.configure_item(appdata, label='Script is OFF')
        ac.isOn = False if widgetLabel == 'Script is ON' else True

    def set_main_window(self):
        dpg.create_viewport(title='Custom Title', width=600, height=600)
        with dpg.window(label='jlrewj', no_title_bar=True, no_move=True, width=600, height=600):
            # double click delay slider
            dpg.add_button(label='Max delay between double clicks. Default: 0.3s')
            slider = dpg.add_slider_float(min_value=0.03, max_value=1.5, callback=self.setDoubleClickDelay)

            # regular click delay slider
            dpg.add_button(label='Max delay between regular clicks. Default: 0.6s')
            dpg.add_slider_float(min_value=1, max_value=5, callback=self.setClickMaxDelay)

            dpg.add_button(label='Script is OFF', callback=self.setOnOff)

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


