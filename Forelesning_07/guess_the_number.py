print("---------------------------")

import random

print(random.randrange(1, 101))

guess = random.randrange(1, 101)                #genererer et tilfeldig tall mellom 1 og 100

print("---------------------------")

while guess != 69:                              #definerer ønsket tall, så lenge tallet ikke er lik ( != ) 69
    print(f"the guess was {guess}")
    guess = random.randrange(1, 101)            #genererer et tilfeldig tall på nytt
    #if guess == 69:                            #unødvendig
print("The guess was correct! The number is 69")



print("---------------------------")

