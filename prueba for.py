#Escribe un código que imprima todos los números del 1 al 20 
#Y diga si cada uno es primo, par o impar. Usa el for y la función es_primo() que ya vimos antes.

"""
def mostrar_residuos(number):
    print(f"Probando divisores para {number}:")
    for prime in range(2, number):
        residuo = number % prime
        print(f"{number} % {prime} = {residuo}")
        if residuo == 0:
            print(f"-> {number} es divisible por {prime}, por lo tanto NO es primo.\n")
            return
    print(f"-> {number} NO es divisible por ningún número entre 2 y {number-1}, por eso ES primo.\n")

# Prueba con algunos números
mostrar_residuos(7)
mostrar_residuos(10)
"""

def prime_number(number):
    if  number < 2:
        return False
    
    for prime in range(2, number):
        if number % prime == 0:
            return False
    return True

for num in range(2,102):
    if prime_number(num):
        print (f"{num} es primo")

"""
def is_prime(number):
    for xx in range(2,number):
        if number % xx == 0:
            return False
    return True

def number_classification(x,y):
    prime = []
    even = []
    odd = []

    for yy in range(x, y + 1):
        if is_prime(yy):
            prime.append(yy)
        if yy % 2 == 0:
            even.append(yy)
        else:
            odd.append(yy)
    return prime, even, odd

prime, even, odd = number_classification(2, 20)

print(f"{prime} Son Primos")
print(f"{even} Son Pares")
print(f"{odd} Son Impares")

"""




















