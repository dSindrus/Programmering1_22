print("")

for number in range(10):            #definerer og printer tallrekken 1-9
    print(number)                   #da til, men ikke med 10.

print("---------------------------")

for number in range(2,19):           #definerer og printer en tallrekke fra 2 til 19
    print(number)

print("---------------------------")

for number in range(4,41,4):         #definerer og printer en tallrekke fra 4 til 40, med intervall på 4.
    print(number)

print("---------------------------")

print(range(10))

number_list = []
for number in range(5):             #0 til 4, men ikke med 5.
    number_list.append(number)      #legger dette inn i den tomme lista.
print(number_list)

print("---------------------------")

range_list = list(range(10))        #konverterer range om til en liste
print(range_list)

print("---------------------------")

