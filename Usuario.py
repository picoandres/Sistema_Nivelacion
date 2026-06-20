import random

class Usuario:
    def __init__(self, cedula, nombre, correo, contrasena, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.rol = rol

    def iniciar_sesion(self, contrasena):
        pass

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

    def cerrar_sesion(self):
        self.sesionActiva = False
        print(f"{self.nombre} ha salido del sistema")

    def ver_perfil(self):
        print(f"Perfil de {self.rol}")
        print(f"ID: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

    def editar_perfil(self, *args):
        print("Editar perfil")
        print("Nuevos datos:", args)
        print("Perfil actualizado exitosamente\n")