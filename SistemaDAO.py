from DataBase import ConexionSQLServer
from Estudiante import Estudiante
from Docente import Docente
from Administrador import Administrador

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
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
                SELECT titulo, especialidad
                FROM Docente
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                return Docente(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.titulo,
                    datos.especialidad,
                )

            # ===== ADMINISTRADOR =====
            elif rol == "Administrador":

                sql = """
                SELECT id_admin, sede, telefono
                FROM Administrador
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

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
            print("Error: ", e)
            return None

        finally:
            self.db.cerrarConexion()        


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


class DocenteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
        
    def guardar(self, docente: Docente):
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
                docente.cedula, docente.nombre, docente.correo,
                docente.contrasena, docente.rol
            ))
            #Insertar Docente (Hijo)
            sql_docente ="""
            INSERT INTO Docente
            (
                cedula,
                titulo,
                especialidad
            )

            VALUES (?, ?, ?)
            """
            self.db.cursor.execute(sql_docente, (
                docente.cedula, docente.titulo, docente.especialidad
            ))
            conexion.commit()
            return True
        
        except Exception as e:
            conexion.rollback()
            print(f"Error al guardar docente en BD: {e}")
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
               D.titulo,
               D.especialidad
            FROM Usuario U
            INNER JOIN Docente D
            ON U.cedula = D.cedula
            """

            self.db.cursor.execute(sql)

            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error: ", e)
            return []

        finally:
            self.db.cerrarConexion()