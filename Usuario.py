from Observador import Observador

class Usuario(Observador):
    def __init__(self, cedula, nombre, correo, contrasena, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.rol = rol
        self.notificaciones = []

    def verPerfil(self):
        print(f"\n=============== Perfil de {self.rol} ===============")
        print(f"Cédula          : {self.cedula}")
        print(f"Nombre          : {self.nombre}")
        print(f"Correo          : {self.correo}")

    def cambiarContrasena(self, usuario_dao):
        print("\n========== CAMBIAR CONTRASEÑA ==========")

        actual = input("Ingrese su contraseña actual: ").strip()

        if actual != self.__contrasena:
            print("\nLa contraseña actual no es correcta\n")
            return False

        nueva = input("Ingrese la nueva contraseña (mínimo 8 caracteres): ").strip()
        confirmar = input("Confirme la nueva contraseña: ").strip()

        if not nueva or not confirmar:
            print("\nDebe completar todos los campos\n")
            return False

        if nueva != confirmar:
            print("\nLas contraseñas no coinciden\n")
            return False

        if nueva == self.__contrasena:
            print("\nLa nueva contraseña no puede ser igual a la actual\n")
            return False

        if len(nueva) < 8:
            print("\nLa nueva contraseña debe tener al menos 8 caracteres\n")
            return False

        if usuario_dao.actualizarContrasena(self.cedula, nueva):
            self.__contrasena = nueva
            print("\nContraseña actualizada correctamente\n")
            return True
        else:
            print("\nNo se pudo actualizar la contraseña\n")
            return False

    # MÉTODOS DEL OBSERVER
    def actualizar(self, mensaje):
        self.notificaciones.append(mensaje)
        if not self.notificaciones:
            print("\nNo hay notificaciones\n")

        print("=" * 60)
        print("NOTIFICACIÓN RECIBIDA")
        print(f"Usuario: {self.nombre}")
        print(f"Rol    : {self.rol}")
        print(f"Mensaje: {mensaje}")
        print("=" * 60 + "\n")