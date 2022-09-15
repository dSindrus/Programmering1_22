print("-----------------------")

while True:
    guess = input("What is the meaning of life?: ")
    if guess == "42":
        print("That is correct.")
        break
    else:
        print("Nope, try again.")

print("Thanks for guessing! :)")