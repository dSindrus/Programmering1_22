import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=700, height=500)

with dpg.window(no_title_bar=True, width=700, height=500):
    
    with dpg.tab_bar():                                             #Oppretter en "tab-bar"
        with dpg.tab(label="Content1"):                             #Oppretter en tab
            dpg.add_text("OVERSKRIFT")
            with dpg.group(horizontal=True):                        #gruppe med elemter organisert horisontalt
                dpg.add_button(label="Button1")
                dpg.add_text("Some text")

        with dpg.tab(label="Content2"):                             #Oppretter en tab
            with dpg.group(width=150):                              #grupperte elementer med en bestemt bredde.
                dpg.add_button(label="button2")
                dpg.add_button(label="button3")

        with dpg.tab(label="Content3"):                             #Oppretter en tab
            with dpg.group(horizontal=True, width=150):             #Grupperte elementer med både horisontal orientering, og bestemt bredde.
                dpg.add_button(label="button4")
                dpg.add_text("TEEEEXT")
                dpg.add_button(label="button5")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()