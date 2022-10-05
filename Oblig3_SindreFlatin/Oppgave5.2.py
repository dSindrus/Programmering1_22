print("---------------------------")

Inception = {"name": "Inception", "year": 2010, "rating": 8.7}
InsideOut = {"name": "Inside Out", "year": 2015, "rating": 8.1}                    #Definerer 3 dictionaries med data om hver sin film
ConAir = {"name": "Con Air", "year": 1997, "rating": 6.9}

movie_list = [Inception,InsideOut,ConAir]                                               #Oppretter lista med dictionaries

#print(movie_list)                                                                       #Printer listen med filmer

#print("-----------------------------")


def add_movie(list, name, year, rating=5):
    movie_list.append({"name": name,"year": year,"rating": rating})


add_movie(movie_list, "Snatch", 2000, 8.2)
add_movie(movie_list, "The Shawshank Redemption", 1994, 9.3)
add_movie(movie_list, "Mr Nobody", 2009, 7.8)
add_movie(movie_list, "Kopps", 2003, )                                              #C) Får automatisk rating 5 når man dropper å legge inn rating  i forkant.

#print(list(movie_list))

'''Oppgave 5.2'''
#A)
print("-----------------------------")

def print_movies(name,year,rating):
    for dictionary in movie_list:
        print(f"{dictionary[name]} - {dictionary[year]} has a rating of {dictionary[rating]}")

print_movies('name', 'year', 'rating')                                              #

print("-----------------------------")

#B)

def avarage_rating(list, rating):
    for score in movie_list:
        sum_rating = 0.0
        for verdi in movie_list:
            sum_rating += verdi['rating']
        return round(sum_rating / len(movie_list), 2)

print(avarage_rating('list', 'rating'))
