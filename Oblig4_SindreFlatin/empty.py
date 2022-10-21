def calculate_ace_player (player_hand, player_score):
    for x in player_hand and dealer_hand:
        if x["name"] == "Ace" and player_score > 21 and dealer_score > 21:
            x.update({"value": 1})


def calculate_ace_dealer (dealer_hand, dealer_score):
    for x in player_hand and dealer_hand:
        if x["name"] == "Ace" and player_score > 21 and dealer_score > 21:
            x.update({"value": 1})