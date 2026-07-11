#Subject del patron Observer
class GestorNotificaciones():
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
    
    def notificar_todos(self, mensaje, tipo="general"):
        if tipo == "general":
            mensaje_final = f"[NOTIFICACIÓN] {mensaje}"
        elif tipo == "calificacion":
            mensaje_final = f"[CALIFICACIÓN] {mensaje}"
        elif tipo == "evaluacion":
            mensaje_final = f"[EVALUACIÓN] {mensaje}"
        else:
            mensaje_final = mensaje

        for observador in self.observadores:
            observador.actualizar(mensaje_final)