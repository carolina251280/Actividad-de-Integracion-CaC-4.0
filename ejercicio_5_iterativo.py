def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("¡Valor no válido! Intente nuevamente.")

numero = get_int()
print(f"Valor entero ingresado: {numero}")
