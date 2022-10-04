print("-----------------------------")

#A)

Inception = {"name": "Inception", "year": 2010, "imdb-rating": 8.7}
InsideOut = {"name": "Inside Out", "year": 2015, "imdb-rating": 8.1}                    #Definerer 3 dictionaries med data om hver sin film
ConAir = {"name": "Con Air", "year": 1997, "imdb-rating": 6.9}

movie_list = [Inception,InsideOut,ConAir]                                               #Oppretter lista med dictionaries

print(movie_list)                                                                       #Printer listen med filmer

print("-----------------------------")

#B)

Snatch = {"name": "Snatch", "year": 2000, "imdb-rating": 8.2}
Shawshank = {"name": "The Shawshank Redemption", "year": 1994, "imdb-rating": 9.3}  # Definerer 3 dictionaries med data om hver sin film
Nobody = {"name": "Mr. Nobody", "year": 2009, "imdb-rating": 7.8}

new_movie_list = [Snatch, Shawshank, Nobody]

def added_movies(movie_list):
    for movies in movie_list:
        movie_list.append(new_movie_list)

added_movies(movie_list)

print("-----------------------------")


