from Aula import Aula

class AulaFisica(Aula):
    def __init__(self, id_aula, nombre, capacidad, modalidad, tipo, estado, ubicacion, bloque):
        super().__init__(id_aula, nombre, capacidad, modalidad, tipo, estado)
        self.ubicacion = ubicacion
        self.bloque = bloque
        
    def mostrar_info(self):
        super().mostrar_info(self)
        print(f"Ubicación: {self.ubicacion}")
        print(f"Bloque: {self.bloque}")
