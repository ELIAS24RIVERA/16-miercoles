import numpy as np

# Crear dos matrices de 3x3
matriz_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matriz_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Multiplicar las dos matrices
resultado = np.dot(matriz_a, matriz_b)

# Imprimir las matrices y el resultado
print("Matriz A (3x3):")
print(matriz_a)

print("\nMatriz B (3x3):")
print(matriz_b)

print("\nResultado de la multiplicación (3x3):")
print(resultado)
