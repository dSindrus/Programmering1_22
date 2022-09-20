#En for å legge til noe, en for å slette noe, og en for å skrive ut hele listen.
#Brukeren skal deretter kunne skrive en input for å velge hvilken kommando som skal taes i bruk.
#Programmet skal gå i en evig løkke frem til brukeren avslutter det med en egen kommando for dette.

#"Pakkelisten! Hva vil du gjøre?\n 1. Legge til noe? 2. Fjerne noe? 3. Se lista 4. Avslutte\nSvar her:"
print("-------------------------------------")

pakkelista = []
handling = int

while handling != "4":
    handling = input("Pakkelisten! Hva vil du gjøre?\n1.) Legge til noe? \n2.) Fjerne noe? \n3.) Se lista \n4.) Avslutte.\nSvar her:")
    print("------------------------")
    if handling == "1":
        pakkelista.append(input("Hva du legge til i lista?"))


    if handling == "2":
        print("------------------------")
        print(pakkelista)
        pakkelista.pop(input("Hva vil du fjerne fra lista?"))

    if handling == "3":
        print("------------------------")
        print(pakkelista)
        print("------------------------")

    if handling == "4":
        exit()
