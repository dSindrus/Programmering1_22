print("--------------------------------------------------")

try:
    number_1 = int(input("Type in a whole number:"))
    number_2 = int(input("Type in another whole number:"))
    result = number_1 / number_2
    print(f"{number_1} / {number_2} = {result}")

except ValueError:
    print("You have to input a whole number!")
    print()

except ZeroDivisionError:
    print("U can't devide by zero!")
    print()

else:
    print("Everything is awesome!")                         #Kunne også limt print(f"{number_1} / {number_2} = {result}") inn her fra Try:.

print("End of program.")