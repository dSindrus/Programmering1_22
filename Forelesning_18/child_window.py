import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=800, height=600)

with dpg.window(no_title_bar=True, width=700, height=500):

    dpg.add_text("Outside child window")
    with dpg.child_window(label="child_window", width=300, height=300):     #no_scrollbar=True
        for number in range(25):
            dpg.add_text(f"Item {number}")
        dpg.add_text("Content")
    dpg.add_text("Outside child window")

    with dpg.child_window(width=-1, height=-1):
        dpg.add_text("Other content")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()