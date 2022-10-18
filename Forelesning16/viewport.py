import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Det beste programmet i verden", width=800, height=500)

with dpg.window(label="window name", width=200, height=200):
    dpg.add_text("Test, test, test!")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()