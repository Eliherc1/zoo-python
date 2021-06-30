from .animal import Animal

class Camello(Animal):
    def __init__(self,nombre, edad):
        super().__init__("Camello de Nombre: " + nombre.capitalize() , edad, 0, 0)
        super().alimentacion()
        self.joroba = 1

    def alimentacion(self):
        self.felicidad = self.felicidad + 15
        self.salud = self.salud + 15
        print(f"Has Alimentado al {self.nombre} en 15, ahora su felicidad es de {self.felicidad} y su Salud de {self.salud}")
        return self

    def display_info_detail(self):
        print(f"Soy un {self.nombre} y tengo {self.joroba} joroba")