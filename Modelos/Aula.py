class Aula:
    capacidad_maxima = 40

    def __init__(self, id_aula, nombre, capacidad, modalidad, tipo, estado):
        self.id = id_aula
        self.nombre = nombre
        self.capacidad = capacidad
        self.modalidad = modalidad
        self.tipo = tipo
        self.estado = estado

    def mostrarInfo(self):
        print(f"ID        : {self.id}")
        print(f"Nombre    : {self.nombre}")
        print(f"Capacidad : {self.capacidad}")
        print(f"Modalidad : {self.modalidad}")
        print(f"Tipo      : {self.tipo}")
        print(f"Estado    : {'Disponible' if self.estado else 'No disponible'}")