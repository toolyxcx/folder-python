repetir="s"
presupuesto=100000
cantidad=0
gastos=0

while repetir=="s" or repetir=="S":
    registro=(input("digite s para registrar un gasto o n para no registrar mas gastos \n"))
    gasto=int(input("digite el valor del gasto \n"))
    gastos=gastos+gasto
    presupuesto=presupuesto-gasto
    cantidad=cantidad+1

    print("el valor del gasto es", gastos)
    print("elvalor del presupuesto que le queda es", presupuesto)
    if cantidad==3:
        repetir=input("ya no tienes derechos a mas gastos")
        break
