from BaseDeDatos import ConexionSQLServer # YA ESTÁ LISTA, QUIZÁ SE LE PUEDAN METER VALIDACIONES
from Modelos.AsignacionDocente import AsignacionDocente
from Modelos.Paralelo import Paralelo
from Modelos.Materia import Materia

class AsignacionDocenteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, asignacion: AsignacionDocente):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:

            sql = """
            INSERT INTO AsignacionDocente
            (
                cedulaDocente,
                idParalelo,
                idMateria
            )
            VALUES (?, ?, ?)
            """

            self.db.cursor.execute(sql, (
                asignacion.cedulaDocente,
                asignacion.idParalelo,
                asignacion.idMateria
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar asignación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def eliminar(self, cedulaDocente, idParalelo, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:

            sql = """
            DELETE
            FROM AsignacionDocente
            WHERE cedulaDocente = ?
            AND idParalelo = ?
            AND idMateria = ?
            """

            self.db.cursor.execute(sql, (
                cedulaDocente,
                idParalelo,
                idMateria
            ))

            conexion.commit()

            return self.db.cursor.rowcount > 0

        except Exception as e:
            conexion.rollback()
            print("Error al eliminar asignación:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def buscar(self, cedulaDocente, idParalelo, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:

            sql = """
            SELECT
                ad.cedulaDocente,
                ad.idParalelo,
                ad.idMateria,
                u.nombre,
                c.nombreCurso,
                p.paralelo,
                m.nombre
            FROM AsignacionDocente ad

            INNER JOIN Usuario u
                ON ad.cedulaDocente = u.cedula

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            WHERE
                ad.cedulaDocente = ?
            AND ad.idParalelo = ?
            AND ad.idMateria = ?
            """

            self.db.cursor.execute(sql, (
                cedulaDocente,
                idParalelo,
                idMateria
            ))

            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return AsignacionDocente(
                fila.cedulaDocente,
                fila.idParalelo,
                fila.idMateria,
                fila.nombre,
                fila.nombreCurso,
                fila.paralelo,
                fila.nombre
            )

        except Exception as e:
            print("Error al buscar estudiante:", e)
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
                ad.cedulaDocente,
                ad.idParalelo,
                ad.idMateria,
                u.nombre AS nombreDocente,
                c.nombreCurso,
                p.paralelo AS nombreParalelo,
                m.nombre AS nombreMateria
            FROM AsignacionDocente ad

            INNER JOIN Usuario u
                ON ad.cedulaDocente = u.cedula

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            ORDER BY
                c.nombreCurso,
                p.paralelo,
                m.nombre
            """

            self.db.cursor.execute(sql)

            asignaciones = []

            for fila in self.db.cursor.fetchall():

                asignaciones.append(
                    AsignacionDocente(
                        fila.cedulaDocente,
                        fila.idParalelo,
                        fila.idMateria,
                        fila.nombreDocente,
                        fila.nombreCurso,
                        fila.nombreParalelo,
                        fila.nombreMateria
                    )
                )

            return asignaciones

        except Exception as e:
            print("Error al listar asignaciones:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT
                ad.cedulaDocente,
                ad.idParalelo,
                ad.idMateria,
                u.nombre AS nombreDocente,
                c.nombreCurso,
                p.paralelo AS nombreParalelo,
                m.nombre AS nombreMateria
            FROM AsignacionDocente ad

            INNER JOIN Usuario u
                ON ad.cedulaDocente = u.cedula

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            WHERE ad.cedulaDocente = ?

            ORDER BY
                c.nombreCurso,
                p.paralelo
            """

            self.db.cursor.execute(sql, (cedulaDocente,))

            asignaciones = []

            for fila in self.db.cursor.fetchall():

                asignaciones.append(
                    AsignacionDocente(
                        fila.cedulaDocente,
                        fila.idParalelo,
                        fila.idMateria,
                        fila.nombreDocente,
                        fila.nombreCurso,
                        fila.nombreParalelo,
                        fila.nombreMateria
                    )
                )

            return asignaciones

        except Exception as e:
            print("Error al buscar asignación del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorParalelo(self, idParalelo):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT
                ad.cedulaDocente,
                ad.idParalelo,
                ad.idMateria,
                u.nombre AS nombreDocente,
                c.nombreCurso,
                p.paralelo AS nombreParalelo,
                m.nombre AS nombreMateria

            FROM AsignacionDocente ad

            INNER JOIN Usuario u
                ON ad.cedulaDocente = u.cedula

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            WHERE ad.idParalelo = ?

            ORDER BY
                m.nombre
            """

            self.db.cursor.execute(sql, (idParalelo,))

            asignaciones = []

            for fila in self.db.cursor.fetchall():

                asignaciones.append(
                    AsignacionDocente(
                        fila.cedulaDocente,
                        fila.idParalelo,
                        fila.idMateria,
                        fila.nombreDocente,
                        fila.nombreCurso,
                        fila.nombreParalelo,
                        fila.nombreMateria
                    )
                )

            return asignaciones

        except Exception as e:
            print("Error al buscar asignaciones:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorParaleloMateria(self, idParalelo, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:

            sql = """
            SELECT
                ad.cedulaDocente,
                ad.idParalelo,
                ad.idMateria,
                u.nombre AS nombreDocente,
                c.nombreCurso,
                p.paralelo AS nombreParalelo,
                m.nombre AS nombreMateria

            FROM AsignacionDocente ad

            INNER JOIN Usuario u
                ON ad.cedulaDocente = u.cedula

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            WHERE
                ad.idParalelo = ?
                AND ad.idMateria = ?
            """

            self.db.cursor.execute(sql, (idParalelo, idMateria))

            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return AsignacionDocente(
                fila.cedulaDocente,
                fila.idParalelo,
                fila.idMateria,
                fila.nombreDocente,
                fila.nombreCurso,
                fila.nombreParalelo,
                fila.nombreMateria
            )

        except Exception as e:
            print("Error al buscar asignación:", e)
            return None

        finally:
            self.db.cerrarConexion()

    
    def listarParalelosDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT DISTINCT

                p.idParalelo,
                p.idCurso,
                c.nombreCurso,
                p.paralelo,
                p.jornada,
                p.cupoMaximo,
                p.estado

            FROM AsignacionDocente ad

            INNER JOIN Paralelo p
                ON ad.idParalelo = p.idParalelo

            INNER JOIN Curso c
                ON p.idCurso = c.idCurso

            WHERE ad.cedulaDocente = ?

            ORDER BY
                c.nombreCurso,
                p.paralelo
            """

            self.db.cursor.execute(sql, (cedulaDocente,))

            paralelos = []

            for fila in self.db.cursor.fetchall():

                paralelo = Paralelo(
                    fila.idParalelo,
                    fila.idCurso,
                    fila.paralelo,
                    fila.jornada,
                    fila.cupoMaximo,
                    fila.estado
                )

                paralelo.nombreCurso = fila.nombreCurso

                paralelos.append(paralelo)

            return paralelos

        except Exception as e:
            print("Error al listar paralelos del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()

    
    def listarMateriasDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:

            sql = """
            SELECT DISTINCT

                m.idMateria,
                m.nombre,
                m.descripcion,
                m.horas,
                m.estado

            FROM AsignacionDocente ad

            INNER JOIN Materia m
                ON ad.idMateria = m.idMateria

            WHERE ad.cedulaDocente = ?

            ORDER BY m.nombre
            """

            self.db.cursor.execute(sql, (cedulaDocente,))

            materias = []

            for fila in self.db.cursor.fetchall():

                materias.append(
                    Materia(
                        fila.idMateria,
                        fila.nombre,
                        fila.descripcion,
                        fila.horas,
                        fila.estado
                    )
                )

            return materias

        except Exception as e:
            print("Error al listar materias del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def docenteTieneAsignacion(self, cedulaDocente, idParalelo, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:

            sql = """
            SELECT 1
            FROM AsignacionDocente
            WHERE
                cedulaDocente = ?
                AND idParalelo = ?
                AND idMateria = ?
            """

            self.db.cursor.execute(sql, (
                cedulaDocente,
                idParalelo,
                idMateria
            ))

            return self.db.cursor.fetchone() is not None

        except Exception as e:
            print("Error al validar asignación de docente:", e)
            return False

        finally:
            self.db.cerrarConexion()