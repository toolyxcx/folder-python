
from random import randint

dado1=randint(1,6)
dado2=randint(1,6)


if dado1==1 and dado2==1: 
    print("Salio un par de unos en los dados, Ganaste!")

elif dado1==1 and dado2==2 or dado2==1 and dado1==2:
    print("Salio un total de tres en los dados, Ganaste!")
elif dado1==5 and dado2==6 or dado1==6 and dado2==5:
    print("Salio un total de once en los dados, Ganaste!")
elif dado1==6 and dado2==6 or dado1==6 and dado2==6: 
    print("Salio un total de doce en los dados, Ganaste!")
elif dado1==3 and dado2==6 or dado1==6 and dado2==3:
    print("Salio un total de nueve en los dados, Perdiste!")
elif dado1==2 and dado2==3 or dado1==3 and dado2==2:
    print("Salio un total de cinco en los dados, Perdiste!")
elif dado1==3 and dado2==3 or dado1==3 and dado2==3:
    print("Salio un total de seis en los dados, Perdiste!")
    

else:
    print("Perdiste!")