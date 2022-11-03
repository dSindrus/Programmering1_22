import dearpygui.dearpygui as dpg
import random

#JEG VIL LAGE ET ENKELT PROGRAM SOM LAR EN GRUPPE LEGGE INN X ANTALL FILMER SELV, FOR SÅ Å VELGE EN TILFELDIG FILM


movie_list = []
favorite_movie = {}
movie_choice = {}


def add_movie():
    movie_title = dpg.get_value("input_movie_name")
    movie_genre = dpg.get_value("input_movie_genre")        #Mulig å ha rullgardin-meny her?
    movie_year = dpg.get_value("input_movie_year")
    movie_score = dpg.get_value("input_IMDB_score")
    favorite_movie = str(f"{movie_title} + {movie_genre} + {movie_year} + {movie_score}")
    movie_list.append(favorite_movie)
    dpg.add_text([movie_list], parent="list_view")          #Mulig å få elementene presentert vertikalt?


def delete_items():
    dpg.delete_item("list_view", children_only=True)



def random_movie():
    movie_choice = random.choice(movie_list)



dpg.create_context()
dpg.create_viewport(title="PyCharm", width=700, height=500)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Favorite movies")
    with dpg.group(horizontal=True):
        dpg.add_text("Movie name: ")
        dpg.add_input_text(tag="input_movie_name", width=200)
        '''dpg.add_button(label="Add item", callback=add_movie_title)
        dpg.add_button(label="Delete items", callback=delete_items)'''
    with dpg.group(horizontal=True):
        dpg.add_text("Movie genre: ")
        dpg.add_listbox(("Action", "Horror", "Drama", "Crime", "Thriller", "Adventure"), num_items = 5,tag="input_movie_genre", width=200)
        '''dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)'''
    with dpg.group(horizontal=True):
        dpg.add_text("Movie year: ")
        dpg.add_input_int(tag="input_movie_year", width=200)
        '''dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)'''
    with dpg.group(horizontal=True):
        dpg.add_text("IMDB-score: ")
        dpg.add_input_float(tag="input_movie_score", width=200)
        '''dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)'''
    dpg.add_button(label="Add item", callback=add_movie)
    dpg.add_button(label="Delete items", callback=delete_items)
    with dpg.child_window(tag="list_view", height=-1, width=-1):
        dpg.add_text("Movie list here!")
        #dpg.add_listbox(movie_list, tag="list_view")
    dpg.add_button(label="Choose a random movie", callback=random_movie)    #Skal velge en tilfeldig film.


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)                  #Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()