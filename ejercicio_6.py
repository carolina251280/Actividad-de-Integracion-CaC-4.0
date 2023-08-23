class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Edad no válida.")
            self.__edad = 0
    
    def get_edad(self):
        return self.__edad
    
    def set_dni(self, dni):
        if len(dni) == 8:  
            self.__dni = dni
        else:
            print("DNI no válido.")
            self.__dni = dni
    
    def get_dni(self):
        return self.__dni
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
dni = input("Ingrese el DNI: ")

persona1 = Persona()
persona1.set_nombre(nombre)
persona1.set_edad(edad)
persona1.set_dni(dni)

persona1.mostrar()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
