from .animal import Animal

class Delfin(Animal):
    def __init__(self,nombre, edad):
        super().__init__("Delfin de Nombre: " + nombre.capitalize(), edad, 0, 0)
        super().alimentacion()
        self.aletas=2

    def alimentacion(self):
        self.felicidad = self.felicidad + 20
        self.salud = self.salud + 20
        print(f"Has Alimentado al {self.nombre} en 20, ahora su felicidad es de {self.felicidad} y su Salud de {self.salud}")
        return self

    def display_info_detail(self):
        print(f"Soy un {self.nombre} y tengo {self.aletas} aletas")
