from datetime import datetime
from BaseDeDatos import ConexionSQLServer

class EvaluacionDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, idCurso, idMateria, titulo, descripcion, fecha, ponderacion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            idCurso = str(idCurso).strip()
            idMateria = str(idMateria).strip()
            titulo = str(titulo).strip()
            descripcion = str(descripcion).strip()
            fecha = str(fecha).strip()

            if not idCurso or not idMateria or not titulo or not descripcion or not fecha:
                print("Todos los campos son obligatorios")
                return False

            if len(titulo) > 100:
                print("El título no puede exceder los 100 caracteres")
                return False

            if ponderacion <= 0 or ponderacion > 100:
                print("La ponderación debe estar entre 1 y 100")
                return False

            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                print("La fecha debe tener el formato AAAA-MM-DD")
                return False

            sql_curso = """
            SELECT 1
            FROM Curso
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_curso, (idCurso,))
            curso = self.db.cursor.fetchone()

            if curso is None:
                print("No existe un curso con ese ID")
                return False

            sql_materia = """
            SELECT 1
            FROM Materia
            WHERE idMateria = ?
            """
            self.db.cursor.execute(sql_materia, (idMateria,))
            if self.db.cursor.fetchone() is None:
                print("No existe una materia con ese ID")
                return False

            sql_curso_materia = """
            SELECT 1
            FROM CursoMateria
            WHERE idCurso = ? AND idMateria = ?
            """
            self.db.cursor.execute(sql_curso_materia, (idCurso, idMateria))
            if self.db.cursor.fetchone() is None:
                print("Esa materia no está asignada a ese curso")
                return False

            cedula_docente = curso.cedulaDocente

            if cedula_docente is None:
                print("El curso no tiene un docente asignado")
                return False
            
            sql_docente = """
            SELECT idMateria
            FROM Docente
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_docente, (cedula_docente,))
            docente = self.db.cursor.fetchone()

            if docente is None:
                print("El docente asignado al curso no existe")
                return False

            if docente.idMateria != idMateria:
                print("Materia de evaluación distinta a la asignada al docente del curso")
                return False
            
            sql_total = """
            SELECT ISNULL(SUM(ponderacion), 0) AS totalPonderacion
            FROM Evaluacion
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_total, (idCurso,))
            resultado = self.db.cursor.fetchone()
            total_actual = int(resultado.totalPonderacion) if resultado else 0

            if total_actual + ponderacion > 100:
                disponible = 100 - total_actual
                print("No se puede registrar la evaluación")
                print(f"El curso ya tiene {total_actual}% asignado")
                print(f"Solo queda {disponible}% disponible")
                return False

            sql = """
            INSERT INTO Evaluacion
                (
                    idCurso,
                    idMateria,
                    titulo,
                    descripcion,
                    fecha,
                    ponderacion
                )
            VALUES (?, ?, ?, ?, ?, ?)
            """

            self.db.cursor.execute(sql, (idCurso, idMateria, titulo, descripcion, fecha, ponderacion))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar evaluación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def listarPorCurso(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                e.idEvaluacion,
                e.idCurso,
                e.idMateria,
                m.nombre AS nombreMateria,
                e.titulo,
                e.descripcion,
                e.fecha,
                e.ponderacion
            FROM Evaluacion e
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE e.idCurso = ?
            ORDER BY e.fecha, e.titulo
            """

            self.db.cursor.execute(sql, (idCurso,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar evaluaciones del curso:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def listarPorDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                e.idEvaluacion,
                e.idCurso,
                c.nombreCurso,
                e.idMateria,
                m.nombre AS nombreMateria,
                e.titulo,
                e.descripcion,
                e.fecha,
                e.ponderacion
            FROM Evaluacion e
            INNER JOIN Curso c
                ON e.idCurso = c.idCurso
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.cedulaDocente = ?
            ORDER BY c.nombreCurso, m.nombre, e.fecha
            """

            self.db.cursor.execute(sql, (cedulaDocente,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar evaluaciones del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def listarPorCursoYDocente(self, idCurso, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                e.idEvaluacion,
                e.idCurso,
                c.nombreCurso,
                e.idMateria,
                m.nombre AS nombreMateria,
                e.titulo,
                e.descripcion,
                e.fecha,
                e.ponderacion
            FROM Evaluacion e
            INNER JOIN Curso c
                ON e.idCurso = c.idCurso
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE e.idCurso = ?
            AND c.cedulaDocente = ?
            ORDER BY m.nombre, e.fecha, e.idEvaluacion
            """

            self.db.cursor.execute(sql, (idCurso, cedulaDocente))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar evaluaciones del curso del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorId(self, idEvaluacion):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                e.idEvaluacion,
                e.idCurso,
                c.nombreCurso,
                e.idMateria,
                m.nombre AS nombreMateria,
                e.titulo,
                e.descripcion,
                e.fecha,
                e.ponderacion
            FROM Evaluacion e
            INNER JOIN Curso c
                ON e.idCurso = c.idCurso
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE e.idEvaluacion = ?
            """

            self.db.cursor.execute(sql, (idEvaluacion,))
            return self.db.cursor.fetchone()

        except Exception as e:
            print("Error al buscar evaluación:", e)
            return None

        finally:
            self.db.cerrarConexion()

    
    def editar(self, idEvaluacion, titulo, descripcion, fecha, ponderacion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            titulo = titulo.strip()
            fecha = fecha.strip()

            if not titulo or not fecha:
                print("El título y la fecha son obligatorios")
                return False

            if len(titulo) > 100:
                print("El título no puede exceder los 100 caracteres")
                return False

            if ponderacion <= 0 or ponderacion > 100:
                print("La ponderación debe estar entre 1 y 100")
                return False

            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                print("La fecha debe tener el formato AAAA-MM-DD")
                return False

            if descripcion is not None and descripcion.strip() == "":
                descripcion = None

            sql_actual = """
            SELECT idCurso, ponderacion
            FROM Evaluacion
            WHERE idEvaluacion = ?
            """

            self.db.cursor.execute(sql_actual, (idEvaluacion,))
            evaluacion_actual = self.db.cursor.fetchone()

            if evaluacion_actual is None:
                print("No existe una evaluación con ese ID")
                return False

            idCurso = evaluacion_actual.idCurso
            ponderacion_actual = evaluacion_actual.ponderacion

            sql_total = """
            SELECT ISNULL(SUM(ponderacion), 0) AS totalPonderacion
            FROM Evaluacion
            WHERE idCurso = ?
            """

            self.db.cursor.execute(sql_total, (idCurso,))
            resultado = self.db.cursor.fetchone()
            total_actual = int(resultado.totalPonderacion) if resultado else 0

            nuevo_total = total_actual - ponderacion_actual + ponderacion

            if nuevo_total > 100:
                disponible = 100 - (total_actual - ponderacion_actual)
                print("\nNo se puede editar la evaluación")
                print(f"El curso ya tiene {total_actual}% asignado en total")
                print(f"Sin contar esta evaluación, solo quedan {disponible}% disponibles\n")
                return False

            sql = """
            UPDATE Evaluacion
            SET titulo = ?,
                descripcion = ?,
                fecha = ?,
                ponderacion = ?
            WHERE idEvaluacion = ?
            """

            self.db.cursor.execute(sql, (titulo, descripcion, fecha, ponderacion, idEvaluacion))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al editar evaluación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def eliminar(self, idEvaluacion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql_existe = """
            SELECT 1
            FROM Evaluacion
            WHERE idEvaluacion = ?
            """
            self.db.cursor.execute(sql_existe, (idEvaluacion,))
            if self.db.cursor.fetchone() is None:
                print("No existe una evaluación con ese ID")
                return False

            sql_verificar = """
            SELECT 1
            FROM Calificacion
            WHERE idEvaluacion = ?
            """
            self.db.cursor.execute(sql_verificar, (idEvaluacion,))
            if self.db.cursor.fetchone() is not None:
                print("No se puede eliminar la evaluación porque tiene calificaciones registradas")
                return False

            sql = """
            DELETE FROM Evaluacion
            WHERE idEvaluacion = ?
            """
            self.db.cursor.execute(sql, (idEvaluacion,))
            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al eliminar evaluación:", e)
            return False

        finally:
            self.db.cerrarConexion()