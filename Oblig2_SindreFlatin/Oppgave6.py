print("-------------------------------------")

pakkelista = []
handling = str

while handling != "4":
    handling = input("Pakkelisten! Hva vil du gjøre?\n1) Legge til noe? \n2) Fjerne noe? \n3) Se lista \n4) Avslutte.\nSvar med et tall her:")
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
