print("-------------------------------")

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
    print("Welcome to a game of blackjack!")
    print("-------------------------------")
    print(f"The cards have now been dealt. \nYou have a {player_hand[0]} and a {player_hand[1]} with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")


deal_cards()

player_score = bjm.calculate_hand_value(player_hand)
dealer_score = bjm.calculate_hand_value(dealer_hand)


def print_results_stand(player_score, dealer_score):
    if dealer_score > 21:
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("You win!")
    if player_score > 21:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print("Busted! You got more than 21\nDealer wins!.")
    elif player_score > dealer_score and dealer_score > 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {player_hand} with a value of {dealer_score}")
        print("You win!")
    elif dealer_score > player_score and player_score > 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {player_hand} with a value of {dealer_score}")
        print("Dealer wins!")
    elif player_score == dealer_hand:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("Equal score, no winners!")


def print_results_hit(player_score, dealer_score):
    if dealer_score > 21:
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("You win!")
    if player_score > 21:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print("Busted! You got more than 21\nDealer wins!.")
    elif player_score > dealer_score and dealer_score > 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {player_hand} with a value of {dealer_score}")
        print("You win!")
    elif dealer_score > player_score and player_score > 22:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {player_hand} with a value of {dealer_score}")
        print("Dealer wins!")
    elif player_score == dealer_hand:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("Equal score, no winners!")


#1.2 A)
while True: #player_score < 22 and dealer_score < 22:

    if player_score == 21:
        print("--------------------------------")
        print("Blackjack! You won.")
        exit()

#1.2 B,C,D)
    else:
        print("--------------------------------")
        player_input = input("Do u want to:\n1. Hit \n2. Stand \n3. Exit:")
        print("-------------------------------")
        if player_input == "1":
            print("You chose to Hit!")
            player_hand.append(random.choice(list(deck)))
            deck.remove(player_hand[-1])
            player_score = bjm.calculate_hand_value(player_hand)
            print_results_hit(player_score, dealer_score)

        elif player_input == "2":                                 #NOTETOSELF; Stand gjør pr. nå ingenting. 19.10
            print("You chose to stand!")
            print_results_stand(player_score, dealer_score)

        elif player_score < 21:
            print(f"You now have {player_hand}  with a value of {player_score}")
            print("Busted, u loose!\n You have a score of more than 21.")

        elif player_input == "3":
            print("Goodbye!")
            exit()

        else:
            exit()
