def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("¡Valor no válido! Intente nuevamente.")
        return get_int()

numero = get_int()
print(f"Valor entero ingresado: {numero}")