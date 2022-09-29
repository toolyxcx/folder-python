from random import randint, random


from random import randint

moneda=randint(1,2)
eleccion=int(input("Digite 1 para escoger cara o 2 para sello \n"))

if moneda==1 and eleccion==1: 
    print("Salio cara, usted escogio cara, Ganaste!")

elif moneda==1 and eleccion==2:
    print("Salio cara, usted escogio sello, Perdiste!")
elif moneda==2 and eleccion==2:
    print("Salio sello, usted escogio sello, Ganaste!")
elif moneda==2 and eleccion==1:
    print("Salio sello, usted escogio cara, Perdiste!")
elif eleccion!=1 or eleccion!=2:
    print("Digitaste una opcion incorrecta")
else: 
    print("Datos incorrectos")

