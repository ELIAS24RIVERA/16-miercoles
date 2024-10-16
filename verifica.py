import re
def validar_contraseña(contraseña):
    if(6 <= len(contraseña) <= 16 and
       re.search(r'[a-z]', contraseña)and
       re.search(r'[A-Z]', contraseña)and
       re.search(r'[0-9]', contraseña)and
       re.search(r'[$#@]', contraseña)):
        return True
    return False
contraseña = input("ingresa una contraseña")
if validar_contraseña(contraseña):
    print("contraseña valida")
else:
    print("contraseña invalida")