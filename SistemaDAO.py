from DataBase import ConexionSQLServer
from Estudiante import Estudiante
from Docente import Docente

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
            conexion.rollbak()
            print(f"error al guardar estudiante en BD: {e}")
            return False
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
                docente._Usuario__contrasena, docente.rol
            ))
            #Insertar Docente (Hijo)
            sql_docente ="""
            INSERT INTO Docente
            (
                cedula,
                titulo,
                especialidad,
                paralelo
            )

            VALUES (?, ?, ?, ?)
            """
            self.db.cursor.execute(sql_docente, (
                docente.cedula, docente.titulo, docente.especialidad,
                None
            ))
            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()
            print(f"error al guardar estudiante en BD: {e}")
            return False
        finally:
            self.db.cerrarConexion()
