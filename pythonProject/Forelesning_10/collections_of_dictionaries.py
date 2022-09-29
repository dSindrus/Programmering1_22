print("--------------------------------------------")

games = [
    {"name": "Dota 2", "genre": "MOBA", "max players": 10},
    {"name": "Tekken 7", "genre": "Fighting Game", "max players": 2}
]

print(games)

print("--------------------------------------------")

games.append({"name":"Jump King", "genre": "Platformer", "max players": 1})

print(games)

print("--------------------------------------------")

print(games[0]["genre"])

games[1]["name"] = "TEKKEN 8"
print(games[1])

print("--------------------------------------------")

for game in games:                                  #itererer/leser opp ett og ett element.
    print(game)

print("--------------------------------------------")

for game in games:                                  #itererer gjennom hvert spill
    for key, value in game.items():                 #Går gjennom hver nøkkel i hvert spill, og printer det.
        print(f"{key} - {value}")
    print("----------------")

print("\n--------Using a dictionary--------")
game_dict = {
    "Dota 2": {"genre": "MOBA", "max players": 10},
    "Tekken 7": {"genre": "Fighting Game", "max players": 2},
}

print(game_dict)
print()
print(game_dict["Dota 2"])                          #printer ut tilhørende nøkkel til det spesifiserte spillet.
print()
game_dict["Jump King"] = {"genre": "Platformer", "max players": 1}

print(game_dict)

print("--------------------------------------------")

print(game_dict["Tekken 7"]["genre"])               #ut ifra en samling spill, vil vi hente ut tekken 7's sjanger.

print("--------------------------------------------")

for key, value in game_dict.items():
    print(f"The game {key} is of the {value['genre']} genre and has "           #Husk at string i string må ha forskjellige tegn ' // "
        f"{value['max players']} max players")                                  #For hvert av spillene i dictionary'n, printes ut sjanger og antall spillere.