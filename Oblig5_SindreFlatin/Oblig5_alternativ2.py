import dearpygui.dearpygui as dpg

movie_list = []

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


def add_movie_title():
    Movie.title = dpg.get_value("input_movie_name")
    Movie.genre
    Movie.year =
    dpg.add_text(movie_name, parent="list_view")
    movie_name = Movie.title
    #movie_list.append(movie_name)

'''def add_movie_year():
    movie_year = dpg.get_value("input_movie_name")
    dpg.add_text(movie_yaer, parent="list_view")
    movie_list.append(movie_year)'''


def delete_items():
    dpg.delete_item("list_view", children_only=True)


dpg.create_context()
dpg.create_viewport(title="PyCharm", width=700, height=500)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Favorite movies")
    with dpg.group(horizontal=True):
        dpg.add_text("Movie name: ")
        dpg.add_input_text(tag="input_item_name", width=200)
        dpg.add_button(label="Add item", callback=add_movie_title)
        dpg.add_button(label="Delete items", callback=delete_items)
    with dpg.group(horizontal=True):
        dpg.add_text("Movie genre: ")
        dpg.add_input_text(tag="input_item_name", width=200)
        dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)
    with dpg.group(horizontal=True):
        dpg.add_text("Movie year: ")
        dpg.add_input_text(tag="input_item_name", width=200)
        dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)
    with dpg.group(horizontal=True):
        dpg.add_text("IMDB-score: ")
        dpg.add_input_text(tag="input_item_name", width=200)
        dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)
    with dpg.child_window(tag="list_view", height=-1, width=-1):
        "content"

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)                                              #Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()