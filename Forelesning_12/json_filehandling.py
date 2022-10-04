import json

print("--------------------------------")

game = {"name": "Gothic", "genre": "RPG", "max players": 1}         #definerer en dictionary

try:
    with open("text_files/game.json", "w") as file:
        json.dump(game, file, indent=4)             #Gjør dictionary om til fil, og indent legger til x mellomrom i filen.
except FileNotFoundError:
    print("File not found")

try:
    with open("text_files/game.json") as file:
        dict_from_file = json.load(file)

except FileNotFoundError:                           #Legger til en exception som printer beskjed om error.
    print("File not found.")
except json.decoder.JSONDecodeError:                #Legger til en exception som printer beskjed om error.
    print("File content is not JSON")

else:
    print(dict_from_file)                               #Printer filen
    print(dict_from_file["name"])                       #Printer en nøkkel i filen med []