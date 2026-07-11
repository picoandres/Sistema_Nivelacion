from BaseDeDatos import ConexionSQLServer # SE DEBE MODIFICAR #
from Modelos.HorarioCurso import HorarioCurso

class HorarioDAO:
    def __init__(self):
        self.db = ConexionSQLServer()


    def guardar(self, idCurso, horario: HorarioCurso):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            INSERT INTO Horario
            (
                idCurso,
                dia,
                horaInicio,
                horaFin,
                aula,
                asignador
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """

            self.db.cursor.execute(sql, (
                idCurso,
                horario.dia,
                horario.horaInicio,
                horario.horaFin,
                horario.aula,
                horario.asignador
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar horario:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def buscarPorCurso(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                dia,
                horaInicio,
                horaFin,
                aula,
                asignador
            FROM Horario
            WHERE idCurso = ?
            """

            self.db.cursor.execute(sql, (idCurso,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return HorarioCurso(
                fila.dia,
                str(fila.horaInicio),
                str(fila.horaFin),
                fila.aula,
                fila.asignador
            )

        except Exception as e:
            print("Error al buscar horario del curso:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def listarPorDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                c.idCurso,
                c.nombreCurso,
                c.modalidad,
                c.jornada,
                u.nombre AS nombreDocente,
                h.dia,
                h.horaInicio,
                h.horaFin,
                h.aula,
                h.asignador
            FROM Curso c
            INNER JOIN Horario h
                ON c.idCurso = h.idCurso
            LEFT JOIN Usuario u
                ON c.cedulaDocente = u.cedula
            WHERE c.cedulaDocente = ?
            ORDER BY c.nombreCurso
            """

            self.db.cursor.execute(sql, (cedulaDocente,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar cronograma del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def listarPorEstudiante(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                c.idCurso,
                c.nombreCurso,
                c.modalidad,
                c.jornada,
                u.nombre AS nombreDocente,
                h.dia,
                h.horaInicio,
                h.horaFin,
                h.aula,
                h.asignador
            FROM AsignacionCurso ac
            INNER JOIN Curso c
                ON ac.idCurso = c.idCurso
            INNER JOIN Horario h
                ON c.idCurso = h.idCurso
            LEFT JOIN Usuario u
                ON c.cedulaDocente = u.cedula
            WHERE ac.cedulaEstudiante = ?
            ORDER BY c.nombreCurso
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar cronograma del estudiante:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def listarTodos(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                c.idCurso,
                c.nombreCurso,
                c.modalidad,
                c.jornada,
                u.nombre AS nombreDocente,
                h.dia,
                h.horaInicio,
                h.horaFin,
                h.aula,
                h.asignador
            FROM Curso c
            INNER JOIN Horario h
                ON c.idCurso = h.idCurso
            LEFT JOIN Usuario u
                ON c.cedulaDocente = u.cedula
            ORDER BY c.nombreCurso
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar cronograma:", e)
            return []

        finally:
            self.db.cerrarConexion()