lista=[]
suma=0
for i in range (0,4,1):
    nota=float(input("Digite la nota obtenida de cada uno de los talleres, recuerde que la calificación es de 0.0 a 5.0 \n"))
    lista.insert(i,nota)
    suma=suma+lista[i]
prom=suma/4
print(lista)
print(f"el promedio de las 4 notas es {prom}")
if 0.0<=prom<=2.9:
    print("Reprobaste la asignatura")
elif 3.0<=prom<=4.0:
    print("Pasaste raspando la asignatura") 
elif 4.0<=prom<=5.0:
    print("Aprobaste con buenos resultados")
    