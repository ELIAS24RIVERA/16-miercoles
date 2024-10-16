def validar(edad):
    if edad < 0:
        print("no existe esa edad.")
    elif 60 >= edad >= 18:
        print("tienes la edad suficiente para votar.")
    else:
        print("no tiene la edad suficiente para votar.")
try:
    edad_usuario = int(input("por favor, introdusca tu edad: "))
    validar(edad_usuario)
except ValueError:
    print("por favor, introduces un numero valido")