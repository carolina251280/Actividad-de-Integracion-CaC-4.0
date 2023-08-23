def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia_palabras = {}
    
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
