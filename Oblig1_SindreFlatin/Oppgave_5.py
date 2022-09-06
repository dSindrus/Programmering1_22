#//Note to self//
#Oversikt over hvor mange småkaker 5 personer har spist:
#Person 1: 5 småkaker
#Person 2: 9 småkaker
#Person 3: 2.3 småkaker
#Person 4: 21 småkaker
#Person 5: 0 småkaker

person_1 = 5
person_2 = 9
person_3 = 2.5                  # Her defineres antall småkaker person 1-5 spiser i snitt på en uke
person_4 = 21
person_5 = 0
antall_personer = 5     # Her defineres totalt antall personer.

antall_kaker = person_1 + person_2 + person_3 + person_4 + person_5     # Her defineres totalt antall kaker spist. kun for å gjøre regnestykket under kortere.

print("Person 1 spiser 5 småkaker, person 2 spiser 9 småkaker, person 3 spiser 2.5 småkaker, person 4 spiser 21 småkaker(jeebus), og person 5 spiser ingen kaker.")
print(" " )
print(f"Totalt antall småkaker spist er: {antall_kaker}")
print(" ")
print(f"Antall småkaker de fem personene spiser i gjennomsnitt på en uke er: {int(antall_kaker/antall_personer)}")      #Her regnes gjennomsnittet ut ved hjelp av int.
print(f"Runder vi ikke ned, er antallet i gjennomsnitt: {float(antall_kaker/antall_personer)}")     #Samme utregning gjort ved bruk av float. Ikke nødvendig, men følte jeg måtte. :-)