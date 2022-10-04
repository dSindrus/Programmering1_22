print("----------------------------------------")
import json_module

game = {"name": "Trackmania", "genre": "Racing", "max players": 64}

filename = "text_files/game_v2.json"

json_module.write_json(game, filename)

dict_from_file = json_module.load_json("text_files/game_v2.json")
print(dict_from_file)
print(dict_from_file["name"])

print("----------------------------------------")

other_dict_from_file = json_module.load_json("text_files/game.json")
print(other_dict_from_file)
print(other_dict_from_file["name"])
