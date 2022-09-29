print("---------------------------------------------------------------------------------")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15]

def get_user_weight():
    user_weight = input("What is your weight on earth?: ")
    user_weight = float(user_weight)

    if user_weight <= 0:
        print("The weight must be a positive number.")
        exit()
    return user_weight


def print_planet_choices(planet_list):
    print("\n====Planets====")
    for index in range(len(planet_list)):
        print(f"{index + 1} - {planet_list[index]}")

def get_planet__choice_index(number_of_planets):
    planet_number = input("\nPick a planet by typing a number (int): ")
    planet_number = int(planet_number)

    if planet_number < 1 or planet_number > number_of_planets:
        print("The number you entered is outside of the accepted range.")
        exit()  # Avslutter programmet.

    return planet_number - 1

def calculate_and_display_planet_weight(user_weight, gravity_list, planet_list, index):
    planet_weight = user_weight / gravity_list[2] * gravity_list[index]

    print(f"\nYour weight on {planet_list[index]} is: {planet_weight}")
    print("------------------------------------------------------------------")

while True:
    your_weight = get_user_weight()

    print_planet_choices(planets)

    planet_index = get_planet__choice_index(len(planets))

    calculate_and_display_planet_weight(your_weight, planets_gravity, planets, planet_index)

    quit = input("Do you want to quit? ")
    if quit == "yes":
        exit()

