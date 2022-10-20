import dearpygui.dearpygui as dpg

def print_something():
    print("The button did a thing!")

dpg.create_context()
dpg.create_viewport(title="Simple button click", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True, width=600, height=400):
    dpg.add_text("Simple button")
    dpg.add_button(label="Click me", width=150, callback=print_something)   #print_something uten (), fordi programmet vil kalle funksjonen ved programstart med ()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()