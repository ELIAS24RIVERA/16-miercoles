def palabra_mas_larga(lista_palabras):
    return max(lista_palabras, key=len)

# Ejemplo de uso
palabras = ["python", "algoritmo", "desarrollo", "inteligencia", "artificial"]
print(f"La palabra más larga es: {palabra_mas_larga(palabras)}")