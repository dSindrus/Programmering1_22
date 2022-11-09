import dearpygui.dearpygui as dpg
import random

#JEG VIL LAGE ET ENKELT PROGRAM SOM LAR EN GRUPPE LEGGE INN X ANTALL FILMER SELV, FOR SÅ Å LA PROGRAMMET VELGE EN TILFELDIG FILM.


movie_list = []
favorite_movie = {}



def add_movie():

    movie_title = dpg.get_value("input_movie_name")
    movie_genre = dpg.get_value("input_movie_genre")        #Mulig å ha rullgardin-meny her?
    movie_year = dpg.get_value("input_movie_year")
    movie_score = dpg.get_value("input_IMDB_score")
    favorite_movie = {f"{movie_title}, within the genre {movie_genre} was produced in {movie_year}, and has got an IMDB-rating of {movie_score}"}
    movie_list.append(favorite_movie)
    dpg.add_text(f"{movie_title}, within the genre {movie_genre} was produced in {movie_year}, and has got an IMDB-rating of {movie_score}") #'''(movie_list[-1]), parent="list_view")'''          #Mulig å få elementene presentert vertikalt?
    favorite_movie = ()

#def


def delete_all_items():
    dpg.delete_item("list_view", children_only=True)
    movie_list = []
    favorite_movie = ()



def random_movie():
    movie_choice = random.choice(movie_list)
    dpg.add_text((movie_choice), parent= "list_view")



dpg.create_context()
dpg.create_viewport(title="PyCharm", width=800, height=600)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Favorite movies")
    with dpg.group(horizontal=True):
        dpg.add_text("Movie name: ")
        dpg.add_input_text(tag="input_movie_name", width=200)
        '''dpg.add_button(label="Add item", callback=add_movie_title)
        dpg.add_button(label="Delete items", callback=delete_items)'''
    with dpg.group(horizontal=True):
        dpg.add_text("Movie genre: ")
        dpg.add_listbox(("Action", "Horror", "Drama", "Crime", "Thriller", "Adventure"), num_items = 5,tag="input_movie_genre", width=150)
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
    dpg.add_button(label="Delete items", callback=delete_all_items)
    with dpg.child_window(tag="list_view", height=200, width=270):
        #dpg.add_listbox([favorite_movie], num_items=10, tag="list_view_list", width=250)
        dpg.add_text("Movie list here!")
        #for x in movie_list:
            #dpg.add_listbox(movie_list, tag="list_view")
    dpg.add_button(label="Choose a random movie", callback=random_movie)    #Skal velge en tilfeldig film.


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)                  #Setter bredde og høyde lik det opprinnelige vinduet.
dpg.start_dearpygui()
dpg.destroy_context()