def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia_palabras = {}
    
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras

def palabra_mas_repetida(diccionario):
    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    frecuencia = diccionario[palabra_mas_repetida]
    return palabra_mas_repetida, frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

palabra_repetida, frecuencia_palabra_repetida = palabra_mas_repetida(resultado)
print(f"Palabra más repetida: {palabra_repetida} (Frecuencia: {frecuencia_palabra_repetida})")
