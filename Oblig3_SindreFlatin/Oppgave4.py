print("------------------------------")
import random

antall_forsøk = range(3)

def volum_utregning(antall_forsøk):
    for forsøk in antall_forsøk:                    #Kjører funksjonen utifra antall_forsøk.
        lengde = random.randint(1, 10)
        bredde = random.randint(1, 10)
        høyde = random.randint(1, 10)

        volum = lengde * bredde * høyde
        print("------------------------")           #pynt
        print(f"Forsøk {forsøk+1}")
        print(f"Med lengde: {lengde}cm\n bredde: {bredde}cm\n og høyde: {høyde}cm\n er volumet: {volum}cm^3")
        print("------------------------")

volum_utregning(antall_forsøk)

