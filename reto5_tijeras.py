from random import randint


hand1=randint(1,3)
hand2=randint(1,3)
if hand1==1 and hand2==2:
    print("sacaste piedra y el jugador 2 papel, perdiste!")
elif hand1==2 and hand2==1:
    print("sacaste papel y el jugador 2 piedra, ganaste!")
elif hand1==1 and hand2==3:
    print("sacaste piedra y el jugador 2 tijeras, ganaste!")
elif hand1==3 and hand2==1:
    print("sacaste tijeras y el jugador 2 piedra, perdiste!")
elif hand1==2 and hand2==3:
    print("sacaste papel y el jugador 2 tijeras, perdiste!")
elif hand1==3 and hand2==2:
    print("sacaste tijera y el jugador 2 papel, ganaste!")
elif hand1==1 and hand2==1 or hand1==2 and hand2==2 or hand1==3 and hand2==3:
    print("empate!")

print("adios")

    

