from Aula import Aula

class AulaVirtual(Aula):
    def __init__(self, id_aula, nombre, capacidad, modalidad, tipo, estado, plataforma, enlace):
        super().__init__(id_aula, nombre, capacidad, modalidad, tipo, estado)
        self.plataforma = plataforma
        self.enlace = enlace

    def mostrar_info(self):
        super().mostrar_info(self)
        print(f"Plataforma: {self.plataforma}")
        print(f"URL: {self.enlace}")
        
    def cerrar_aula(self):
        print("Cerrando aula ")
        self.estado = False
        
    def abrir_aula(self):
        print("Abriendo aula ")
        self.estado = True
