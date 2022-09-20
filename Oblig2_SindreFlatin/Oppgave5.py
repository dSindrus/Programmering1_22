print("-------------------------------------")
#1.
import random
antall_deltagere = int(input("Spill dart! \nHvor mange skal spille dart?:"))        #brukerbestemt antall deltagere
antall_kast = 3                                                                     #definerer antall kast

for deltager in range(antall_deltagere):                                            #definerer en deltager fra et bestemte antall deltagere.
    total_score = 0
    for kast in range(antall_kast):                                                 #begrenser antall kast til 3. Jeg kunne brukt en int i stedet for variabel, men ble  mer oversiktlig for meg å gjøre det sånn.
        score = random.randrange(0,61)                                              #definerer score til å være et tall mellom 0 og 60.
        total_score += score                                                        #legger sammen score'ne.
        print(f"Kast: {score}")                                                     #printer score etter hvert kast.
    print(f"Spiller {deltager + 1} fikk {total_score} poeng!")                      #printer til slutt totalt antall poeng.
    print("-------------------------")                                              #La inn en printet linje for å gjøre resultatet ryddigere.
print("-------------------------------------")

