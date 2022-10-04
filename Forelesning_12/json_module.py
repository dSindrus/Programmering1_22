import json


def write_json(dictionary, filename):
    try:
        with open(filename, "w") as file:
            json.dump(dictionary, file, indent=4)
    except FileNotFoundError:
        print("File not found")

def load_json(filename):
    try:
        with open(filename) as file:
            dict_from_file = json.load(file)

    except FileNotFoundError:  # Legger til en exception som printer beskjed om error.
        print("File not found.")
    except json.decoder.JSONDecodeError:  # Legger til en exception som printer beskjed om error.
        print("File content is not JSON")

    else:
        print(dict_from_file)  # Printer filen
        print(dict_from_file["name"])