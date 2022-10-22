def calculate_ace_player (player_hand, player_score):
    for x in player_hand and player_hand:
        if x["name"] == "Ace" and player_score > 21 and dealer_score > 21:
            x.update({"value": 1})


def calculate_ace_dealer (dealer_hand, dealer_score):
    for x in player_hand and dealer_hand:
        if x["name"] == "Ace" and player_score > 21 and dealer_score > 21:
            x.update({"value": 1})

def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += get_card_value(card)
        for key, value in full_deck.items():
            if {key} in full_deck == "Ace of clubs" or {key} in full_deck == "Ace of hearts" or {key} in full_deck == "Ace of hearts" or {key} in full_deck == "Ace of hearts" and hand_value > 21:
        return hand_value


def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += get_card_value(card)
        for key in full_deck.items():
            if key in full_deck == "Ace of clubs" and hand_value > 21:
                card.update({"value": 1})
            if key in full_deck == "Ace of hearts" and hand_value > 21:
                card.update({"value": 1})
            if key in full_deck == "Ace of spades" and hand_value > 21:
                card.update({"value": 1})
            if key in full_deck == "Ace of diamonds" and hand_value > 21:
                card.update({"value": 1})
        return hand_value


def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += get_card_value(card)
        if "ace" in card and hand_value >= 21:
            hand += 1
    return hand_value