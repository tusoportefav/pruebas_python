import random

def select_user():
    while True:
        select = input("Escribe piedra, papel, tijera o salir para terminar: ").strip().lower()
        if select in ["piedra","papel","tijera","salir"]:
            return select
        else:
            print("Entrada no valida, por favor intenta de nuevo.")

def determine_winner(user,pc):
    if user == pc:
        return "dead heat"
    elif (user == "piedra" and pc == "tijera") or\
    (user == "papel" and pc == "piedra") or\
    (user == "tijera" and pc == "papel"):
        return "user"
    else:
        return "pc"
    
def game():
    optionts = ["piedra", "papel", "tijera"]
    victory = 0
    defeat = 0
    dead_heat = 0

    while True:
        user = select_user()
        if user == "salir":
            break
        cp = random.choice(optionts)
        print(f"La computadora elijio: {cp}")

        total = determine_winner(user,cp)

        if total == "dead heat":
            print("Esto es un empate")
            dead_heat += 1
        elif total == "user":
            print("Has ganado,¡Felicidades!")
            victory += 1
        else:
            print("Has perdido, :c")
            defeat +=1
        
    print("\n===Resultados Finales===")
    print(f"Victorias = {victory}")
    print(f"Derrotas = {defeat}")
    print(f"Empates = {dead_heat}")

game()
