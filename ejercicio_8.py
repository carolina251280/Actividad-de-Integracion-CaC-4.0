class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Cuenta:
    def __init__(self, titular, cantidad=1000.0): 
        self.titular = titular
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("DNI del titular:", self.titular.dni)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
        else:
            print("Saldo insuficiente")

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=500.0):  
        super().__init__(titular, cantidad)
        self.__bonificacion = 5.0  

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        edad = self.titular.edad
        return 18 <= edad <= 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            if cantidad <= self.get_cantidad():
                super().retirar(cantidad)
            else:
                print("Saldo insuficiente")
        else:
            print("Retiro no permitido para titulares no válidos")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion, "%")  

def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()

nombre_titular = input("Ingresar el nombre del titular: ")
dni_titular = input("Ingresar el DNI del titular: ")
while not validar_dni(dni_titular):
    print("DNI inválido. Asegúrate de que sea un número de 8 dígitos.")
    dni_titular = input("Ingresar el DNI del titular: ")

edad_titular = int(input("Ingresar la edad del titular: "))

titular = Persona(nombre_titular, dni_titular, edad_titular)

if 18 <= edad_titular <= 25:
    cuenta = CuentaJoven(titular)
else:
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
