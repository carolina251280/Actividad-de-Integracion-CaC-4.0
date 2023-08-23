class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Cuenta:
    def __init__(self, titular, cantidad=1000.0):
        self.titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("DNI del titular:", self.titular.dni)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
        else:
            print("Saldo insuficiente.")

def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()

nombre_titular = input("Ingresar el nombre del titular: ")
dni_titular = input("Ingresar el DNI del titular: ")
while not validar_dni(dni_titular):
    print("DNI inválido. Asegúrate de que sea un número de 8 dígitos.")
    dni_titular = input("Ingresar el DNI del titular: ")

edad_titular = int(input("Ingresar la edad del titular: "))
titular = Persona(nombre_titular, dni_titular, edad_titular)

if edad_titular >= 18:
    cuenta = Cuenta(titular)
    while True:
        print("\nOpciones:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar datos de la cuenta")
        print("4 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingreso = float(input("Ingrese la cantidad a ingresar: "))
            cuenta.ingresar(ingreso)
        elif opcion == '2':
            retiro = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(retiro)
        elif opcion == '3':
            cuenta.mostrar()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
else:
    print("Cuenta no válida para menores de edad.")

