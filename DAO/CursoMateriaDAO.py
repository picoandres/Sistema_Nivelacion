from BaseDeDatos import ConexionSQLServer # CLASE VIEJA, PROBABLEMENTE DEBA MODIFICARSE O ELIMINARSE
from Modelos.Materia import Materia

class CursoMateriaDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def _existeEnConexion(self, idCurso, idMateria):
        sql = """
        SELECT 1
        FROM CursoMateria
        WHERE idCurso = ? AND idMateria = ?
        """
        self.db.cursor.execute(sql, (idCurso, idMateria))
        return self.db.cursor.fetchone() is not None


    def existe(self, idCurso, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            return self._existeEnConexion(idCurso, idMateria)

        except Exception as e:
            print("Error al verificar asignación curso-materia:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def guardar(self, idCurso, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql_curso = """
            SELECT 1
            FROM Curso
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_curso, (idCurso,))
            if self.db.cursor.fetchone() is None:
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

            if self._existeEnConexion(idCurso, idMateria):
                print(f"\nLa materia {idMateria} ya está asignada al curso {idCurso}")
                return False

            sql = """
            INSERT INTO CursoMateria
            (
                idCurso,
                idMateria
            )
            VALUES (?, ?)
            """

            self.db.cursor.execute(sql, (idCurso, idMateria))
            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al asignar materia al curso:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def buscarMateriasPorCurso(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                m.idMateria,
                m.nombre,
                m.descripcion,
                m.horas,
                m.estado
            FROM CursoMateria cm
            INNER JOIN Materia m
                ON cm.idMateria = m.idMateria
            WHERE cm.idCurso = ?
            ORDER BY m.nombre
            """

            self.db.cursor.execute(sql, (idCurso,))
            resultados = self.db.cursor.fetchall()

            materias = []
            for fila in resultados:
                materia = Materia(
                    fila.idMateria,
                    fila.nombre,
                    fila.descripcion,
                    fila.horas,
                    fila.estado
                )
                materias.append(materia)

            return materias

        except Exception as e:
            print("Error al buscar materias del curso:", e)
            return []

        finally:
            self.db.cerrarConexion()