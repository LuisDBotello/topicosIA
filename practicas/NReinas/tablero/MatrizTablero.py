import random

from topicosIA.NReinas.tablero.Tablero import Tablero
from topicosIA.NReinas.Reina import Reina

import numpy as np

class MatrizTablero(Tablero):
    
    reinas = None
    colisiones = None
    combinacion = None

    def __init__(self, size):
        self.size = size
        self.tablero = np.zeros((size, size))
        self.colisiones = 0
        self.reinas = np.array([Reina(i, np.array([-1, -1])) for i in range(size)])

    def colocarReinas(self):
        self.tablero = np.zeros((self.size, self.size))

        for i in range(self.size):
            j = random.randint(0, self.size - 1) #columna random
            self.tablero[i][j] = 1

            if (self.tablero[i][j] == 1):
                self.reinas[i].set_posicion(np.array([i, j])) #ponemos posicion a la reina
    
    def get_size(self):
        return self.size

    def get_tablero(self):
        return self.tablero

    def get_reinas(self):
        return self.reinas

    def set_colisiones(self, colisiones):
        self.colisiones = colisiones

    def get_colisiones(self):
        return self.colisiones

    def get_combinacion(self):
        combinacion = ""
        for i in range(self.reinas.size):
            combinacion += str(self.reinas[i].get_posicion()[0]) + str(self.reinas[i].get_posicion()[1])
        return combinacion

    def get_combinaciones(self):
        return self.size ** self.size
    
    def evaluarColisiones(self):
            
        reinas = self.get_reinas()
        colisiones = 0

        for i in range(self.get_size()):
            for j in range(i + 1, self.get_size()):
                if self.__hayColision(reinas[i].get_posicion(), reinas[j].get_posicion()):
                    colisiones += 1
                    i += 1

        self.set_colisiones(colisiones)

    def __hayColision(self, pos1, pos2):
        
        if pos1[0] == pos2[0] or pos1[1] == pos2[1]: #columna o fila son iguales
            return True
        
        if abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]): #colision en diagonal \
            return True

        if abs(pos1[0] - pos2[0]) == abs(pos2[1] - pos1[1]): #colision en diagonal /
            return True
                
        return False