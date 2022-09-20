print("--------------------------------------------------------------")
#Fra presentasjon i forelesningen
movie= {'title': 'Soul','year': 2020, 'duration': 100, 'score':8.4}        #legger til nøkkler med tilhørende verdier til en variabel. Disse kan endres/refereres til
print(movie['title'])
print(f"Filmen varer i {movie.get('duration')} minutter")

print("--------------------------------------------------------------")

movie['director'] = 'Pete Docter'                           #Oppretter en ny nøkkel med tilhørende verdi

print(f"Filmen er regissert av {movie.get('director')}")    #henter ut kun nøkkelen vi opprettet over.

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

for key in movie:
    print(f"{key}")                                         #Printer ut nøklene fra et gitt dictionaries

for key, value in movie.items():                            #Printer ut nøkler med verdier fra dictionary'en
    print(f"{key} - {value}")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

#.pop() metoden kan brukes til å fjerne en nøkkel.
#dictionary_name.pop(nøkkel)
#del-statement kan også brukes. Den kan slette alt mulig.
#del dictionary_name[nøkkel]

movie.pop('director')
del movie['score']
print(movie)

print("--------------------------------------------------------------")
print("")
#Nytt eksempel:

game = {'name': 'Dota 2',
        'genre': 'MOBA',
}

print(game['name'])                                         #henter ut kun nøkkelen vi opprettet over.
print(game['genre'])                                        #henter ut kun nøkkelen vi opprettet over.

print(game.get('Genre'))                                    #Nøkkelen er case-sensitive

print("--------------------------------------------------------------")

game['max players'] = 10                                    #Legger til nøkkel til dictionary'en
print(game)

print("--------------------------------------------------------------")

game['name'] = 'DOTA 2'                                     #Endrer navn på element/nøkkel
print(game)

print("--------------------------------------------------------------")

game.pop('max players')                                     #Fjerner et nøkkel-element
print(game)

del game['genre']
print(game)                                                 #Annen metode å fjerne nøkkel-element