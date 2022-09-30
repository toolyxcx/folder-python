from random import randint
repeat="SI"
repetir="si"
juego=0
saldo=0

while repeat=="si" or repeat=="SI":
    plata=int(input("ingrese el saldo que desea recagar \n"))
    saldo=saldo+plata
    print("su saldo global es de ",saldo)
    if saldo>=0:
        repeat=input("si desea ingresar mas dinero escriba si, de lo contrario escriba no\n")
    else:
        break
apuesta=int(input("ingrese el valor que desea apostar \n"))
while repetir=="si" or repetir=="SI":
    moneda=randint(1,2)
    election=int(input("digite 1 para elegir cara y 2 para selccionar sello "))
    if moneda==1 and election==1:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio cara , ha elegido cara, !!EN HORA BUENA HAS GANADO!!, deberia duplicar tu apuesta")
    elif moneda==1 and election==2:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio cara, :c usted escogio sello :c , perdiste!!")
    elif moneda==2 and election==2:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio sello , ha elegido sello, !!EN HORA BUENA HAS GANADO!!, deberias duplicar tu apuesta")
    elif moneda==2 and election==1:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio sello, :c usted escogio cara :c , perdiste!!")
    elif election==1 or election==2:
        print("digitaste una opcion incorrecta")
    else:
        print("datos incorrectos")
    print("su saldo actual es",saldo)
    repetir=input("si quiere jugar de nuevo escriba si o de lo contrario escriba no \n")
    if saldo<=0:
        plata=int(input("infrese el saldo que desea recargar "))
    elif repetir=="SI" or repetir=="si":
        apuesta=int(input("ingrese el valor que desea apostar \n"))
    else:
        break
print("el numero de veces que usted jugo fue",juego,"el dinero acumulado fue",saldo)