print("-------------------------------------")

pakkelista = []
handling = str

while handling != "4":
    handling = input("Pakkelisten! Hva vil du gjøre?\n1) Legge til noe? \n2) Fjerne noe? \n3) Se lista \n4) Avslutte.\nSvar med et tall her:")          #definerer en input med tekst og brukte \n for å få de listet loddrett
    print("------------------------")
    if handling == "1":
        pakkelista.append(input("Hva du legge til i lista?"))                   #legger til elementer i lista ved hjelp av .apppend.

    if handling == "2":
        print("------------------------")
        print(pakkelista)                                                       #La til en print av listen for oversiktens skyld.
        pakkelista.remove(input("Hva vil du fjerne fra lista?"))                   #Fjerner det definerte elementet ved hjelp av .pop

    if handling == "3":
        print("PAKKELISTA:")
        print("------------------------")
        print(pakkelista)                                                       #enkel print av lista
        print("------------------------")

    if handling == "4":
        exit()
