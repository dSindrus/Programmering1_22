import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height = 300)

with dpg.window(no_title_bar=True, width = 400, height = 400):
    dpg.add_text("temp")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()