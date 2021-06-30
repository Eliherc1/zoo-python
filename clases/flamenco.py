from .animal import Animal

class Flamenco(Animal):
    def __init__(self, nombre, edad):
        super().__init__("Flamenco de Nombre: " + nombre.capitalize(), edad,0 ,0)
        super().alimentacion()
        self.alas= 2

    def alimentacion(self):
        self.felicidad = self.felicidad + 30
        self.salud = self.salud + 30
        print(f"Has Alimentado al {self.nombre} en 30, ahora su felicidad es de {self.felicidad} y su Salud de {self.salud}")
        return self
    
    def display_info_detail(self):
        print(f"Soy un {self.nombre} y tengo {self.alas} alas")
