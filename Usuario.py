import random

class Usuario:
    def __init__(self, cedula, nombre, correo, contrasena):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.sesionActiva = False

    def iniciarSesion(self, contrasena):
        if contrasena == self.contrasena:
            self.sesionActiva = True
            return True
        return False

    def cerrarSesion(self):
        self.sesionActiva = False
        print(f"{self.nombre} ha salido del sistema")

    def verPerfil(self):
        print("Perfil de usuario")
        print(f"ID: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Contraseña: {self.contrasena}")

    def recuperarContrasena(self, **kwargs):
        codigo_random = random.randint(1000, 9999)
        print("Escoja un método para recuperar su contraseña")
        while True:
            opcion = input("Correo o teléfono: ").lower()

            if opcion in kwargs.values():
                print(f"Código: {codigo_random}")

                codigo = int(input("Ingrese el código que acaba de recibir: "))

                if codigo == codigo_random:
                    self.contrasena = input("Escriba la nueva contraseña: ")
                    print("Contraseña actualizada")
                    break
                else:
                    print("Código incorrecto")
            else:
                print("Escoja solo entre correo o número de teléfono")

    def editarPerfil(self, *args):
        print("Editar perfil")
        print("Nuevos datos:", args)
        print("Perfil actualizado exitosamente\n")