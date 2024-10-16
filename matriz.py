import numpy as np

# Crear y mostrar la matriz de 4x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Matriz original (4x3):\n", matriz)

# Eliminar la tercera columna y mostrar la matriz reducida
matriz_reducida = np.delete(matriz, 2, axis=1)
print("\nMatriz reducida (4x2):\n", matriz_reducida)

