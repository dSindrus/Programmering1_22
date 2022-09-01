print(2 + 2)

int_1 = 42
operation_1=2

addition_result = int_1+operation_1
print(addition_result)

print(f"Division: {int_1 / operation_1}")           #Til tross for divisjonen av to int-verdier, ble resultatet en float.
                                                    #Dette er noe Python gjør selv med divisjon(deling).

print(f"Floor division: {int_1 // operation_1}")

print(f"Exponentiation: {int_1 ** operation_1}")    #eksponensiering: x^y, for eksempel. I dette tilfellet 42^2

print(f"Modulus: {int_1 % operation_1}")            #Modulus - rest etter divisjon med heltall. 42 % 2 = 0.

float_1 = 3.14

print(f"Operation with int and float: {int_1 + float_1}")  #Kombinasjon av int-verdi og float-verdi vil bli en float-verdi.

number = 0
number = number + 3
print(f"Number: {number}")  #legger til verdi på en definert variabel. Assignemnt operator
number += 1                 #samme som operasjonen over, men da med " += "
print(f"Number: {number}")
number *= 2                 #Assignment operator
print(f"Number: {number}")



