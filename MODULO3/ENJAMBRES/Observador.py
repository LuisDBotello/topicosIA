from abc import ABC, abstractmethod

class Observador(ABC):
    
    @abstractmethod
    def actualizar(self, particula):
        pass