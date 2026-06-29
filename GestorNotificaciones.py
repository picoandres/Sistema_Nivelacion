#Subject del patron Observer
from abc import ABC

class GestorNotificaciones(ABC):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, usuario):
        if usuario not in self.observadores:
            self.observadores.append(usuario)

    def eliminar_observador(self, usuario):
        if usuario in self.observadores:
            self.observadores.remove(usuario)
    
    def notificar_Todos(self, mensaje):
        print("====NOTIFICACIONES====")
        for usuario in self.observadores:
            usuario.actualizar(mensaje)
