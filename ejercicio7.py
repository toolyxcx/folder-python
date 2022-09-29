total=0
#contador debe iniciar en 0 antes del ciclo (lo de abajo)  
minutos=0
for i in range(0,3,1):
    precio=int(input("ingrese el valor del prodructo \n"))
    cantidad=int(input("ingrese la cantidad del producto \n"))
    subtotal=precio*cantidad
    #acumulador viven dentro de un ciclo
    #aumenta en un valor variable
    
    total=total+subtotal
    #contador vive dentro de un ciclo
    #aumenta en un valor fijo
    #minutos+=1
    minutos=minutos+1
    
print(f"el costo del desayuno es {total} \n")
print(f"por esta compra ganaste {minutos} minutos para recargar a tu movil exito")


print("adios")

