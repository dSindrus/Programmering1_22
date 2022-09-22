print("------------------------------")

def print_game_character(character, game="Super Mario Bros"):       #Game kan vøre definert her, uten at det vil påvirke koden under.
    print(f"{character} is a character in the game {game}")

print_game_character("Link", "The Legend of Zelda.")
print_game_character("Mario", "Super Mario Bros.")
print_game_character("Apex Legends", "Pathfinder")              #Feil rekkefølge
print_game_character(game="Apex Legends", character="Pathfinder")   #riktig rekkefølge ved hjelp av keyword argument
print_game_character("Samus", game="Metroid")

print_game_character("luigi")       #Bruker defiinisjonen og henter ut spill automatisk.
