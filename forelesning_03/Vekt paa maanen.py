# Vekt på månen = vekt på jorden / jordens tyngdekraft * månens tyngdekraft. //brukerdefinert vekt.

my_earth_weight = input("Spesifiser egenvekt på jorden: ")      #input() alltid string, så må konverteres.

my_earth_weight = float(my_earth_weight)                        #Her konverteres string til float-verdi

earth_gravity = 9.807
moon_gravity = 1.622

moon_weight = my_earth_weight / earth_gravity * moon_gravity

print(f"Min vekt på månen er: {moon_weight} kg")