from random import randint

election=int(input("oprima 1 para ingresar el valor de su compra o oprima 2 para ingresar la cantidad de productos\n"))
if election==1:
    compra=int(input("ingrese el valor de su compra\n"))
else:
    numeroproductos=int(input("ingrese la cantidad de productos \n"))
    valorproducto=10000
    compra=numeroproductos*valorproducto
    
descuento=randint(1,4)
if compra>=50000:
    print("El cliente puede participar para el descuento")
    if descuento==1:
        calculo=compra*0.10
        total=compra-calculo
        print("Salio bolita roja, su descuento es del 10%, su total a pagar es ", total)
    elif descuento==2:
        calculo=compra*0.30
        total=compra-calculo
        print("Salio bolita azul, su descuento es del 30%, su total a pagar es ", total)
    elif descuento==3:
        calculo=compra*0.50
        total=compra-calculo
        print("Salio bolita amarilla, su descuento es del 50%, su total a pagar es ", total)
    elif descuento==4:
        print("Salio bolita blanca, te llevas totalmente gratis tu compra")
    else:
        print("el juego escogio",descuento)
else:
    print("el cliente no puede participar para participar den beneficio de su compra, su total a pagar es",compra)
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("Ingrese el valor con el que desea pagar"))
    cambio=valorrecibido-total
    print("su compra fue de",total,", realizo el pago con",valorrecibido,"su cambio es de",cambio)
else:
    descuento==4
    print("!!ganaste!!")