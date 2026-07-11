from abc import ABC, abstractmethod

class TiempoContrato(ABC):
    @abstractmethod
    def obtenerTipo(self):
        pass

class TiempoCompleto(TiempoContrato):
    def obtenerTipo(self):
        return "Tiempo Completo"

class TiempoParcial(TiempoContrato):
    def obtenerTipo(self):
        return "Tiempo Parcial"