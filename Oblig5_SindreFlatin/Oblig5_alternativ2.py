import dearpygui.dearpygui as dpg
import random

#JEG VIL LAGE ET ENKELT PROGRAM SOM LAR EN GRUPPE LEGGE INN X ANTALL FILMER SELV, FOR SÅ Å LA PROGRAMMET VELGE EN TILFELDIG FILM.


movie_list = []
favorite_movie = {}



def add_movie():

    movie_title = dpg.get_value("input_movie_name")
    movie_genre = dpg.get_value("input_movie_genre")                                    #Mulig å ha rullgardin-meny her?
    movie_year = dpg.get_value("input_movie_year")
    movie_score = round(dpg.get_value("input_movie_score"), 2)                          #Runder ned desimalet, og begrenser det til kun 2 desimaler.
    favorite_movie = {f"{movie_title} {movie_genre} {movie_year} {movie_score}"}
    movie_list.append(favorite_movie)
    dpg.add_text(favorite_movie, parent="list_view")                                    #Mulig å få elementene presentert vertikalt?

    favorite_movie = None


def delete_all_items():
    dpg.delete_item("list_view", children_only=True)
    movie_list = None
    favorite_movie = None



def random_movie():
    movie_choice = random.choice(movie_list)
    dpg.add_text("---------------------------", parent="list_view")
    dpg.add_text("The random movie chosen is:", parent="list_view")
    dpg.add_text(movie_choice, parent="list_view")
    dpg.add_text("---------------------------", parent="list_view")



dpg.create_context()
dpg.create_viewport(title="PyCharm", width=800, height=600)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Favorite movies")
    with dpg.group(horizontal=True):
        dpg.add_text("Movie name: ")
        dpg.add_input_text(tag="input_movie_name", width=200)

    with dpg.group(horizontal=True):
        dpg.add_text("Movie genre: ")
        dpg.add_listbox(("Action", "Comedy", "Sci-Fi", "Horror", "Drama", "Crime", "Thriller", "Adventure", "Romance"), num_items = 5,tag="input_movie_genre", width=150)

    with dpg.group(horizontal=True):
        dpg.add_text("Movie year: ")
        dpg.add_input_int(tag="input_movie_year", width=200)

    with dpg.group(horizontal=True):
        dpg.add_text("IMDB-score: ")
        dpg.add_input_float(tag="input_movie_score", width=200)

    dpg.add_button(label="Add item", callback=add_movie)
    dpg.add_button(label="Delete items", callback=delete_all_items)

    with dpg.child_window(tag="list_view", height=200, width=270):
        #dpg.add_listbox([favorite_movie], num_items=10, tag="list_view_list", width=250)
        dpg.add_text("Movie list here!")
    dpg.add_button(label="Choose a random movie", callback=random_movie)    #Skal velge en tilfeldig film.


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)                  #Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()