edad=int(input("ingresa tu edad en años \n"))

if 0<=edad<=4:
    print("El cliente ingresa gratis")
elif 4<=edad<=18:
    print("debe pagar 20 mil")
elif 18<=edad<=60:
    print("debe pagar 15 mil")
elif edad>60:
    print("debe pagar 3 mil")

else:
    print("datos incorrectos")


 

