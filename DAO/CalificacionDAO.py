from BaseDeDatos import ConexionSQLServer # PENDIENTE DE MODIFICAR

class CalificacionDAO:
    def __init__(self):
        self.db = ConexionSQLServer()


    def guardar(self, cedulaEstudiante, idCurso, idEvaluacion, nota, descripcion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10")
                return False

            if descripcion is not None:
                descripcion = descripcion.strip()
                if descripcion == "":
                    descripcion = None

            
            sql_estudiante = """
            SELECT 1
            FROM AsignacionCurso
            WHERE cedulaEstudiante = ? AND idCurso = ?
            """
            self.db.cursor.execute(sql_estudiante, (cedulaEstudiante, idCurso))
            if self.db.cursor.fetchone() is None:
                print("El estudiante no está asignado a ese curso")
                return False

            sql_evaluacion = """
            SELECT 1
            FROM Evaluacion
            WHERE idEvaluacion = ? AND idCurso = ?
            """
            self.db.cursor.execute(sql_evaluacion, (idEvaluacion, idCurso))
            if self.db.cursor.fetchone() is None:
                print("La evaluación no pertenece a ese curso")
                return False

            sql_duplicado = """
            SELECT 1
            FROM Calificacion
            WHERE cedulaEstudiante = ? AND idEvaluacion = ?
            """
            self.db.cursor.execute(sql_duplicado, (cedulaEstudiante, idEvaluacion))
            if self.db.cursor.fetchone() is not None:
                print("\nEse estudiante ya tiene una calificación registrada en esa evaluación")
                return False

            sql = """
            INSERT INTO Calificacion
            (
                cedulaEstudiante,
                idCurso,
                idEvaluacion,
                nota,
                descripcion
            )
            VALUES (?, ?, ?, ?, ?)
            """

            self.db.cursor.execute(sql, (
                cedulaEstudiante,
                idCurso,
                idEvaluacion,
                nota,
                descripcion
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar calificación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def listarPorEstudiante(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                c.idCalificacion,
                c.idCurso,
                cu.nombreCurso,
                c.idEvaluacion,
                e.titulo,
                e.idMateria,
                m.nombre AS nombreMateria,
                c.nota,
                c.descripcion
            FROM Calificacion c
            INNER JOIN Curso cu
                ON c.idCurso = cu.idCurso
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.cedulaEstudiante = ?
            ORDER BY c.idCurso, e.idEvaluacion
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar calificaciones del estudiante:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorCurso(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                c.idCalificacion,
                c.cedulaEstudiante,
                u.nombre AS nombreEstudiante,
                c.idCurso,
                c.idEvaluacion,
                e.titulo AS tituloEvaluacion,
                m.nombre AS nombreMateria,
                c.nota,
                c.descripcion
            FROM Calificacion c
            INNER JOIN Usuario u
                ON c.cedulaEstudiante = u.cedula
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.idCurso = ?
            ORDER BY u.nombre, e.titulo
            """

            self.db.cursor.execute(sql, (idCurso,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al buscar calificaciones del curso:", e)
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
                c.idCalificacion,
                c.cedulaEstudiante,
                u.nombre AS nombreEstudiante,
                c.idCurso,
                cu.nombreCurso,
                c.idEvaluacion,
                e.titulo AS tituloEvaluacion,
                e.idMateria,
                m.nombre AS nombreMateria,
                c.nota,
                c.descripcion
            FROM Calificacion c
            INNER JOIN Usuario u
                ON c.cedulaEstudiante = u.cedula
            INNER JOIN Curso cu
                ON c.idCurso = cu.idCurso
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.idCurso = ? AND cu.cedulaDocente = ?
            ORDER BY u.nombre, e.titulo
            """

            self.db.cursor.execute(sql, (idCurso, cedulaDocente))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar calificaciones del curso:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorId(self, idCalificacion):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                c.idCalificacion,
                c.cedulaEstudiante,
                u.nombre AS nombreEstudiante,
                c.idCurso,
                cu.nombreCurso,
                c.idEvaluacion,
                e.titulo AS tituloEvaluacion,
                e.idMateria,
                m.nombre AS nombreMateria,
                c.nota,
                c.descripcion
            FROM Calificacion c
            INNER JOIN Usuario u
                ON c.cedulaEstudiante = u.cedula
            INNER JOIN Curso cu
                ON c.idCurso = cu.idCurso
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.idCalificacion = ?
            """

            self.db.cursor.execute(sql, (idCalificacion,))
            return self.db.cursor.fetchone()

        except Exception as e:
            print("Error al buscar calificación:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def buscarPorIdYDocente(self, idCalificacion, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                c.idCalificacion,
                c.cedulaEstudiante,
                u.nombre AS nombreEstudiante,
                c.idCurso,
                cu.nombreCurso,
                c.idEvaluacion,
                e.titulo AS tituloEvaluacion,
                e.idMateria,
                m.nombre AS nombreMateria,
                c.nota,
                c.descripcion
            FROM Calificacion c
            INNER JOIN Usuario u
                ON c.cedulaEstudiante = u.cedula
            INNER JOIN Curso cu
                ON c.idCurso = cu.idCurso
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            INNER JOIN Materia m
                ON e.idMateria = m.idMateria
            WHERE c.idCalificacion = ? AND cu.cedulaDocente = ?
            """

            self.db.cursor.execute(sql, (idCalificacion, cedulaDocente))
            return self.db.cursor.fetchone()

        except Exception as e:
            print("Error al buscar calificación del docente:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def buscarEstudianteDeCalificacion(self, idCalificacion):
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
            FROM Calificacion c
            INNER JOIN Usuario u
                ON c.cedulaEstudiante = u.cedula
            INNER JOIN Alumnos a
                ON u.cedula = a.cedula
            WHERE c.idCalificacion = ?
            """

            self.db.cursor.execute(sql, (idCalificacion,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            from Modelos.Estudiante import Estudiante
            estudiante = Estudiante(
                fila.cedula,
                fila.nombre,
                fila.correo,
                fila.contrasena,
                "Estudiante",
                fila.carrera,
                fila.paralelo
            )

            return estudiante

        except Exception as e:
            print("Error al buscar estudiante de la calificación:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def editar(self, idCalificacion, nota, descripcion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10")
                return False

            if descripcion is not None:
                descripcion = descripcion.strip()
                if descripcion == "":
                    descripcion = None

            sql_buscar = """
            SELECT 1
            FROM Calificacion
            WHERE idCalificacion = ?
            """
            self.db.cursor.execute(sql_buscar, (idCalificacion,))
            if self.db.cursor.fetchone() is None:
                print("No existe una calificación con ese ID")
                return False

            sql = """
            UPDATE Calificacion
            SET nota = ?,
                descripcion = ?
            WHERE idCalificacion = ?
            """

            self.db.cursor.execute(sql, (nota, descripcion, idCalificacion))
            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al editar calificación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def eliminar(self, idCalificacion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            DELETE FROM Calificacion
            WHERE idCalificacion = ?
            """

            self.db.cursor.execute(sql, (idCalificacion,))
            conexion.commit()

            if self.db.cursor.rowcount == 0:
                print("No existe una calificación con ese ID")
                return False

            return True

        except Exception as e:
            conexion.rollback()
            print("Error al eliminar calificación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def obtenerPromedioPonderado(self, cedulaEstudiante):
        conexion = self.db.conectar()
        if not conexion:
            return 0

        try:
            sql = """
            SELECT
                c.nota,
                e.ponderacion
            FROM Calificacion c
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            WHERE c.cedulaEstudiante = ?
            """

            self.db.cursor.execute(sql, (cedulaEstudiante,))
            resultados = self.db.cursor.fetchall()

            if not resultados:
                return 0

            suma_ponderada = 0
            suma_ponderaciones = 0

            for fila in resultados:
                nota = float(fila.nota)
                ponderacion = float(fila.ponderacion)

                suma_ponderada += nota * ponderacion
                suma_ponderaciones += ponderacion

            if suma_ponderaciones == 0:
                return 0

            promedio = suma_ponderada / suma_ponderaciones
            return round(promedio, 2)

        except Exception as e:
            print("Error al calcular promedio ponderado:", e)
            return 0

        finally:
            self.db.cerrarConexion()


    def obtenerPromedioPonderadoPorCurso(self, cedulaEstudiante, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return 0

        try:
            sql = """
            SELECT
                c.nota,
                e.ponderacion
            FROM Calificacion c
            INNER JOIN Evaluacion e
                ON c.idEvaluacion = e.idEvaluacion
            WHERE c.cedulaEstudiante = ?
            AND c.idCurso = ?
            """

            self.db.cursor.execute(sql, (cedulaEstudiante, idCurso))
            resultados = self.db.cursor.fetchall()

            if not resultados:
                return 0

            suma_ponderada = 0
            suma_ponderaciones = 0

            for fila in resultados:
                nota = float(fila.nota)
                ponderacion = float(fila.ponderacion)

                suma_ponderada += nota * ponderacion
                suma_ponderaciones += ponderacion

            if suma_ponderaciones == 0:
                return 0

            return round(suma_ponderada / suma_ponderaciones, 2)

        except Exception as e:
            print("Error al calcular promedio ponderado del curso:", e)
            return 0

        finally:
            self.db.cerrarConexion()