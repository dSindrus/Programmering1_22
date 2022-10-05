print("------------------------------------------")

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

'''-------Oppgave 5.3-------'''

#A)


def list_to_file(filename):
    file = open("my_movies.txt", "w")                                                          #Oppretter, eller åpner, filen ved hjelp av open
    for filmer in filename:
        file.write(f"{filmer['name']} - {filmer['year']} has a rating of {filmer['rating']}\n")     #Skriver dataen fra de forskjellige nøklene i dictionary'en til fil
    file.close()

list_to_file(movie_list)

#B)
def read_from_file(my_movies):
    f = open("my_movies.txt", "r")
    print(f.read())                                     #åpner filen, og printer så innholdet i konsollen.

read_from_file("my_movies.txt")                         #Kjører funksjonen, som resulterer i en print av filens innhold.

