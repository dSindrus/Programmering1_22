print("-------------------------------------")

for number in range(9,102,2):               #listen defineres her fra 9-101, med et intervall på 2.
    print(number)

print("-------------------------------------")

number = 9                                  #definerer number som 9, så det er utgangspunktet før while-løkken
while number < 102:                         #"Så lenge number er mindre enn 102, printer den ut nummeret.
    print(number)
    number += 2                             #Her endres number til tallverdien det for øyeblikket har, pluss to for å kun få oddetallene.

print("-------------------------------------")
