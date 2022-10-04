import random

antall_utregninger = range(3)                                                                                   #Definerer antall utregninger

def volum_utregning(antall_utregninger):
    for forsøk in antall_utregninger:                                                                           #Kjører funksjonen utifra antall_utregninger.
        lengde = random.randint(1, 10)                                                                          #definerer en tilfeldig verdi på lengde
        bredde = random.randint(1, 10)                                                                          #definerer en tilfeldig verdi på bredde
        høyde = random.randint(1, 10)                                                                           #definerer en tilfeldig verdi på høyde

        volum = lengde * bredde * høyde                                                                         #Selve utregningen
        print("------------------------")           #pynt
        print(f"Regnestykke {forsøk+1}:")                                                                       #La til en funksjon som viser hvilken uttregnning funksjonen tilhører
        print("------------------------")           #pynt
        print(f"Med lengde: {lengde}cm\n bredde: {bredde}cm\n og høyde: {høyde}cm\n er volumet: {volum}cm^3")   #printer ut de tilfeldige verdiene med tilhørende resultat hver gang funksjonen kjører.


volum_utregning(antall_utregninger)                                                                             #Printer ut et definert antall funksjoner, med forskjellige verdier og resultat.

print("------------------------")           #pynt