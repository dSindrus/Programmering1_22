import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.create_viewport(title="PyCharm", width=700, height=500)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Placeholder")
    with dpg.child_window(tag="menu", height=50, width=-1):                         #width = -1 setter bredden lik det opprinnelige vinduet.
        dpg.add_text("Menu")
    with dpg.child_window(tag="main", height=200, width=-1):                        #width = -1 setter bredden lik det opprinnelige vinduet.
        dpg.add_text("main")
        with dpg.group(horizontal=True):
            with dpg.child_window(tag="files", height=-1, width=100):               #height = -1, og width = -1 setter høyde og bredde lik tilhørende vindu.
                dpg.add_text("files")
                with dpg.tree_node(label="Forelesning_19"):
                    dpg.add_text("pycharm_gui.py")
                    dpg.add_text("template_py")
            with dpg.child_window(tag="editor", height=-1, width=-1):
                dpg.add_text("Editior")
                dpg.add_input_text(tag="input", multiline=True, height=-1, width=-1)
    with dpg.child_window(tag="terminal", height=-1, width=-1):
        dpg.add_text("Terminal")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)                                              #Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()