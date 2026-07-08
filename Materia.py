class Materia:
    def __init__(self, idMateria, nombre, descripcion, horas, estado=True):
        self.idMateria = idMateria
        self.nombre = nombre
        self.descripcion = descripcion
        self.horas = horas
        self.estado = estado

    def verInformacion(self):
        print(f"ID: {self.idMateria}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Horas: {self.horas}")
        print(f"Estado: {'Activa' if self.estado else 'Inactiva'}")

    def cambiarEstado(self, nuevo_estado):
        self.estado = nuevo_estado

    def editarMateria(self, nuevoNombre=None, nuevaDescripcion=None, nuevasHoras=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevaDescripcion:
            self.descripcion = nuevaDescripcion
        if nuevasHoras is not None:
            self.horas = nuevasHoras

    def __str__(self):
        estado = "Activa" if self.estado else "Inactiva"
        return f"{self.idMateria} - {self.nombre} ({estado})"