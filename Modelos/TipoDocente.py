from abc import ABC, abstractmethod

class TipoDocente(ABC):
    @abstractmethod
    def obtenerTipo(self):
        pass

class Titular(TipoDocente):
    def obtenerTipo(self):
        return "Titular"
    
class Suplente(TipoDocente):
    def obtenerTipo(self):
        return "Suplente"
