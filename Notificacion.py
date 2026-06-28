from GestorNotificaciones import gestorNotificaciones
class Notificacion(gestorNotificaciones):
    def __init__(self):
        super().__init__()

    def enviar(self, mensaje):
        print("enviando notificaciones...")
        self.notificar(mensaje)
