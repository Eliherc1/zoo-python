from .animal import Animal

class Delfin(Animal):
    def __init__(self, aletas, nombre, edad):
        super().__init__("Delfin, Nombre: " + nombre.capitalize(), edad, 0, 0)
        super().alimentacion()
        self.aletas=aletas

    def alimentacion(self, cant_fel, cant_salud):
        self.felicidad = self.felicidad + cant_fel
        self.salud = self.salud + cant_salud
        return self