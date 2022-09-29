from timeit import repeat

repetirt="s"
repetir="S"
alcancia=0
while repetir=="s" or repetir=="S":
    plata=int(input("ingrese el valor a ahorrar \n"))
    alcancia=alcancia+plata
    if alcancia<=100000: 
        repetir=input("desea ingresar mas dinero s o n para salir \n")
        
    else:
        print(f"su valor ahorrado es {alcancia}, su alcancia esta llena")
        break
        


print(f"el total ahorrado es {alcancia} ")


