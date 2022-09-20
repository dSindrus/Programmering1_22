print("-------------------------------------")

bok_liste = ["The Hobbit", "Farmers Giles of Ham",
             "The fellowship of the Ring", "The Two Towers", "The Return of the King",
             "The Adventures of Tom Bombadil", "Tree and Leaf"]                             #Oppretter liste med alle bøkene, og la de under hverandre for å ha litt mer oversikt i koden.
#1.

print(f"De to første bøkene er: {bok_liste[0:2]}")
print(f"De to siste bøkene er: {bok_liste[-2:]}")

print("-------------------------------------")

#2.

bok_liste.append("The Silmarillion")        #legger til nytt element i lista
bok_liste.append("Unfinished Tales")        #legger til nytt element i lista

for bøker in bok_liste:                     #La til en for-løkke for å få bøkene listet loddrett
    print(bøker)

print("-------------------------------------")
#3.

bok_liste[2] = "Lord of the Rings: Fellowship of the Ring"      #Omdefinerer elementet ved hjelp av index
bok_liste[3] = "Lord of the Rings: The Two Towers"              #Omdefinerer elementet ved hjelp av index
bok_liste[4] = "Lord of the Rings: The return of the King"      #Omdefinerer elementet ved hjelp av index
for bøker in bok_liste:
    print(bøker)

print("-------------------------------------")
#4

sorted_books = sorted(bok_liste)                                #Omdefinerer lista til en sortert liste

for bøker in sorted_books:                                      #lagde en fo-løkke for å få resultatet listet loddrett
    print(bøker)                                                

