import dearpygui.dearpygui as dpg

item_list = []

def add_item():
    item_name = dpg.get_value("input_item_name")
    dpg.add_text(item_name, parent="list_view")
    #item_list.append(item_name)


def delete_items():
    dpg.delete_item("list_view", children_only=True)

dpg.create_context()
dpg.create_viewport(title="Add and delete items", width=700, height=500)

with dpg.window(no_title_bar=True, tag="window"):
    with dpg.group(horizontal=True):
        dpg.add_text("Item name: ")
        dpg.add_input_text(tag="input_item_name", width=200)
        dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="delete items", callback=delete_items)
    with dpg.child_window(tag="list_view", height=-1, width=-1):
        "content"


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)  # Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()