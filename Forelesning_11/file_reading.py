print("------------------------------------------------")

'''file = open("zen_of_python.txt")
print(file.read())

file.close()'''

try:                                                            #Sjekker filnavnet stemmer ved hjelp av try og except.
    with open("text_files/zen_of_python.txt") as file:          #henter og åpner fil ved hjelp av with <åpne fil> as file:.
        print(file.read())
except FileNotFoundError:
    print("File was not found")

print("------------------------------------------------")

with open("text_files/zen_of_python.txt") as file:              #Henter ut hver linje i teskstfilen som et eget element. Vannrett, vel å merke.
    print(file.readlines())

print("------------------------------------------------")

with open("text_files/zen_of_python.txt") as file:              #Henter ut en linje fra teksten, og starter med første, andre, tredje, osv.
    print(file.readline().rstrip())                             #.rstrip fjerner tomrom fra tekstfil, eksempelvis mellomrom mellom linjer.
    print(file.readline().rstrip()) 
