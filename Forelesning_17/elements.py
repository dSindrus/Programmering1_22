import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Elementer", width=600, height=400)

with dpg.window(label="window name", width=500, height=300):
    dpg.add_text("Dette er en statisk tekst!")
    dpg.add_input_text(label="Tekstfelt", width=150)
    dpg.add_input_int(label="Int-felt", width=150)
    dpg.add_input_float(label="Float-felt", width=150)
    dpg.add_button(label="Knapp")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()