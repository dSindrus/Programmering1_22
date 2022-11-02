import dearpygui.dearpygui as dpg

def add_item():
    item_name = dpg.get_value("input_item_name")
    dpg.add_text(item_name, parent="list_view")
    item_list.append(item_name)


def delete_items():
    dpg.delete_item("list_view", children_only=True)

class Movie:
    def __init__(self, title, genre, year, score):
        self.title = title
        self.genre = genre
        self.year = year
        self.score = score

    def get_description(self):
        return f"The movie name is " \
               f"{self.title}, from the genre {self.genre}" \
               f". It was produced in {self.year} and has a IMDB-score of " \
               f"{self.score}"