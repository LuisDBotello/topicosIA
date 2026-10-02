import numpy as np
import time


# NReynas.py
from NReinas.HashMap import HashMap
from topicosIA.NReinas.tablero.MatrizTablero import MatrizTablero

def millis():
    return int(time.perf_counter() * 1000)

def aSegundos(t1, t2):
    return (t2 - t1) / 1000

if __name__ == "__main__":

    tablero = MatrizTablero(7)
    tablero.colocarReinas()

    print("Tablero inicial: ")
    for i in range(tablero.get_size()):
        print("Reinas: " + str(tablero.get_reinas()[i].get_posicion()))
    
    
    #tabú
    tabu_list = HashMap()
    soluciones = HashMap()

    limite = tablero.get_combinaciones()
    iteraciones = 0
    
    tiempo = millis()
    while(True):

        if(tabu_list.__contains__(tablero.get_combinacion())): #no evaluar
            tablero.colocarReinas()
            continue

        
        tablero.evaluarColisiones()

        if (tablero.get_colisiones() == 0): 
            soluciones.__setitem__(tablero.get_combinacion(), True)
        else:
            combinacion = tablero.get_combinacion()
            tabu_list.__setitem__(combinacion, True)

        iteraciones += 1
        if(iteraciones == limite): 
            break

        tablero.colocarReinas()

    print(f"Tardó {aSegundos(tiempo, millis())} s")
    print("Soluciones encontradas: " + str(soluciones.__len__()))
    print("Iteraciones: " + str(iteraciones))
    print("Soluciones: ")
    print(soluciones.__repr__())




