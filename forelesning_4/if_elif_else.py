#IF, ELIF og ELSE
print("--------------------------------------------------------------------------")

if False:
    print("Meningsløs print")
else:
    print("Detta, derimot, gir mening fordi statementen er falsk")
print(" ")


if "text" == "TEXT":
    print("Tekstene er like!")
else:
    print("Tekstene er ikke like")

print("---------------------------------------------------------------------------")

print("Sjekk om tallet er positivt, eller negativt!")
number = int(input("Skriv inn et tall her:"))
if number > 0:
    print(f"{number} er et positivt tall..")
elif number < 0:
    print(f"{number} er et negativt tall.")
else:
    print(f"{number} er hverken positivt, eller negativt.")

