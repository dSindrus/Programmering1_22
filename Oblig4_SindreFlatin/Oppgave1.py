print("-----------------------")

#A)

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

#B)
    def get_movie(self):
        print(f"{self.title} was released in {self.year}, and currently has a score of {self.rating}")


Inception = Movie("Inception", 2010, 8.8)
TheMartian = Movie("The Martian", 2015, 8)
Joker = Movie("Joker", 2019, 8.4)

#A)
print(f"{Inception.title} was released in {Inception.year} and currently has a score of {Inception.rating}")
print(f"{TheMartian.title} was released in {TheMartian.year} and currently has a score of {TheMartian.rating}")
print(f"{Joker.title} was released in {Joker.year} and currently has a score of {Joker.rating}")

print("-----------------------------------------------------------")

#B)
Inception.get_movie()
TheMartian.get_movie()
Joker.get_movie()
