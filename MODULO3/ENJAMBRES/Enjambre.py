import random

from Particula import Particula
from Observador import Observador

class Enjambre(Observador):
    
    limX, limY = 0.0, 0.0
    bestgV, bestgX, bestgY = 0, 0, 0
    w, c1, c2 = 0.0, 0.0, 0.0
    
    def __init__(self, nParticulas, funcion_objetivo, c1, c2, w,  limX, limY ):
        self.particulas = []
        self.limX = limX
        self.limY = limY
        self.funcion_objetivo = funcion_objetivo
        self.bestgV = float("-inf")
        self.bestgX = None
        self.bestgY = None
        self.c1 = c1
        self.c2 = c2
        self.w = w
        
        for i in range(nParticulas):
            particula = Particula(i)
            particula.agregar_observador(self)
            
            self.particulas.append(particula)
            self.actualizar(particula)

    def actualizar(self, particula):
        self.particulas[particula.id] = particula
    
    def dispersar(self):
        self.bestgV = float("-inf")
        self.bestgX = None
        self.bestgY = None

        for particula in self.particulas:
            particula.x = random.uniform(-self.limX, self.limX)
            particula.y = random.uniform(-self.limY, self.limY)

            particula.vx = random.uniform(-1, 1)
            particula.vy = random.uniform(-1, 1)

            particula.best = float("-inf")
            particula.bestx = None
            particula.besty = None

            particula.notify()
            
    def agregarParticula(self, particula):
        self.particulas.append(particula)
        
    def iterar(self):
        for particula in self.particulas:
            self.__evaluar(particula)

        for particula in self.particulas:
            self.__actualizarVelocidades(particula)

        for particula in self.particulas:
            self.__actualizarPosiciones(particula)
#privados
        
    def __evaluar(self, particula):
        particula.valor = self.funcion_objetivo(
            particula.x,
            particula.y
        )
        
        if(self.bestgV < particula.valor):
            self.bestgV, self.bestgX, self.bestgY = particula.valor, particula.x, particula.y 

        if(particula.best < particula.valor): #máximo por particula
            particula.best, particula.bestx, particula.besty = particula.valor, particula.x, particula.y
            
            
    def __actualizarVelocidades(self, particula):
        r1 = random.random()
        r2 = random.random()
        particula.vx = self.w * particula.vx + self.c1 * r1 * (particula.bestx - particula.x) + self.c2 * r2 * (self.bestgX - particula.x)
        particula.vy = self.w * particula.vy + self.c1 * r1 * (particula.besty - particula.y) + self.c2 * r2 * (self.bestgY - particula.y)

    def __actualizarPosiciones(self, particula):
        nuevo_x = particula.x + particula.vx
        nuevo_y = particula.y + particula.vy

        nuevo_x = max(-self.limX, min(self.limX, nuevo_x))
        nuevo_y = max(-self.limY, min(self.limY, nuevo_y))

        particula.mover(nuevo_x, nuevo_y)
                

    def __str__(self):
        return "\n".join(str(particula.id) for particula in self.particulas)

    def __ponerRandom(self, particula, limX, limY):
        particula.x = random.uniform(-limX, limX)
        particula.y = random.uniform(-limY, limY)
        particula.notify()
