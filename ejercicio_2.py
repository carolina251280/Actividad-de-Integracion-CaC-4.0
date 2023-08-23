def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def mcm_de_divisores(divisores1, divisores2):
    
    divisores_totales = set(divisores1) | set(divisores2)
    return min(divisores_totales)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

divisores_numero1 = encontrar_divisores(numero1)
divisores_numero2 = encontrar_divisores(numero2)

mcm = mcm_de_divisores(divisores_numero1, divisores_numero2)
print(f"El Mínimo Común Múltiplo de {numero1} y {numero2} es {mcm}")


