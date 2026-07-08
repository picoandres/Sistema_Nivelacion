from BaseDeDatos import ConexionSQLServer
from Estudiante import Estudiante

class AsignacionCursoDAO:
    def __init__(self):
        self.db = ConexionSQLServer()


    def guardar(self, cedula, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            if not cedula or not idCurso:
                print("La cédula del estudiante y el ID del curso son obligatorios")
                return False

            sql_verificar = """
            SELECT idCurso
            FROM AsignacionCurso
            WHERE cedulaEstudiante = ?
            """
            self.db.cursor.execute(sql_verificar, (cedula,))
            asignacion = self.db.cursor.fetchone()

            if asignacion is not None:
                print("El estudiante ya pertenece a un curso de nivelación")
                return False

            sql_estudiante = """
            SELECT 1
            FROM Alumnos
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_estudiante, (cedula,))
            if self.db.cursor.fetchone() is None:
                print("No existe un estudiante con esa cédula")
                return False

            sql_curso = """
            SELECT 1
            FROM Curso
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_curso, (idCurso,))
            if self.db.cursor.fetchone() is None:
                print("No existe un curso con ese ID")
                return False

            sql_existe = """
            SELECT 1
            FROM AsignacionCurso
            WHERE cedulaEstudiante = ? AND idCurso = ?
            """
            self.db.cursor.execute(sql_existe, (cedula, idCurso))
            if self.db.cursor.fetchone() is not None:
                print("El estudiante ya está asignado a este curso")
                return False

            sql = """
            INSERT INTO AsignacionCurso
            (
                cedulaEstudiante,
                idCurso
            )
            VALUES (?, ?)
            """

            self.db.cursor.execute(sql, (cedula, idCurso))
            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al asignar estudiante a curso:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def existe(self, cedula, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            sql = """
            SELECT 1
            FROM AsignacionCurso
            WHERE cedulaEstudiante = ?
              AND idCurso = ?
            """

            self.db.cursor.execute(sql, (cedula, idCurso))
            return self.db.cursor.fetchone() is not None

        except Exception as e:
            print("Error al verificar asignación estudiante-curso:", e)
            return False
        
        finally:
            self.db.cerrarConexion()


    def buscarPorEstudiante(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                C.idCurso,
                C.nombreCurso,
                C.modalidad,
                C.jornada,
                D.nombre AS docente
            FROM AsignacionCurso AC
            INNER JOIN Curso C
                ON AC.idCurso = C.idCurso
            LEFT JOIN Docente Doc
                ON C.cedulaDocente = Doc.cedula
            LEFT JOIN Usuario D
                ON Doc.cedula = D.cedula
            WHERE AC.cedulaEstudiante = ?
            ORDER BY C.nombreCurso
            """

            self.db.cursor.execute(sql, (cedula,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al buscar cursos del estudiante:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarEstudiantesPorCursoYDocente(self, idCurso, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                U.cedula,
                U.nombre,
                U.correo,
                A.carrera,
                A.paralelo
            FROM AsignacionCurso AC
            INNER JOIN Curso C
                ON AC.idCurso = C.idCurso
            INNER JOIN Usuario U
                ON AC.cedulaEstudiante = U.cedula
            INNER JOIN Alumnos A
                ON U.cedula = A.cedula
            WHERE C.idCurso = ?
              AND C.cedulaDocente = ?
            ORDER BY U.nombre
            """

            self.db.cursor.execute(sql, (idCurso, cedulaDocente))
            filas = self.db.cursor.fetchall()

            estudiantes = []
            for fila in filas:
                estudiante = Estudiante(
                    fila.cedula,
                    fila.nombre,
                    fila.correo,
                    "",
                    "Estudiante",
                    fila.carrera,
                    fila.paralelo
                )
                estudiantes.append(estudiante)
            
            return estudiantes
        
        except Exception as e:
            print("Error al buscar estudiantes del curso:", e)
            return []

        finally:
            self.db.cerrarConexion()