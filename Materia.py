class Materia: 
    def __init__(self, idMateria, nombre, descripcion):
        self.idMateria = idMateria
        self.nombre = nombre
        self.descripcion = descripcion
        self.activa = True

    def mostrarMateriasDisponibles(self, listaMaterias):
        if len(listaMaterias) == 0:
            print("No hay materias registradas")
            return

        print("----- MATERIAS DISPONIBLES -----")

        for materia in listaMaterias:
            print(f"ID: {materia.idMateria}")
            print(f"Nombre: {materia.nombre}")
            print(f"Descripción: {materia.descripcion}")
            print("-" * 30)

    def actualizarContenido(self, nuevoNombre, nuevaDescripcion):
        self.nombre = nuevoNombre
        self.descripcion = nuevaDescripcion
        
        print("Materia actualizada correctamente.")
        print(f"ID: {self.idMateria}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")

    def habilitarRetiroMateria(self):
        self.activa = False
        print(f"La materia {self.nombre} ha sido retirada.")

#funcion Mostrar materias disponibles
materia1 = Materia(1, "Algebra Lineal", "Álgebra Lineal")
materia2 = Materia(2, "Base de datos", "integracion de SQL")

listaMaterias = [materia1, materia2]

materia1.mostrarMateriasDisponibles(listaMaterias)

#funcion actualizar materias
materia1.actualizarContenido(
    "Matemáticas Avanzadas",
    "Álgebra y Trigonometría"
)

listaMaterias = [materia1]

#funcion desabilitar materias
materia1.habilitarRetiroMateria()
