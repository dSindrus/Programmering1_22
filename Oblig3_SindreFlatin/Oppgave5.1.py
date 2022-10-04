print("-----------------------------")

#A)

Inception = {"name": "Inception", "year": 2010, "rating": 8.7}
InsideOut = {"name": "Inside Out", "year": 2015, "rating": 8.1}                    #Definerer 3 dictionaries med data om hver sin film
ConAir = {"name": "Con Air", "year": 1997, "rating": 6.9}

movie_list = [Inception,InsideOut,ConAir]                                               #Oppretter lista med dictionaries

print(movie_list)                                                                       #Printer listen med filmer

print("-----------------------------")

#B) OG C)


def add_movie(list, name, year, rating=5):
    movie_list.append({"name": name,"year": year,"rating": rating})


add_movie(movie_list, "Snatch", 2000, 8.2)
add_movie(movie_list, "The Shawshank Redemption", 1994, 9.3)
add_movie(movie_list, "Mr Nobody", 2009, 7.8)
add_movie(movie_list, "Kopps", 2003, )                                              #Får automatisk rating 5

print(list(movie_list))

'''for elementer in range(len(movie_list)):
    for element in movie_list:
        print(element[elementer])'''

print("-----------------------------")

#C)
'''OPPGAVE 5.1 (C)'''

