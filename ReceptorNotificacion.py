#Patron de comportamiento Observer
from abc import ABC, abstractmethod

class ReceptorNotificacion(ABC):

    @abstractmethod
    def actualizar(self, mensaje):
        pass
