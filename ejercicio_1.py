def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def mcd_de_divisores(divisores1, divisores2):
    divisores_comunes = set(divisores1) & set(divisores2)
    return max(divisores_comunes)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

divisores_numero1 = encontrar_divisores(numero1)
divisores_numero2 = encontrar_divisores(numero2)

mcd = mcd_de_divisores(divisores_numero1, divisores_numero2)
print(f"El Máximo Común Divisor de {numero1} y {numero2} es {mcd}")
