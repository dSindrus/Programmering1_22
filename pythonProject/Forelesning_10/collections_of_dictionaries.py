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
