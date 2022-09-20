print("-------------------------------------")

bok_liste = ["The Hobbit", "Farmers Giles of Ham",
             "Lord of the Rings: The fellowship of the Ring", "Lord of the Rings: The Two Towers", "Lord of the Rings: The Return of the King",
             "The Adventures of Tom Bombadil", "Tree and Leaf"]

LOTR_trilogi = []

LOTR_trilogi.append(bok_liste[2:5])             #Legger til elementer fra første liste inn i nye ved hjelp av index.
for bøker in LOTR_trilogi:
    print(bøker)

print("-------------------------------------")

LOTR = []
for trilogi in bok_liste:
    if "Lord of the Rings:" in trilogi:
        LOTR.append(trilogi)                    #Legger til elementer som inneholder "Lord of the Rings"-strengen
                                                #fra den gamle listen, til den nye.
print(LOTR)

print("-------------------------------------")
