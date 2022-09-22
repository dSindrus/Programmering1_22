print("------------------------------")
from math import log

def woof_woof_bark():
    print("Woof Woof Bark")


def dog_to_human_age(dog_age):                                  #Dog to human year converter
    human_equivalemt_age = 16 * log(dog_age) +31                #The result is rounded to a full year.
    return round(human_equivalemt_age)                          #dog_age is dogs actual age,
                                                                #the return is the dog's age in human years

print(dog_to_human_age(20))
print(dog_to_human_age(8))

woof_woof_bark()