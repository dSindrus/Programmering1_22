print("--------------------------")

import random
import blackjack_module as bjm

#1.1)

deck = bjm.get_new_shuffled_deck()
player_hand = []
dealer_hand = []

def deal_cards():
    player_hand.append(random.choice(list(deck)))
    deck.remove(player_hand[0])
    player_hand.append(random.choice(list(deck)))
    deck.remove(player_hand[1])

    dealer_hand.append(random.choice(list(deck)))
    deck.remove(dealer_hand[0])
    dealer_hand.append(random.choice(list(deck)))
    deck.remove(dealer_hand[1])

    player_score = bjm.calculate_hand_value(player_hand)
    dealer_score = bjm.calculate_hand_value(dealer_hand)

    print(player_score)
    print(dealer_score)

    print("-------------------------------")

    print(f"The cards have been dealt. You have a {player_hand[0]}  and a {player_hand[1]} with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")

deal_cards()

player_score = bjm.calculate_hand_value(player_hand)
dealer_score = bjm.calculate_hand_value(dealer_hand)

#1.2 A)

if player_score == 21:
    print("-------------------------------")
    print("Blackjack! You won.")
#1.2 B)
else:
    print("-------------------------------")
    player_input = input("Do u want to 1. Hit or 2. Stand?:")
    print("-------------------------------")
    if player_input == "Hit":
        player_hand.append(random.choice(list(deck)))
        deck.remove(player_hand)
        print("You chose to Hit!")
        print(player_hand)
    elif player_input == "Stand":
        print("You chose to stand!")
        deal_cards()
    else:
        exit()






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