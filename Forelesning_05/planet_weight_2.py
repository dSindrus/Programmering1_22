print("")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]       #Definerer liste med planeter
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]                          #Definerer liste med planetenes tyngdekraft

your_weight = input("What is your weight on earth?: ")
your_weight = float(your_weight)

if your_weight <= 0:
    print("The weight must be a positiv number.")
    exit()

print("\n===Planets===")                                #Lager oversikften med linjeavstand ved hjelp av \n
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")

planet_number = input("\nPick a planet by typing a number (int): ")             #brukerdefinert verdi utifra listen over planeter
planet_number = int(planet_number)

if planet_number < 1 or planet_number > 8:                                      #if-test for å sikre at brukeren har valgt et gyldig tall
    print("The number you entered is outside of the accepted range.")
    exit()

planet_index = planet_number -1                                                 #

#jordvekt / jordtyngdekraft * planettyngdekraft
planet_weight = your_weight / planets_gravity[2] * planets_gravity[planet_index]

print(f"Your weight on {planets[planet_index]} is: {planet_weight} kg ")

