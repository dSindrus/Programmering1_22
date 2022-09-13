print("")

games_list = ["Disco Elysium", "Hunt: Showdown", "Jump King", "Stardew Valley",]

for number_in_series in range(1,4):
    games_list.append(f"Dark Souls {number_in_series}")              #Legger til hvert spill i serien til listen med spill

print(games_list)

print("---------------------------------------------------------------------")

games_without_ds = []

for game in games_list:
    if "Dark Souls" not in game:                                    #fjerner Dark Souls-spillene fra listen. Sjekker iterativt etter "Dark Souls" i hvert element.
        games_without_ds.append(game)

print(f"Games without the Dark Souls games: {games_without_ds}")
