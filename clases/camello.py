from .animal import Animal

class Camello(Animal):
    def __init__(self, joroba, nombre, edad):
        super().__init__("Camello, Nombre: " + nombre.capitalize() , edad, 0, 0)
        super().alimentacion()
        self.joroba = joroba

    def alimentacion(self, cant_fel, cant_salud):
        self.felicidad = self.felicidad + cant_fel
        self.salud = self.salud + cant_salud
        return self