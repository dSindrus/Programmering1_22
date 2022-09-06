# Lag en mini-kalkulator. Ta to tall som input fra brukeren på en fornuftig måte.

tall_1 = int(input()) #Her settes brukerdefinerte tallverdi i utregningen ved hjelp av input og int.
tall_2 = int(input())

print(f"{tall_1} ganger {tall_2} = {tall_1 * tall_2}")                              # Her ganges de to tallene sammen ved hjelp av operatoren *
print(f"{tall_1} delt på {tall_2} = {tall_1 / tall_2}")                             # Her deles det første tallet med det andre ved hjelp av operatoren /
print(f"{tall_1} pluss {tall_2} = {tall_1 + tall_2}")                               # Her plusses de to tallene sammen ved hjelp av operatoren +
print(f"{tall_1} minus {tall_2} = {tall_1 - tall_2}")                               # Her regnes det første tallet minus det andre tallet.
print(f"{tall_1} modulo {tall_2} = {tall_1 % tall_2}")                              # Her regnes rest etter divisjon, til nærmeste heltall, ved hjelp av operatoren %
print(f"{tall_1} opphøyd i {tall_2} = {tall_1 ** tall_2}")                          # Her regnes tall 1 opphøyd i tall 2 ut ved hjelp av operatoren **
print (f"{tall_1} delt på {tall_2} (med nedrunding) = {tall_1 // tall_2}")          # Her deles det første tallet med det andre, og fjerner eventuelle desimaler ved hjelp av operatoren //


