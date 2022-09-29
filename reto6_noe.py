from random import randint


bola=randint(1,4)
valor=int(input("ingrese el valor de su compra \n"))
if bola==1 and valor>=50000:
    descuento=10/100
    total=valor*descuento
    print(f"felicidades ha ganado el 10% de descuento su valor a pagar es {total}")
elif bola==2 and valor>=50000:
    descuento=30/100
    total=valor*descuento
    print(f"felicidades ha ganado el 30% de desuento su valor a pagar es {total}")
elif bola==3 and valor>=50000:
    descuento=50/100
    total=valor*descuento
    print(f"felicidades ha ganado el 50% de descuento su valor a pagar es {total}")
elif bola==4 and valor>=50000:
    print("felicidades tu compra es totalmente gratis")
elif valor<50000:
    print("su valor es menor a 50000, no obtiene descuento")




    

