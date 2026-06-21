from abc import ABC, abstractmethod

class Aula(ABC):
    def __init__(self, id_aula, nombre, capacidad, modalidad, tipo, estado):
        self.id = id_aula
        self.nombre = nombre
        self.capacidad = capacidad
        self.modalidad = modalidad
        self.tipo = tipo
        self.estado = estado
        self.aulas = []
        
        
    def mostrar_info(self):
        print(self.nombre)
        print(f"Id: {self.id}")
        print(f"Capacidad {self.capacidad}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")
    
