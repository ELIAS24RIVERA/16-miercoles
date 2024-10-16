def fibonacci(n):
    secuencia = [0, 1]  # Los primeros dos términos de la secuencia de Fibonacci

    # Generar los términos restantes
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]  # Suma de los dos términos anteriores
        secuencia.append(siguiente)

    return secuencia[:n]  # Retorna la secuencia hasta n términos
 
# Ejemplo de uso
num_terminos = 20
print(f"Secuencia de Fibonacci con {num_terminos} términos: {fibonacci(num_terminos)}")