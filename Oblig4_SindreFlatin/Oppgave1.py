print("-----------------------")

#A)

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating


    def get_movie(self):
        return f"{self.title} was released in {self.year}, and currently has a score of {self.rating}"


Inception = Movie("Inception", 2010, 8.8)
TheMartian = Movie("The Martian", 2015, 8)
Joker = Movie("Joker", 2019, 8.4)

Movie.get_movie(Inception)
Movie.get_movie(TheMartian)
Movie.get_movie(Joker)