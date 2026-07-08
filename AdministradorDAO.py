from BaseDeDatos import ConexionSQLServer
from Administrador import Administrador

class AdministradorDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
    

    def buscarPorCedula(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            sql = """
            SELECT
                U.cedula,
                U.nombre,
                U.correo,
                U.contrasena,
                U.rol,
                A.id_admin,
                A.sede,
                A.telefono
            FROM Usuario U
            INNER JOIN Administrador A
                ON U.cedula = A.cedula
            WHERE U.cedula = ?
            """

            self.db.cursor.execute(sql, (cedula,))

            datos = self.db.cursor.fetchone()
            if datos is None:
                return None

            return Administrador(
                datos.cedula,
                datos.nombre,
                datos.correo,
                datos.contrasena,
                datos.rol,
                datos.id_admin,
                datos.sede,
                datos.telefono
            )

        except Exception as e:
            print("Error:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                U.cedula,
                U.nombre,
                U.correo,
                A.id_admin,
                A.sede,
                A.telefono
            FROM Usuario U
            INNER JOIN Administrador A
                ON U.cedula = A.cedula
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error:", e)
            return []

        finally:
            self.db.cerrarConexion()