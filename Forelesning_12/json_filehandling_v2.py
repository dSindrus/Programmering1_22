import json_module

game = {"name": "Trackmania", "genre": "Racing", "max players": 64}

filename = "text_files/game_v2.json"

json_module.write_json(game, filename)

