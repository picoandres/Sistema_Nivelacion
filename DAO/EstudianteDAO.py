from BaseDeDatos import ConexionSQLServer # DEBE MODIFICARSE #
from Modelos.Estudiante import Estudiante

class EstudianteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, estudiante: Estudiante):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            #insertar en Usuario (padre)
            sql_usuario ="""
            INSERT INTO Usuario
            (
                cedula,
                nombre,
                correo,
                contrasena,
                rol
            )

            VALUES (?, ?, ?, ?, ?)
            """
            self.db.cursor.execute(sql_usuario, (
                estudiante.cedula, estudiante.nombre, estudiante.correo,
                estudiante.contrasena, estudiante.rol
            ))
            #Insertar Estudiante (Hijo)
            sql_estudiante ="""
            INSERT INTO Alumnos
            (
                cedula,
                carrera,
                paralelo
            )
            VALUES (?, ?, ?)
            """
            self.db.cursor.execute(sql_estudiante, (
                estudiante.cedula, estudiante.carrera, estudiante.paralelo,
            ))
            conexion.commit()
            return True
        
        except Exception as e:
            conexion.rollback()
            print(f"Error al guardar estudiante en BD: {e}")
            return False
        
        finally:
            self.db.cerrarConexion()

    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []
        
        try:
            sql = """
            SELECT U.cedula,
               U.nombre,
               U.correo,
               A.carrera,
               A.paralelo
            FROM Usuario U
            INNER JOIN Alumnos A
            ON U.cedula = A.cedula
            """

            self.db.cursor.execute(sql)

            return self.db.cursor.fetchall()
        
        except Exception as e:
            print("Error: ", e)
            return []
        
        finally:
            self.db.cerrarConexion()

    
    def buscar(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                u.cedula,
                u.nombre,
                u.correo,
                u.contrasena,
                u.rol,
                a.carrera,
                a.paralelo
            FROM Usuario u
            INNER JOIN Alumnos a
                ON u.cedula = a.cedula
            WHERE u.cedula = ?
            """

            self.db.cursor.execute(sql, (cedula,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return Estudiante(
                fila.cedula,
                fila.nombre,
                fila.correo,
                fila.contrasena,
                fila.rol,
                fila.carrera,
                fila.paralelo
            )

        except Exception as e:
            print("Error al buscar estudiante:", e)
            return None

        finally:
            self.db.cerrarConexion()