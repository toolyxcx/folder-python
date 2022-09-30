Notas=0
Cantidad=1

for i in range (0,4,1):

    Nota=float(input("Digite la nota obtenida de cada uno de los talleres, recuerde que la calificación es de 1.0 a 5.0  \n"))
    Notas=Notas+Nota
    Cantidad=Cantidad+1


Promedio=Notas/Cantidad
print("El promedio de la nota es", Promedio)

if 0.0<=Promedio<=2.9:
    print("Reprobaste la asignatura")
    

elif 3.0<=Promedio<=3.9:
    print("Pasaste raspando la asignatura") 
   

elif 4.0<=Promedio<=5.0:
    print("Aprobaste con buenos resultados")

elif Nota>5:
    print("datos incorrectos")

else:
    print("ingreso un valor invalido")






