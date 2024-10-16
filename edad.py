def verificar_edad(edad):
    if edad < 0:
        print("no existe esa edad.")
    elif edad >= 18:
        print("tienes la edad suficiente para votar.")
    else:
        print("no tiene la edad suficiente para votar.")
try:
    edad_usuario = int(input("por favor, introduce tu edad: "))
    verificar_edad(edad_usuario)
except ValueError:
    print("por favor, introdusce un numero valido.")