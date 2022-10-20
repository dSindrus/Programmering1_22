import dearpygui.dearpygui as dpg

def calculate_weight():
    weight = dpg.get_value("input_weight")
    moon_weight = weight / 9.807 * 1.622
    dpg.set_value("text_output", f"Result: {moon_weight}KG")
    #print(f"your weight on the moon is {moon_weight} KG")

dpg.create_context()
dpg.create_viewport(title="Your weight on the moon", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True, width=600, height=400):
    dpg.add_text("Check what your weight is on the moon!")
    dpg.add_input_int(label="Your weight on earth", width=200, tag="input_weight")
    dpg.add_button(label="Click me", width=100, callback=calculate_weight)
    dpg.add_text("Results: ", tag="text_output")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
