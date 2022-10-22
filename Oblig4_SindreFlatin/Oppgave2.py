import random
import blackjack_module as bjm

#1.1)

deck = bjm.get_new_shuffled_deck()
player_hand = []
dealer_hand = []
player_input = "x"
chip_stack = 5

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

    #print(player_score)     #Hadde denne her kun for å bekrefte at det fungerte i starten.
    #print(dealer_score)     #Hadde denne her Kun for å bekrefte at det fungerte i starten.

    '''print("-------------------------------")
    print("Welcome to a game of blackjack!")
    print("-------------------------------")'''
    print(f"The cards have now been dealt. \nYou have a {player_hand[0]} and a {player_hand[1]} with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")


def print_results_stand(player_score, dealer_score, chip_stack):
    if dealer_score > 21:
        chip_stack.append(bet)
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("You win!")
        print(f"You have now {chip_stack} chips")
    if player_score > dealer_score and player_score < 22:                               #Her fant jeg ut at jeg hadde feil tegnsetting etter "and dealer_score"
        chip_stack.append(bet)
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")         #hadde feil variabel i printen. player_hand i stedet for dealer hand.
        print("You win!")
        print(f"You have now {chip_stack} chips")
    if dealer_score > player_score and dealer_score < 22:                               #Her fant jeg ut at jeg hadde feil tegnsetting etter "and dealer_score"
        chip_stack.append(bet)
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")         #hadde feil variabel i printen. player_hand i stedet for dealer hand.
        print("Dealer wins!")
        print(f"You have now {chip_stack} chips")
    if player_score == dealer_score:                                                    #Og her fant jeg ut at jeg hadde feil variabel i statement'en. Jeg hadde først dealer_hand. Det var svært frustrerende.
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("Equal score, no winners!")

                                                                    #endte opp med å kopiere funksjonen og ha to separate, men identiske. Kun for å se om det hjalp på stand-problemet,
def print_results_hit(player_score, dealer_score):
    if dealer_score > 21:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")
    if player_score > dealer_score and player_score < 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")
    if dealer_score > player_score and dealer_score < 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")
    if player_score == dealer_score:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")


'''deal_cards()

player_score = bjm.calculate_hand_value(player_hand)
dealer_score = bjm.calculate_hand_value(dealer_hand)'''

while True:
    try:
        print("-------------------------------")
        print("Welcome to a game of blackjack!")
        print("-------------------------------")
        bet = int(input("How many chips do you want to bet? \nBet:"))
        if chip_stack > 0:
            while chip_stack != 0:
                player_hand = []
                dealer_hand = []
                if bet <= chip_stack and bet > 0:
                    deal_cards()
                    player_score = bjm.calculate_hand_value(player_hand)
                    dealer_score = bjm.calculate_hand_value(dealer_hand)

                    #1.3
                    while True: #player_input != "4":
                        # 1.2 A)
                        if player_score == 21:
                            print("--------------------------------")
                            print("Blackjack! You won.")
                            break
                        #1.2 B,C,D)
                        else:
                            print("--------------------------------")
                            while player_input != "2" or player_score < 22:
                                player_input = input("Do you want to:\n1. Hit \n2. Stand \n3. Restart \n4. Exit \nAnswer:")
                                print("-------------------------------")
                                if player_input == "1":
                                    print("You chose to Hit!")
                                    print("-------------------------------")
                                    player_hand.append(random.choice(list(deck)))
                                    deck.remove(player_hand[-1])
                                    player_score = bjm.calculate_hand_value(player_hand)
                                    print_results_hit(player_score, dealer_score)
                                    if player_score > 21:
                                        print(f"You now have {player_hand}  with a value of {player_score}")
                                        print("Busted! You got more than 21\nDealer wins!")
                                        break

                                if player_input == "2":                                 #NOTETOSELF; Stand gjør pr. nå ingenting. 19.10
                                    print("You chose to stand!")
                                    print("-------------------------------")
                                    player_score = bjm.calculate_hand_value(player_hand)
                                    dealer_score = bjm.calculate_hand_value(dealer_hand)
                                    #1.4)
                                    while dealer_score < 17:
                                        print("dealer draws a card")
                                        dealer_hand.append(random.choice(list(deck)))
                                        deck.remove(dealer_hand[-1])
                                        dealer_score = bjm.calculate_hand_value(dealer_hand)
                                    print_results_stand(player_score, dealer_score)

                                if player_input == "3":
                                    player_hand = []
                                    player_score = 0
                                    dealer_hand = []
                                    dealer_score = 0
                                    deck = bjm.get_new_shuffled_deck()
                                    deal_cards()

                                if player_input == "4":
                                    print("Goodbye!")
                                    exit()
    except ValueError:
        print("Input type was wrong")