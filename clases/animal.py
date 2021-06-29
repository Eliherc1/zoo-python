class Animal:
    def __init__(self, nombre , edad, felicidad, salud):
        self.nombre = nombre
        self.edad = edad
        self.felicidad= felicidad
        self.salud=salud

    def display_info(self):
        print(f"""
        Animal: {self.nombre} 
        Edad: {self.edad}
        Nivel de Felicidad: {self.felicidad}
        Nivel de Salud: {self.salud}""")
        return self

    def alimentacion(self):
        self.felicidad=self.felicidad + 10
        #return self.felicidad
        self.salud=self.salud +10
        #return self.salud
        return self

    def mostrar_alimentacion(self):
        print(f"""
        Animal: {self.nombre}
        Nivel de Felicidad: {self.felicidad}
        Nivel de Salud: {self.salud}""")
        return self