print("------------------------------")
import random

def pick_random_boardgame(boardgames):
    boardgames_index = random.randrange(len(board_games))

    return boardgames.pop(boardgames_index)


def print_list(list_to_print):
    for element in list_to_print:
        print(element)

print("===Board Games===")
board_games = ['Ubungo', 'Pandemic', 'Ticket to Ride', 'Monopoly', 'Risk']
print_list(board_games)

print("------------------------------")

picked_boardgame = pick_random_boardgame(board_games)

print(f"You picked {picked_boardgame}. Have fun playing!")

print("------------------------------")

print("Updated board game list:")
print_list(board_games)

"""print("\nRandom list:")
random_list = [42, 9001, 3.14, 'Norway', 'Python']
print_list(random_list)
"""

print("------------------------------")