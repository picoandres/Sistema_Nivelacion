from BaseDeDatos import ConexionSQLServer
from Materia import Materia

class MateriaDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, materia: Materia):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            INSERT INTO Materia
            (
                idMateria,
                nombre,
                descripcion,
                horas,
                estado
            )
            VALUES (?, ?, ?, ?, ?)
            """

            self.db.cursor.execute(sql, (
                materia.idMateria,
                materia.nombre,
                materia.descripcion,
                materia.horas,
                materia.estado
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar materia:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT idMateria, nombre, descripcion, horas, estado
            FROM Materia
            ORDER BY idMateria
            """

            self.db.cursor.execute(sql)
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
            print("Error al listar materias:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscar(self, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT idMateria, nombre, descripcion, horas, estado
            FROM Materia
            WHERE idMateria = ?
            """

            self.db.cursor.execute(sql, (idMateria,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            return Materia(
                fila.idMateria,
                fila.nombre,
                fila.descripcion,
                fila.horas,
                fila.estado
            )

        except Exception as e:
            print("Error al buscar materia:", e)
            return None

        finally:
            self.db.cerrarConexion()