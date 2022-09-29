M=0
F=0
for i in range(0,10,1):
    Genero=(input("segun tu genero marca M para masculino o F para femenino \n"))
    if Genero=="M" or Genero=="m":
        M=M+1
    else:
        F=F+1
print("El numero de personas con el genero masculino son", M)
print("el numero de personas con el genero femenino son", F)
