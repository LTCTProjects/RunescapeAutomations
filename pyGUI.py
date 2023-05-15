import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo
# import threading

class pyGUI:
    def __init__(self):
        print('pyGUI created')
        dpg.create_context()

    def callback(sender,data):
        print(sender, "returned:", data)

    def set_main_window(self):
        dpg.create_viewport(title='Custom Title', width=600, height=600)
        with dpg.window(label='jlrewj', no_title_bar=True, no_move=True, width=600, height=600):
            # double click delay slider
            dpg.add_button(label='flsdf')
            slider = dpg.add_slider_float(min_value=0.03, max_value=1, callback=self.callback)

            # regular click delay slider
            dpg.add_button(label='flsdf')
            dpg.add_slider_float(min_value=0.03, max_value=1)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()

    # clean up the dearpygui context
    # dpg.destroy_context()


