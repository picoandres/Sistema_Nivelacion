#Patron de comportamiento Observer
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass