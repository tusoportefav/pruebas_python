def contrasena_fuerte(contrasena):
    if len(contrasena)<8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_simbolo = False

    simbolos = "!#$%&@"

    for char in contrasena:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_numero = True
        elif char in simbolos:
            tiene_simbolo = True
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo

usuario = input("Ingresa una contraseña: ")

if contrasena_fuerte(usuario):
    print(f"{usuario}, es una contraseña fuerte")
else:
    print(f"\n{usuario}, es una contraseña debil")