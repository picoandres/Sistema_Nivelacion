class Materia:
    def __init__(self, idMateria, nombre, descripcion, horas, estado=True):
        self.idMateria = idMateria
        self.nombre = nombre
        self.descripcion = descripcion
        self.horas = horas
        self.estado = estado

    def mostrarInformacionMateria(self):
        descripcion = self.descripcion if self.descripcion else "Sin descripción"
        estado = "Activa" if self.estado else "Inactiva"

        print(f"ID: {self.idMateria}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Horas: {self.horas}")
        print(f"Estado: {estado}")


    def __str__(self):
        estado = "Activa" if self.estado else "Inactiva"
        return f"{self.idMateria} - {self.nombre} ({estado})"