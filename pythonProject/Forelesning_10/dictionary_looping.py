print("------------------------")

game = {
    "name": "Dota 2",
    "genre": "MOBA",
    "max players": 10
}

for key in game:
    print(key)

print("----------------")               #To eksempler som gir samme resultat

for key in game.keys():
    print(key)

print("----------------")

for key in game.values():
    print(key)

print("----------------")

for key, value in game.items():
    print(f"{key} -> {value}")
