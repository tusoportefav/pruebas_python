
#PARTE 1 Lógica básica y estructuras
def is_even(x):
    if x % 2 == 0:
       return True

def order_x():
    even = []
    odd  = []
    
    for num in range(2, 21):
        if is_even(num):
            even.append(num)
        else:
            odd.append(num)
    return even, odd

even, odd = order_x()

print(f"{even}, es par")
print(f"{odd}, es impar")


#PARTE 2  Diccionarios, listas y validaciones
#Crea un programa que simule una agenda de contactos. Cada contacto tiene: nombre, teléfono y correo. Permite agregar, eliminar, mostrar todos y buscar por nombre. Usa un diccionario.

def validationofcontact(x):
    symbols = "!.,#$%&/()?¿¡=-[]}{;:_<>" 
    if any(symbol in symbols for symbol in x):
        print("No debe tener simbolos")
        return False
    if not x.isdigit():
        print("Solo debe tener numero")
        return False
    if len(x) != 10:
        print("Debe tener 10 numeros")
        return False
    return True


def contact():
    glossary = {}

    while True:
        print("==MENU==")
        print("1.Agregar Contacto")
        print("2.Elimina Contacto")
        print("3.Mostar Todos")
        print("4.Buscar por Nombre")
        print("5.Salir")

        options = input("¿Que opcion deseas elegir? (1-5) o (salir) para ir al menu: ")

        if options == "1":
            while True:
                key = input("Escribe un nombre para el contacto o (salir) para volver al menu: ")
                if key.lower() == "salir":
                    break
                if key in glossary.keys():
                    while True:
                        answer = input("El contacto ya existe deseas remplazarlo (si/no): ").lower()
                        if answer == "si":
                            break
                        if answer == "no":
                            while True:
                                key = input("Escribe un nombre de contacto diferente: ")   
                                if key in glossary.keys():
                                    continue    
                                break                           
                                                    
                        else:
                            print("Solo puede responder (si/no)")
                            break
                        break                       
                    
                    
                        
                while True:
                    value = input("Escribe su numero de contacto: ")
                    if not validationofcontact(value):
                        continue
                    if value in glossary.values():
                        answer2 = input("El numero de contacto ya existe ¿Deseas remplazarlo?(si/no): ")
                        if answer2 == "si":
                            for name, number in list(glossary.items()):
                                if number == value:
                                    del glossary[name]
                                    print(f"{name}, remplazado con exito por {key}")
                                    break                            
                        elif answer2 == "no":                                
                            value = input ("Escribe un numero diferente: ")
                            if value in glossary.values():
                                continue
                            if not validationofcontact(value):
                                continue
                            break       

                        else:                        
                            print("Solo puede responder (si/no)")  

                    else:
                        break            
                                
                    
            
                glossary[key] = value
                print(f"{key}, agregado con exito")
                break

        elif options == "2":
            if not glossary:
                print("No tienes contactos agregados")
                continue
            else:
                print("==Agenda de Contactos==")
                for key, value in sorted(glossary.items()):
                    print(f"{key} : {value}")

            delate = input("¿Que contactos deseas agregar?: ").lower()
            if delate in glossary:
                del glossary[delate]
                print(f"{delate}, borrado con exito")

        elif options == "3":
            if not glossary:
                print("No tienes contactos agregados")
            else:
                print("==Agenda de Contactos==")
                for key, value in sorted(glossary.items()):
                    print(f"{key} : {value}")

        elif options == "4":
            if not glossary:
                print("No tienes contactos agregados")
                continue
            search = input("¿Que contacto deseas buscar?: ")
            if search in glossary:
                print(f"{search} : {glossary[search]}")

        else:
            options == "5"
            print("Hasta Luego")
            return                      
                                                    

contact()

#Escribe una función que reciba una cadena y devuelva un diccionario 
#con la cantidad de veces que aparece cada letra (ignora espacios y hazlo en minúsculas).
# ejemplo de entrada: "Hola Mundo"
# salida esperada: {'h':1, 'o':2, 'l':1, 'a':1, 'm':1, 'u':1, 'n':1, 'd':1}

def string():
   
    glossary = {}

    text_modified = "Hola hola".lower().replace(" ","")

    for x in text_modified:
        if x in glossary:
            glossary[x] += 1
        else:
            glossary[x] = 1

    print(glossary)

string()

#. Escribe una función que reciba un texto y devuelva cuántas vocales tiene cada una.
# ejemplo: contar_vocales("Esto es una prueba")
# salida: {'a':1, 'e':2, 'i':0, 'o':1, 'u':2}

vawuels = "a","e","i","o","u"

def count_vawuels():

    new_glossary = {}

    text = "esto es una prueba"

    for y in text:
        if y in vawuels:
            if y in new_glossary:
                new_glossary[y] += 1
            else:
                new_glossary[y] = 1
      
    print(new_glossary)
            

count_vawuels()

def consonants():

    frase = "Esto es una prueba de Python"
    vocales = "aeiouAEIOUÁÉÍÓÚáéíóú"
    my_glossary = []

    for x in frase:
        if x.isalpha() and not x in vocales:
            my_glossary.append(x.lower())

    sorted_myglossary = sorted(my_glossary)

    print(sorted_myglossary)
    print(len(sorted_myglossary))

consonants()

def consonant_sorted():

    phrase = "Esto es una prueba de Python"
    notvawuels = "aeiouAEIOUÁÉÍÓÚáéíóú"
    mydict = {}

    for x in phrase:
        x = x.lower()
        if x.isalpha() and not x in notvawuels:
            if x in mydict:
                mydict[x] +=1
            else:            
                mydict[x] = 1

    that_sorted = dict(sorted(mydict.items()))
    print(that_sorted)
    print("total consonants", len(that_sorted))
    
consonant_sorted()
