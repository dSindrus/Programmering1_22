if True:
    print(" ")
    print("Look, the if-statement is True.")
    print("We can add more than one line.")
    print(" ")
statement = 2 == 2

if statement:
    print(f"Visst faen ere rekti, fordi det er {statement} bro!")
    print(" ")

if "text" == "TEXT":
    print("Tekstene er like!")

print("---------------------------------------")
print(" ")

number = int(input())
if number > 0:
    print(f"{number} is a positive number.")

if number < 0:
    print(f"{number} is a negative number")

if number == 0:
    print(f"{number} is zero")

print(" ")
print("End of story")