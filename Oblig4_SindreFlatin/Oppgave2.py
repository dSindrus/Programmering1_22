import random
import blackjack_module as bjm

#1.1)

deck = bjm.get_new_shuffled_deck()
player_hand = []
dealer_hand = []
player_input = "x"
chip_stack = 5
bet = int

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

    print("-------------------------------")
    print("Welcome to a game of blackjack!")
    print("-------------------------------")
    #bet = int(input("How many chips do you want to bet? \nBet:"))
    print(f"The cards have now been dealt. \n-------------------------------\nYou have a {player_hand[0]} and a {player_hand[1]} with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}, with a value of {bjm.get_card_value(dealer_hand[0])}")


def print_results_stand(player_score, dealer_score, chip_stack, bet):               #DET ER NO FUCKERY HER, FAENIHELVETE
    if dealer_score > 21:
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("You win!")
        chip_stack = chip_stack + bet
        print(f"You now have {chip_stack} chips")

    if player_score > dealer_score and player_score < 22:                               #Her fant jeg ut at jeg hadde feil tegnsetting etter "and dealer_score"
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")         #hadde feil variabel i printen. player_hand i stedet for dealer hand.
        print("You win!")
        chip_stack = chip_stack + bet
        print(f"You now have {chip_stack} chips")

    if dealer_score > player_score and dealer_score < 22:                               #Her fant jeg ut at jeg hadde feil tegnsetting etter "and dealer_score"
        print(f"Your hand is {player_hand} with a value of {player_score}")
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")         #hadde feil variabel i printen. player_hand i stedet for dealer hand.
        print("Dealer wins!")
        chip_stack -= bet
        print(f"You now have {chip_stack} chips")
        if chip_stack == 0:
            print("You're out of chips!")


    if player_score == dealer_score:
        print(f"Your hand is {player_hand} with a value of {player_score}")             #Og her fant jeg ut at jeg hadde feil variabel i statement'en. Jeg hadde først dealer_hand. Det var svært frustrerende.
        print(f"Dealer's hand is {dealer_hand} with a value of {dealer_score}")
        print("Equal score, no winners!")
        bet = 0


def print_results_hit(player_score, dealer_score, chip_stack):
    if player_score > 21:
        chip_stack = chip_stack - bet
        print(f"You now have {player_hand}  with a value of {player_score}")
        print("Busted! You got more than 21\nDealer wins!")
        print(f"You now have {chip_stack} chips")
        if chip_stack == 0:
            print("You're out of chips!")

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


# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    try:
        print("-------------------------------")
        print("Welcome to a game of blackjack!")
        print("-------------------------------")

#1.6)
        print(f"You have {chip_stack} chips.")
        bet = int(input("How many chips do you want to bet? \nBet:"))
        if chip_stack > 0:
            while chip_stack != 0:
                player_hand = []
                dealer_hand = []
                if bet <= chip_stack:
                    deal_cards()
                    player_score = bjm.calculate_hand_value(player_hand)
                    dealer_score = bjm.calculate_hand_value(dealer_hand)
 # -------------------------------------------------------------------------------------------------------------------------------------------------
 # -------------------------------------------------------------------------------------------------------------------------------------------------

                    #1.3)
                    while True:
                        # 1.2 A)
                        if player_score == 21:
                            print("--------------------------------")
                            print("Blackjack! You won.")
                            chip_stack += bet
                            print(f"You now have {chip_stack} chips")
                            print("--------------------------------")
                            choice_input = input("Do you want to play another round? \n1. Yes \n2. No \nAnswer: ")
                            bet = 0
                            if choice_input == "1":
                                player_hand = []
                                dealer_hand = []
                                deck = bjm.get_new_shuffled_deck()
                                print(f"You now have {chip_stack} chips")
                                bet = int(input("How many chips do you want to bet? \nBet:"))
                                deal_cards()
                                player_score = bjm.calculate_hand_value(player_hand)
                                dealer_score = bjm.calculate_hand_value(dealer_hand)

                            if choice_input == "2":
                                print(f"You ended the game with {chip_stack} chips")
                                with open("score_save.txt", "w") as file:                       #skriver gjenværende antall chips til save-fil
                                    file.write(f"{chip_stack}")
                                print("Okey. Goodbye!")
                                exit()


                        #1.2 B,C,D)
                        else:
                            print("--------------------------------")

                            player_input = input("Do you want to:\n1. Hit \n2. Stand \n3. Restart Game \n4. Exit \nAnswer:")
                            print("-------------------------------")
# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------
                            if player_input == "1":
                                print("You chose to Hit!")
                                print("-------------------------------")
                                player_hand.append(random.choice(list(deck)))
                                deck.remove(player_hand[-1])
                                player_score = bjm.calculate_hand_value(player_hand)
                                #dealer_score = bjm.calculate_hand_value(dealer_hand)

                                if player_score > 21:
                                    chip_stack -= bet
                                    print(f"You now have {player_hand}  with a value of {player_score}")
                                    print("Busted! You got more than 21\nDealer wins!")
                                    print(f"You now have {chip_stack} chips")
                                else:
                                    print_results_hit(player_score, dealer_score, chip_stack)

                                if chip_stack == 0:
                                    player_hand = []
                                    player_score = 0
                                    dealer_hand = []
                                    dealer_score = 0
                                    choice_input = input("Do you want to restart the game? \n1. Yes \n2. No \nAnswer: ")
                                    if choice_input == "1":
                                        chip_stack = 5
                                        deck = bjm.get_new_shuffled_deck()
                                        print(f"You have {chip_stack} chips.")
                                        bet = int(input("How many chips do you want to bet? \nBet:"))
                                        deal_cards()
                                        player_score = bjm.calculate_hand_value(player_hand)
                                        dealer_score = bjm.calculate_hand_value(dealer_hand)
                                        #print_results_stand(player_score,dealer_score,chip_stack)
                                    if choice_input == "2":
                                        print("Goodbye!")
                                        exit()

# -------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------

                            if player_input == "2":
                                print("You chose to stand!")
                                print("-------------------------------")
                                player_score = bjm.calculate_hand_value(player_hand)
                                dealer_score = bjm.calculate_hand_value(dealer_hand)

                                #1.4)
                                while dealer_score < 17:
                                    print("Dealer draws a card")
                                    dealer_hand.append(random.choice(list(deck)))
                                    deck.remove(dealer_hand[-1])
                                    dealer_score = bjm.calculate_hand_value(dealer_hand)
                                print_results_stand(player_score, dealer_score, chip_stack, bet)

                                if chip_stack == 0:
                                    player_hand = []
                                    player_score = 0
                                    dealer_hand = []
                                    dealer_score = 0
                                    choice_input = input("Do you want to restart the game? \n1. Yes \n2. No \nAnswer:")
                                    if choice_input == "1":
                                        chip_stack = 5
                                        deck = bjm.get_new_shuffled_deck()
                                        print(f"You have {chip_stack} chips.")
                                        bet = int(input("How many chips do you want to bet? \nBet:"))
                                        deal_cards()
                                        player_score = bjm.calculate_hand_value(player_hand)
                                        dealer_score = bjm.calculate_hand_value(dealer_hand)
                                        # print_results_stand(player_score,dealer_score,chip_stack)
                                    if choice_input == "2":
                                        print("Goodbye!")
                                        exit()

                                if chip_stack >= 1:
                                    chip_stack += bet
                                    choice_input = input("Do you want to play another round? \n1. Yes \n2. No \nAnswer:")
                                    bet = 0
                                    if choice_input == "1":
                                        #chip_stack = bet + chip_stack
                                        print(f"You now have {chip_stack} chips")
                                        bet = int(input("How many chips do you want to bet? \nBet:"))
                                        player_hand = []
                                        player_score = 0
                                        dealer_hand = []
                                        dealer_score = 0
                                        deck = bjm.get_new_shuffled_deck()
                                        deal_cards()

                                    if chip_stack == 0:
                                        print("You're out of chips!")
                                        choice_input = input("Do you want to restart the game? \n1. Yes \n2. No \nAnswer:")
                                        if choice_input == "1":
                                            player_hand = []
                                            player_score = 0
                                            dealer_hand = []
                                            dealer_score = 0
                                            deck = bjm.get_new_shuffled_deck()
                                            bet = int(input("How many chips do you want to bet? \nBet:"))
                                            deal_cards()

                                    if choice_input == "2":
                                        print(f"You ended the game with {chip_stack} chips")
                                        with open("score_save.txt", "w") as file:               #skriver gjenværende antall chips til save-fil
                                            file.write(f"{chip_stack}")
                                        print("Goodbye!")
                                        exit()
                                if chip_stack == 0:
                                    print("You're out of chips!")
                                    choice_input = input("Do you want to restart the game? \n1. Yes \n2. No \nAnswer:")
                                    if choice_input == "1":
                                        chip_stack = 0
                                        player_hand = []
                                        player_score = 0
                                        dealer_hand = []
                                        dealer_score = 0
                                        deck = bjm.get_new_shuffled_deck()
                                        bet = int(input("How many chips do you want to bet? \nBet:"))
                                        deal_cards()

                                    if choice_input == "2":
                                        print("Goodbye!")
                                        exit()
# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------

                            if player_input == "3":
                                player_hand = []
                                player_score = 0
                                dealer_hand = []
                                dealer_score = 0
                                chip_stack = 5
                                deck = bjm.get_new_shuffled_deck()
                                bet = int(input("How many chips do you want to bet? \nBet:"))
                                deal_cards()

                            if player_input == "4":
                                print("Goodbye!")
                                exit()
    except ValueError:
        print("The input type was not valid!")
        print("Try a number, ")
        exit()