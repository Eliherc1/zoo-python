from .animal import Animal

class Flamenco(Animal):
    def __init__(self, alas, nombre, edad):
        super().__init__("Flamenco, Nombre: " + nombre.capitalize(), edad,0 ,0)
        super().alimentacion()
        self.alas=alas

    def alimentacion(self, cant_fel, cant_salud):
        self.felicidad = self.felicidad + cant_fel
        self.salud = self.salud + cant_salud
        return self