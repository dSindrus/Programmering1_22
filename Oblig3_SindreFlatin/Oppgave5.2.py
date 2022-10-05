#print("---------------------------")

Inception = {"name": "Inception", "year": 2010, "rating": 8.7}
InsideOut = {"name": "Inside Out", "year": 2015, "rating": 8.1}
ConAir = {"name": "Con Air", "year": 1997, "rating": 6.9}

movie_list = [Inception,InsideOut,ConAir]



def add_movie(list, name, year, rating=5):
    movie_list.append({"name": name,"year": year,"rating": rating})


add_movie(movie_list, "Snatch", 2000, 8.2)
add_movie(movie_list, "The Shawshank Redemption", 1994, 9.3)
add_movie(movie_list, "Mr Nobody", 2009, 7.8)
add_movie(movie_list, "Kopps", 2003, 6.7)                           #endret tilbake til korrekt rating fra imdb.

#Koden over kopierte jeg fra oppgave 5.1, og slettet noen kommentarer og la til en rating-verdi på fimen Kopps
'''-----------------Oppgave 5.2-----------------'''
#A)
print("-----------------------------")

def print_movies(name,year,rating):
    for dictionary in movie_list:
        print(f"{dictionary[name]} - {dictionary[year]} has a rating of {dictionary[rating]}")

print_movies('name', 'year', 'rating')

print("-----------------------------")

#B)

def avarage_rating(list, rating):
    for score in movie_list:
        sum_rating = 0.0                                                #Legger en grunnverdi på rating før utregning
        for verdi in movie_list:
            sum_rating += verdi['rating']                               #legger sammen verdiene i rating
        return round(sum_rating / len(movie_list), 2)                   #regnestykke med ", 2" på slutten for å få to desimaler.

print("Gjennomsnittsratingen er" , avarage_rating('list', 'rating'))

print("-----------------------------")

#C)


def film_år(name,year):
    for dictionary in movie_list:
        if dictionary['year'] >= year:                                                                      #Sjekker verdiene i 'year' opp mot verdien i linje 54
            print(f"{dictionary['name']} - {dictionary['year']} has a rating of {dictionary['rating']}")

film_år(movie_list, 2010)







