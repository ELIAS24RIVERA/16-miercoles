def encontrar(lista):
    numeros_visto = set()
    for numero in lista:
        complemento = -numero
        if complemento in numeros_visto:
            print(f"los numeros {numero} y {complemento} suma 0")
        numeros_visto.add(numero)
lista = [3, -1, 4, -2, 1, -3, 5, -4]
encontrar(lista)