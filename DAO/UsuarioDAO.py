from BaseDeDatos import ConexionSQLServer # QUIZÁ SEA NECESARIO CAMBIARLA, AUNQUE ES POCO PROBABLE #
from Modelos.Administrador import Administrador
from Modelos.Estudiante import Estudiante
from Modelos.Docente import Docente, Titular, Suplente, TiempoCompleto, TiempoParcial


class UsuarioDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def crearTipoDocente(self, valor):
        if valor == "Suplente":
            return Suplente()
        return Titular()

    def crearTiempoContrato(self, valor):
        if valor == "Tiempo Parcial":
            return TiempoParcial()
        return TiempoCompleto()


    def buscarUsuario(self, correo, contrasena):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            sql = """
            SELECT *
            FROM Usuario
            WHERE correo = ? AND contrasena = ?
            """

            self.db.cursor.execute(sql, (correo, contrasena))
            usuario = self.db.cursor.fetchone()
        
            if usuario is None:
                return None

            cedula = usuario.cedula
            nombre = usuario.nombre
            correo = usuario.correo
            contrasena = usuario.contrasena
            rol = usuario.rol

            if rol == "Estudiante":

                sql = """
                SELECT carrera, paralelo
                FROM Alumnos
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                return Estudiante(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.carrera,
                    datos.paralelo
                )

            elif rol == "Docente":

                sql = """
                SELECT
                    profesion,
                    especialidad,
                    tipoDocente,
                    tiempoContrato,
                FROM Docente
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                if datos is None:
                    return None
                
                tipo_docente = self.crearTipoDocente(datos.tipoDocente)
                tiempo_contrato = self.crearTiempoContrato(datos.tiempoContrato)

                return Docente(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.profesion,
                    datos.especialidad,
                    tipo_docente,
                    tiempo_contrato,
                )

            elif rol == "Administrador":

                sql = """
                SELECT id_admin, sede, telefono
                FROM Administrador
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                if datos is None:
                    return None

                return Administrador(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.id_admin,
                    datos.sede,
                    datos.telefono
                )
            return None

        except Exception as e:
            print("Error al buscar usuario: ", e)
            return None

        finally:
            self.db.cerrarConexion()

    
    def actualizarContrasena(self, cedula, nueva_contrasena):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            UPDATE Usuario
            SET contrasena = ?
            WHERE cedula = ?
            """

            self.db.cursor.execute(sql, (nueva_contrasena, cedula))
            conexion.commit()
            return self.db.cursor.rowcount > 0

        except Exception as e:
            conexion.rollback()
            print("Error al actualizar contraseña:", e)
            return False

        finally:
            self.db.cerrarConexion()