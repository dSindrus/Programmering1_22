
person_1 = 5
person_2 = 9
person_3 = 2.5                  # Her defineres antall småkaker person 1-5 spiser i snitt på en uke
person_4 = 21
person_5 = 0
antall_personer = 5             # Her defineres totalt antall personer.

antall_kaker = person_1 + person_2 + person_3 + person_4 + person_5     # Her defineres totalt antall kaker spist. kun for å gjøre regnestykket under ryddigere.
print(" ") # Unødvendig, lagt inn for ordensskyld
print("Oversikt over hvor mange småkaker hver person spiser:")

print(" ")                      # Lagt inn for å skape mer rom mellom linjene.

print("Person 1 spiser 5 småkaker,")
print("person 2 spiser 9 småkaker,")
print("person 3 spiser 2.5 småkaker,")
print("person 4 spiser 21 småkaker,")
print("og person 5 spiser ingen kaker.")

print(" ")                      # Lagt inn for å skape mer rom mellom linjene.

print(f"Totalt antall småkaker spist er: {antall_kaker}")
print(" ")
print(f"Antall småkaker personene spiser i gjennomsnitt på en uke er da: {int(antall_kaker/antall_personer)}")     # Her regnes gjennomsnittet ut ved hjelp av dataypen int, og operatoren /.
                                                                                                                    # int fjerner desimalene, og runder i praksis ned verdien
print("---------------------------------------------------------------------------------------")                    # Unødvending, lagt inn for ordensskyld
print(f"Runder vi ikke ned, er antallet i gjennomsnitt: {float(antall_kaker/antall_personer)}")                     # Samme utregning, men ved bruk av float. Ikke nødvendig, men følte jeg måtte. :-)