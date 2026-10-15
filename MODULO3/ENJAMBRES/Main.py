import matplotlib.pyplot as plt
from Enjambre import Enjambre
from GraficoEnjambre import GraficoEnjambre

plt.ion()


def funcion_objetivo(x, y):
    return 100 - (x - 3)**2 - (y - 2)**2

enjambre = Enjambre(50, funcion_objetivo,  1.5, 1.5, 0.7, limX = 100, limY = 100, )

grafico = GraficoEnjambre(enjambre)

enjambre.dispersar()

x = input()

for i in range(70):
    enjambre.iterar()
    grafico.actualizar_grafico()
    plt.pause(0.15)
    
print("El mejor valor fue: " + str(enjambre.bestgV))

print("en x = " + str(enjambre.bestgX) + ", y = " + str(enjambre.bestgY))

plt.ioff()
plt.show()
