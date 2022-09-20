print("--------------------------------------------------------------")

games = ["Dark Souls", "Disco Elysium", "Hunt: Showdown", "Tekken 7", "Dota 2", "Hollow Knight", "Jump King"]

print(games[1:5])               #print deler av liste
print(games[2:4])               #print deler av liste

print("--------------------------------------------------------------")

print(games[1:6:2])             #intervall
print(games[:])                 #kopierer hele lista
print(games[2:])                #kopierer elementer fom. index 2
print(games[:2])                #fra start, men til, men ikke med, index 2

print("--------------------------------------------------------------")

print(games[-2])                #tar utgangspunkt i siste elemnt i liste fra -1 og nedover. Dette er nest siste element.
print(games[-5:-2])             #====||====

print("--------------------------------------------------------------")

classic_game = "Shadow of the Colussus"
print(classic_game[10:])        #printer ut del av tekst-strengen. index for hver bokstav.
