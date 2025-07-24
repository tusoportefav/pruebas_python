def dictionary():
    glossary = {}

    while True:
        key  = input("Ecribe un nombre para tu agenda de contactos o salir para finalizar: ")
        if key.lower() == "salir":
            break
        
        if key in glossary.keys():
            while True:
                answer = input("¿Quieres remplazarlo? (si/no): ").lower()
                if answer == "si":
                    break
                elif answer == "no":
                    key = input("Ecribe un nombre para tu agenda de contactos: ")
                    if key == "salir".lower():
                        return
                    break
                else:
                    print("Respuesta no valida escribe 'si' o 'no' ")

        value = input("Escribe el numero para tu contacto guardado o salir para finalizar: ")
        if value.lower()  == "salir":
            break
        
        if value in glossary.values():
            while True:
                answer2 = input("¿Quieres remplazarlo? (si/no): ").lower()
                if answer2 == "si":
                    break
                elif answer2 == "no":
                    value = input("Escribe un numero diferente para tu contacto: ")
                    if value == "salir":
                        return
                    break  
                else:
                    print("Respueta no valida, escribe 'si' o 'no'")
                    

        if value.isdigit() and len(value) == 10:
            glossary[key] = value
        else:
            print("Numero de contacto no valido (verificar que sean 10 numeros y que no lleve puntos o comas)")

    for key, value in glossary.items():
        print(f"{key} : {value}")

dictionary()  
