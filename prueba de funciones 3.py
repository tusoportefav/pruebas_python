def atm():
    balance = 1000
    while True:
        print("\nMenu ATM")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
        option = input("Elige una opcion del 1-4: ")

        if option == "1":
            print(F"\nTu saldo actual es de {balance}")

        elif option == "2":
            deposit = input("\n¿Cuanto dinero quieres depositar?: ")
            if deposit.isdigit():
                deposit = int(deposit)
                balance += deposit
                print(f"Tienes un saldo actual: {balance}")
            else:
                print("Entrada no valida")
        
        elif option == "3":
            withdrawal = input("\n¿Cuanto dinero quieres retirar?: ")
            if withdrawal.isdigit():
                withdrawal = int(withdrawal)
                if withdrawal <= balance:
                    balance -= withdrawal
                    print(f"Retiro exitoso. Tu saldo actual es de {balance}")
                else:
                    print("Fondos Insuficientes")
            else:
                print("Entrada no valida")
        
        elif option == "4":
            print("\nGracias por usar el ATM. ¡Hasta luego!")
            break

        else:
            print("Opcion no valida")
atm()