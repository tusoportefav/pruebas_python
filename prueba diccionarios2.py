def contacts():
    glossary = {}

    while True:
        key = input("Ingresa el nombre o (salir) para finalizar: ")
        if key.lower() == "salir":
            break
        
        if key in glossary.keys():
            while True:
                answer = input("Este contacto ya existe. ¿Deseas remplazarlo? (si/no): ")
                if answer.lower() == "si":
                    break
                if answer.lower() == "no":
                    key = input("Ingresa el nombre del contacto: ")
                    if key.lower() == "salir":
                        return
                    break
                else:
                    print("solo puedes responder si y no")

        symbols = "#!$%&/¿?()"

        while True:
            value = input("Ingresa el numero de contacto o (salir) para finalizar: ")
            if value.lower() == "salir":
                return
            if any(symbol in value for symbol in symbols):
                print("No puede tener simbolos")
                continue
            if not value.isdigit():
                print("Solo puede tener numeros")
                continue
            if len(value)!= 10:
                print("Solo puede tener 10 numeros")
                continue
            break
        
        if value in glossary.values():
            while True:
                answer2 = input("Este numero de contaco ya existe. ¿Deseas remplazarlo? (si/no): ")
                if answer2.lower() == "si":
                    break
                if answer2.lower() == "no":
                    while True:
                        value = input("Ingresa un numero de contacto diferente: ")
                        if value.lower() == "salir":
                            return
                        if any(symbol in value for symbol in symbols):
                            print("No puede tener simbolos")
                            continue
                        if not value.isdigit():
                            print("Solo puede tener numeros")
                            continue
                        if len(value)!= 10:
                            print("Solo puede tener 10 numeros")
                            continue
                        break
                    break
                else:
                    print("Respuesta no valida ingresa (si/no)")
                
        glossary [key] = value
        
    
        
    print("==Agenda de Contactos==")
    for key, value in glossary.items():
        print(f"{key} : {value}")

contacts()
                        

