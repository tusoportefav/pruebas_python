def validationofcontact(num):
    symbols = "!.,#$%&/()?¿¡=-[]}{;:_<>"
    if any(symbol in num for symbol in symbols):
        print ("No puede tener symbol")
        return False
    if not num.isdigit():
        print("Debe tener solo numeros")  
        return False
    if len(num) != 10:
        print("Debe tener 10 numeros")
        return False
    return True

def contact():
    glossary = {}


    while True:
        print("Menu")
        print("1.Buscar contacto")
        print("2.Agregar Contato")
        print("3.Borrar Contacto")
        print("4.Ver Agenda de contactos")
        print("5.Salir del Menu")

        optionts = input("¿Que vas a realizar? 1-5: ")

        if optionts == "1":
            print("==Agenda de Contactos==")
            if not glossary:
                print("No tienes contactos agregados")
                continue
            else:
                for key, value in glossary.items():
                    print("==Agenda de Contactos==")
                    print(f"{key} : {value}")

            search = (input("\nEscribe el nombre del contacto para buscarlo: "))
            if search in glossary:
                print(f"{search} : {glossary[search]}")
            else:
                print("El contacto no existe")
       
        elif optionts == "2":
            while True:
                key = input("Escribe el nombre o (salir) para volver al menu: ")
                if key.lower() == "salir":
                    break
                if key in glossary.keys():
                    while True:
                        answer = input("El contacto ya existe. ¿Deseas remplazarlo? (si/no): ")
                        if answer.lower() == "salir":
                            return
                        if answer.lower() == "si":
                            break
                        if answer.lower() == "no":
                            key = input("Escribe un diferente nombre de contacto: ")
                            if key.lower() == "salir":
                                return
                            if key in glossary.keys():
                                continue
                            else:
                                break
                        else:
                            print("Solo puedes responder con si o no")                      


                while True:
                    value = input("Escribe un numero de contacto: ")
                    if value.lower() == "salir":
                        return

                    if not validationofcontact(value):
                        continue
                
                    if value in glossary.values():
                        answer2 = input("Este numero ya existe. ¿Deseas remplazarlo? (si/no): ")
                        if answer2.lower() == "salir":
                            return
                        elif answer2.lower() == "si":
                            for name, num in list(glossary.items()):
                                if num == value:
                                    del glossary[name]
                                    print(f"Remplazado con exito")
                                    break
                            break
                        elif answer2.lower() == "no":
                            value = input("Escribe un numero de contacto diferente: ")
                            if value == "salir":
                                return
                            if not validationofcontact(value):
                                continue
                            if value in glossary.values():
                                continue
                            break
                        
                        else:
                            print("Responde con 'si' o 'no'")
                    else:
                        break 
                    
                         
             
                glossary[key] = value
                print(f"{key}, (agregado con exito)")
                break

        elif optionts == "3":
            if not glossary:
                print("\nNo tienes contactos agregados\n")
                continue
            else:
                print("==Agenda de Contactos==")
                for key, value in glossary.items():
                    print(f"{key} : {value}")
            
            delete = input("\nEscribe el nombre del contacto para eliminarlo: ")
            if delete in glossary:
                del glossary[delete]
                print(f"{delete}, (borrado de la agenda)")
                continue
        
            else:
                print(f"El contacto {delete} no existe")
                continue
    

        elif optionts == "4":
            print("==Agenda de Contactos==")
            for key, value in glossary.items():
                print(f"{key} : {value}")       
                continue
        
        elif optionts == "5":
            print ("==Hasta luego==")
            return

        else:
            print("Solo puede ser un numero del 1-5") 


contact()

        

