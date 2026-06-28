#Subject del patron Observer
from abc import ABC

class gestorNotificaciones(ABC):
    def __init__(self):
        self._observadores = []

    def agregarObservador(self, observador):
        self._observadores.append(observador)

    def eliminarObservador(self, observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)