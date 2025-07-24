import random 

def play_guess():

    while True:
        print("\nElige la dificultad")
        print("1. Facil 1 - 10")
        print("2. Intermedio 1 - 30")
        print("3. ProPLayer 1 - 50")
        print("4. Salir")

        select_level = input("\nElige el nivel (1, 2, 3,) o 4 para finalizar: ")

        if select_level.isdigit():
            select_level = int(select_level)

            if select_level == 4:
                print("Hasta Luego")
                return

            elif select_level == 1:
                level_range = 10
            elif select_level == 2:
                level_range = 30
            elif select_level == 3:
                level_range = 50
            else:
                print("Elige una entrada valida")
                continue
        else:
            print("Entrada no valida, ingrese 1, 2, 3: para elegir el nivel")
            continue
   
        number_secret = random.randint(1, level_range)
        attempts = 0
        limit_attempts = 5

        while attempts < limit_attempts:
        
            select = input(f"\nAdivina el numero secreto del 1 al {level_range}: ")
            if select.isdigit():
                select = int(select)
                attempts += 1

                if number_secret < select:
                    print ("El numero secreto es menor")
                elif number_secret > select:
                    print ("El numero secreto es mayor")
                else:
                    print(f"Intento {attempts} de {limit_attempts}")
                    print(f"Ganaste ({number_secret}) es el numero secreto ")
                    print(f"Lo lograste en {attempts} intento(s)")
               
                    break
            else:
                print (f"Entrada no valida, solo puede ser un numero del 1 al {level_range}")
    
        else:
            print(f"Te quedaste sin limites de intentos. El numero secreto era {number_secret}")

play_guess()