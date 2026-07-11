from BaseDeDatos import ConexionSQLServer # YA ESTÁ LISTA, QUIZÁ SE LE PUEDAN METER VALIDACIONES O ALGÚN MÉTODO DE SER NECESARIO
from Modelos.Matricula import Matricula
from Modelos.Estudiante import Estudiante
from Modelos.Paralelo import Paralelo

class MatriculaDAO:

    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, matricula: Matricula):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            cedula = matricula.cedulaEstudiante.strip()
            idParalelo = matricula.idParalelo.strip()

            if not cedula or not idParalelo:
                print("Todos los campos son obligatorios")
                return False

            # Verificar estudiante
            sql = """
            SELECT 1
            FROM Estudiante
            WHERE cedula = ?
            """

            self.db.cursor.execute(sql, (cedula,))
            if self.db.cursor.fetchone() is None:
                print("El estudiante no existe")
                return False

            # Verificar paralelo

            sql = """
            SELECT cupoMaximo
            FROM Paralelo
            WHERE idParalelo = ?
            """

            self.db.cursor.execute(sql, (idParalelo,))
            paralelo = self.db.cursor.fetchone()

            if paralelo is None:
                print("El paralelo no existe")
                return False

            # Un estudiante sólo puede pertenecer a un paralelo

            sql = """
            SELECT 1
            FROM Matricula
            WHERE cedulaEstudiante = ?
            """

            self.db.cursor.execute(sql, (cedula,))
            if self.db.cursor.fetchone():
                print("El estudiante ya está matriculado")
                return False

            # Verificar cupo

            sql = """
            SELECT COUNT(*)
            FROM Matricula
            WHERE idParalelo = ?
            """

            self.db.cursor.execute(sql, (idParalelo,))
            inscritos = self.db.cursor.fetchone()[0]

            if inscritos >= paralelo.cupoMaximo:
                print("El paralelo ya alcanzó su cupo máximo")
                return False

            sql = """
            INSERT INTO Matricula
            (
                cedulaEstudiante,
                idParalelo
            )
            VALUES (?, ?)
            """

            self.db.cursor.execute(sql, (
                cedula,
                idParalelo
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar matrícula:", e)
            return False

        finally:
            self.db.cerrarConexion()

    
    def buscar(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:

            sql = """
            SELECT
                cedulaEstudiante,
                idParalelo,
                fechaAsignacion
            FROM Matricula
            WHERE cedulaEstudiante = ?
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return Matricula(
                fila.cedulaEstudiante,
                fila.idParalelo,
                fila.fechaAsignacion
            )

        except Exception as e:
            print("Error al buscar matrícula:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def existe(self, cedulaEstudiante, idParalelo):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:

            sql = """
            SELECT 1
            FROM Matricula
            WHERE cedulaEstudiante = ?
            AND idParalelo = ?
            """

            self.db.cursor.execute(sql, (
                cedulaEstudiante,
                idParalelo
            ))

            return self.db.cursor.fetchone() is not None

        except Exception as e:
            print("Error al verificar matrícula:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def eliminar(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:

            sql = """
            DELETE
            FROM Matricula
            WHERE cedulaEstudiante = ?
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))

            if self.db.cursor.rowcount == 0:
                print("La matrícula no existe")
                return False

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al eliminar matrícula:", e)
            return False

        finally:
            self.db.cerrarConexion()

    
    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT
                m.cedulaEstudiante,
                m.idParalelo,
                m.fechaAsignacion,
                u.nombre AS nombreEstudiante,
                c.nombreCurso,
                p.paralelo
            FROM Matricula m
            INNER JOIN Estudiante e
                ON m.cedulaEstudiante = e.cedula
            INNER JOIN Usuario u
                ON e.cedula = u.cedula
            INNER JOIN Paralelo p
                ON m.idParalelo = p.idParalelo
            INNER JOIN Curso c
                ON p.idCurso = c.idCurso
            ORDER BY c.nombreCurso, p.paralelo, u.nombre
            """

            self.db.cursor.execute(sql)

            matriculas = []

            for fila in self.db.cursor.fetchall():

                matricula = Matricula(
                    fila.cedulaEstudiante,
                    fila.idParalelo,
                    fila.fechaAsignacion,
                    fila.nombreEstudiante,
                    fila.nombreCurso,
                    fila.paralelo
                )

                matriculas.append(matricula)

            return matriculas

        except Exception as e:
            print("Error al listar matrículas:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarParaleloPorEstudiante(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:

            sql = """
            SELECT
                p.idParalelo,
                p.idCurso,
                p.paralelo,
                p.jornada,
                p.cupoMaximo,
                p.estado,
                c.nombreCurso
            FROM Matricula m
            INNER JOIN Paralelo p
                ON m.idParalelo = p.idParalelo
            INNER JOIN Curso c
                ON p.idCurso = c.idCurso
            WHERE m.cedulaEstudiante = ?
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            paralelo = Paralelo(
                fila.idParalelo,
                fila.idCurso,
                fila.paralelo,
                fila.jornada,
                fila.cupoMaximo,
                fila.estado
            )

            paralelo.nombreCurso = fila.nombreCurso

            return paralelo

        except Exception as e:
            print("Error al buscar paralelo del estudiante:", e)
            return None

        finally:
            self.db.cerrarConexion()

    
    def buscarEstudiantesPorParalelo(self, idParalelo):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT
                e.cedula,
                u.nombre,
                u.correo,
                u.contrasena,
                u.rol,
                e.carrera
            FROM Matricula m
            INNER JOIN Estudiante e
                ON m.cedulaEstudiante = e.cedula
            INNER JOIN Usuario u
                ON e.cedula = u.cedula
            WHERE m.idParalelo = ?
            ORDER BY u.nombre
            """

            self.db.cursor.execute(sql, (idParalelo,))

            estudiantes = []

            for fila in self.db.cursor.fetchall():

                estudiante = Estudiante(
                    fila.cedula,
                    fila.nombre,
                    fila.correo,
                    fila.contrasena,
                    fila.rol,
                    fila.carrera
                )

                estudiantes.append(estudiante)

            return estudiantes

        except Exception as e:
            print("Error al buscar estudiantes del paralelo:", e)
            return []

        finally:
            self.db.cerrarConexion()