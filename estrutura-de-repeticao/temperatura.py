import math
#Desenvolva um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
print("Informe 3 temperaturas em graus celcius a seguir:")
pt = int(input("Primeira temperatura: "))
st = int(input("Segunda temperatura: "))
tt = int(input("Terceira temperatura: "))

#maior e menor temperatura:
mn = (max(pt, st, tt))
print("\nTemperatura maxima =", mn)
mm = min(pt, st, tt)
print("Temperatura minima =", mm)
#media das temperaturas:
media = int(pt + st + tt) / 3
print("Media das temperaturas =", media)



