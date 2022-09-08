print(" ")

random_list = ["Europe", 8, 2.4, False, ["Some element", 42]]       #definere liste.
print(random_list)

print(" ")

games = ["Dark Souls", "Disco Elysium", "God of War", "Hunt: Showdown", "Dota 2"] #definere liste.
print(games)

print(" ")

print(games[2])                                 #printer et spesifikt element fra listen ved hjelp av index.
specific_game = games[1]
print(specific_game)

print("-----------------------------------------------------------------------------")

games[2] = "God of War (2018)"                  #endrinng av element med index i lista.
print(games)

print("-----------------------------------------------------------------------------")

games.append("Stardew Valley")                  #legger til ny string-verdi i lista.
print(games)

games.insert(1, "Jump King")                    #legger til ny stringverdi på en gitt plass i listen.
print(games)
games.insert(4, "Tekken 7")
print(games)

print("-----------------------------------------------------------------------------")

games.pop()                                     #fjerner det siste elemtet i lista.
print(games)

games.pop(3)                                    #fjerner et bestemt element ved hjelp av index.
print(games)

popped_game = games.pop(3)                      #definerer en variabel samtidig som det fjerner elemtet fra lista ved hjelp av pop.
print(popped_game)
print(games)

print("-----------------------------------------------------------------------------")

sorted_games = sorted(games)                    #definerer en variabel med en alfabetisk sortert liste.
print(sorted_games)
print(games)

games.sort()                                    #sorterer listen alfabetisk uten å definere en variabel først.
print(games)
games.sort(reverse=True)                        #en omvendt sortering, fra Å-A.
print(games)

print(f"Length of list: {len(games)}")                               #sjekker lengden på lista.