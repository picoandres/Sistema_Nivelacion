from Aula import Aula

class AulaFisica(Aula):
    def __init__(self, id_aula, nombre, capacidad, modalidad, tipo, estado, ubicacion, bloque):
        super().__init__(id_aula, nombre, capacidad, modalidad, tipo, estado)
        self.ubicacion = ubicacion
        self.bloque = bloque
        
    def mostraInfo(self):
        super().mostrarInfo(self)
        print(f"Ubicación: {self.ubicacion}")
        print(f"Bloque: {self.bloque}")
