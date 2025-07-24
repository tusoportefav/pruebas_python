def password_hard(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    symbol = "@!#$%&"

    for char in password:
        if char.isupper:
            return True
        elif char.islower:
            return True
        elif char.isdigit:
            return True
        elif char in symbol:
            return True
        
    return has_upper and has_lower and has_digit and has_symbol, 


while True:
    user = input("Escribe la contraseña: ")

    if password_hard(user):
        print("contraseña fuerte")
        break
    else:
        print("contraseña debil")

