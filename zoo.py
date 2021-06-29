#from clases.animal import Animal
from clases.camello import Camello
from clases.flamenco import Flamenco
from clases.delfin import Delfin


class Zoo:
    def __init__(self, zoo_nombre):
        self.name = zoo_nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for a in range (len(self.animales)):
            print("Posicion ", a)
            self.animales[a].display_info()

    def cantidad_animales(self):
        return len(self.animales)

    def get_animal(self,posicion):
        return self.animales[posicion]

    def __str__(self):
        return self.name


zoo1 = Zoo("Chimu's Zoo")
print("-"*30, "Bienvenido a ", zoo1, "-"*30)

while True:
    numero = input(
        "1: AGREGAR ANIMAL\n2: MOSTRAR ANIMALES\n3: ALIMENTAR ANIMALES\n4: SALIR\nIngrese su Opcion: ")
    if int(numero) == 4:
        break
# AGREGAR ANIMALES
    elif int(numero) == 1:
        while True:
            num_tipo = input(
                "1: CAMELLO\n2: DELFIN\n3: FLAMENCO\n4: VOLVER\nIngrese su Opcion: ")
            if int(num_tipo) == 1:
                nombre = input("Ingrese el Nombre: ")
                edad = input("Ingrese el Edad: ")
                fel = input("Ingrese el nivel Felicidad: ")
                sal = input("Ingrese el nivel Salud: ")

                animal1 = Camello(1, nombre, edad)
                zoo1.agregar_animal(animal1)
                animal1.alimentacion(int(fel), int(sal))

            elif int(num_tipo) == 2:
                nombre = input("Ingrese el Nombre: ")
                edad = input("Ingrese el Edad: ")
                fel = input("Ingrese el nivel Felicidad: ")
                sal = input("Ingrese el nivel Salud: ")

                animal2 = Delfin(1, nombre, edad)
                zoo1.agregar_animal(animal2)
                animal2.alimentacion(int(fel), int(sal))

            elif int(num_tipo) == 3:
                nombre = input("Ingrese el Nombre: ")
                edad = input("Ingrese el Edad: ")
                fel = input("Ingrese el nivel Felicidad: ")
                sal = input("Ingrese el nivel Salud: ")

                animal3 = Flamenco(1, nombre, edad)
                zoo1.agregar_animal(animal3)
                animal3.alimentacion(int(fel), int(sal))

            else:
                int(num_tipo) == 4
                break
# MOSTRAR ANIMALES
    elif int(numero) == 2:
        zoo1.print_all_info()
        print("Cantidad de Animales en el ZOO: ",zoo1.cantidad_animales())

# ALIMENTAR ANIMALES
    elif int(numero) == 3:
        if zoo1.cantidad_animales() == 0:
            print("ATENCION: Aun no se han creado Animales en el ZOO, utilice la opcion 1 y agregue un nuevo animal")
            
        else:
            print("-"*30,"Listado Animales Ingresados","-"*30)
            zoo1.print_all_info()

            while True:
                op = input("Ingrese Posicion del Animal(Para SALIR Ingrese -1): ")
                if int(op) >= zoo1.cantidad_animales():
                    print("""EL NUMERO INGRESADO NO ES VALIDO, PORFAVOR INTENTA CON OTRO NUMERO!!!!!!!!!!""")
                elif int(op) == -1:
                    break           
                else:
                    fel = input("Ingrese el nivel Felicidad: ")
                    sal = input("Ingrese el nivel Salud: ")
                    zoo1.get_animal(int(op)).alimentacion(int(fel), int(sal))
                    zoo1.get_animal(int(op)).mostrar_alimentacion()
    else:
        print("""EL NUMERO INGRESADO NO ES VALIDO, PORFAVOR INTENTA CON OTRO NUMERO!!!!!!!!!!""")
