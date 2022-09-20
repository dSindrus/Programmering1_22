print("-------------------------------------")

number = input("Hva er meningen med livet?\n (Hint: det er et tall) :")
number = int(number)        #konverterer input'en

if number == 42:
    print("Det stemmer, meningen med livet er 42!")
elif number >= 30 and number <= 50:             #om tallet er større enn, eller lik 30, og mindre enn, eller lik 50
    print("Nærme, men feil!")
else:                                           #for alt annet, print "feil!"
    print("Feil!")

print("-------------------------------------")
