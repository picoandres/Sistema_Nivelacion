import random
from ReceptorNotificacion import ReceptorNotificacion
class Usuario(ReceptorNotificacion):
    def __init__(self, cedula, nombre, correo, contrasena, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.rol = rol
        self.notificaciones = []

    @property
    def contrasena(self):
        return self.__contrasena

    def autenticar(self, correo, contrasena):
        if correo == self.correo and contrasena == self.contrasena:
            return True
        return False

    def cambiar_contrasena(self, nueva):
        self.__contrasena = nueva

    def recuperar_contrasena(self, **kwargs):
        codigo_random = random.randint(1000, 9999)

        print("Escoja un método para recuperar su contraseña")
        while True:
            opcion = input("Correo o teléfono: ").lower()

            if opcion in kwargs.values():
                print(f"Código: {codigo_random}")

                codigo = int(input("Ingrese el código que acaba de recibir: "))

                if codigo == codigo_random:
                    nueva = input("Escriba la nueva contraseña: ")
                    self.cambiar_contrasena(nueva)
                    print("Contraseña actualizada")
                    break
                else:
                    print("Código incorrecto")
            else:
                print("Escoja solo entre correo o número de teléfono")

    def ver_perfil(self):
        print(f"Perfil de {self.rol}")
        print(f"ID: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

    def editar_perfil(self, *args):
        print("Editar perfil")
        print("Nuevos datos:", args)
        print("Perfil actualizado exitosamente\n")

    def actualizar(self, mensaje):
        self.notificaciones.append(mensaje)
        print(40*"=")
        print("Usuario:", self.nombre)
        print("Rol:", self.rol)
        print(f"Notificación: {mensaje}")
        print(40*"=")

    def ver_notificaciones(self):
        if len(self.notificaiones) == 0:
            print("Sin notificaciones")
            return
        
        print("-----Historial-----")
        
        for n in self.notificaciones:
            print("-", n)
