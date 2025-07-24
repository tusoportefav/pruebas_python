friends = []

friends.append ("Mauricio")
friends.append ("Rick")
friends.append ("Damian")
friends.append ("Tip")

print("mis panas son" ,friends)

for hello in friends:
    print(f"Hola, {hello} ¿Como estas?")

#Sin ayuda del editor para ver operaciones 
for hello2 in friends:               
    if hello2.startswith("M"):
        print(f"Bienvenido {hello2}. ¡Bienvenido!, eres VIP")
    else:
        print(f"Hola {hello2}, pase por favor")

#Con ayuda del editor para ver operaciones 
friends2 = ["Mauricio", "Rick", "Damnian", "Tip"]

for hello3 in friends2:
    if hello3.startswith("M"):
        print(f"Bienvenido {hello3}. ¡Bienvenido!, eres VIP")
    else:
        print(f"Hola {hello3}, pase por favor")

"""
friends_list: list[str] = []

friends_list.append("Mauricio")
friends_list.append("Tip")
friends_list.append("Rick")
friends_list.append("Damian")

def greeting(friends_list: list[str]):
    for greet in friends_list:
        if greet.startswith("M"):
            print(f"\nHola {greet}. Eres VIP")
        else:
            print(f"Hola {greet}")
    user = input("Escribe un nombre para la lista: ")
    friends_list.append(user)

    print("\nLista Actualizada")
    for great in friends_list:
        print(f"Hola {great}")

greeting(friends_list)
    
"""
friends3 : list[str] = []

def friends_list(f: list[str]):
    while True:
        user = input("Escribe un =Nombre= para tu lista o =Salir= para finalizar: ")
        if user.lower() == "salir":
            break
        else:
            f.append(user)
    for list_f in f:
        if list_f.lower().startswith("m"):
            print(f"Felicidades {list_f} tienes acceso VIP")
        else:
            print(f"{list_f} tienes acceso")

friends_list(friends3)