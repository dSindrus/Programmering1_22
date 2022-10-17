print("--------------------------")

import random
import blackjack_module as bjm

player_hand = []
dealer_hand = []
game_deck = bjm.full_deck

def get_player_hand():
    bjm.get_new_shuffled_deck()

card1 = random.randrange(game_deck)
card2 =






'''play_blackjack = input("Do you want to play a game of blackjack?"):
while play_blackjack != "Nei":'''



'''def kort_stokk():
    kort_verdi = ["Ess","To","Tre","Fire","Fem","Seks","Sju","Åtte","Ni","Ti","Knekt","Dame","Konge"]
    kort_symbol = ["Hjerte", "Ruter", "Spar","Kløver"]
    stokk = []
    for symbol in kort_symbol:
        for kort in kort_verdi:
            stokk.append(kort + "i" + symbol)
        return stokk

def kort_verdi():
    if kort[:1] in ("Knekt","Dame","Konge", "Ess"):
        return int(10)
    elif kort[:1] in ("Ess","To","Tre","Fire","Fem","Seks","Sju","Åtte","Ni","Ti"):
        return int(kort[:1])
    elif kort[:1] == "Ess"
        print(str(kort))
        verdi = input("Vil du at dette skal være 1, eller 11?")
        while verdi != "1" or verdi != "11":
            if verdi == "1":
                return int(1)
            elif verdi == "11":
                return int(11)
            else
                verdi = input("Vil du at dette skal være 1, eller 11?")


def ny_kortstokk(stokk):
    return stokk(random.randint(0,len(stokk)-1))

def slett_kort (stokk, kort):
    return stokk.remove(kort)

spill_blackjack = ipnut("Vil du spille en runde blackjack?"):
while spill_blackjack != "Nei":
    korthånd = ny_kortstokk()
    kort1 = nytt_kort(ny_kortstokk(korthånd))
    slett_kort(ny_kortstokk(kort1))
    kort2 = ny_kortstokk(korthånd)'''