#Intenta hacer un mini‑proyecto: por ejemplo, una calculadora que evalúe expresiones con ayuda de una stack.

def my_sum(a, b, c):
    if a + b == c:
        return c

print(my_sum(20, 20, c = 20 + 20))


def my_sustracion(a, b):
    return a - b
print(my_sustracion(40, 20))

def my_multiplication(a, b):
    return a * b
print(my_multiplication(20, 20))

def division(a, b):
    if  b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b
print(division(20, 2))






def get_squared_number(number):
    squared_number = []

    for n in number:
        squared_number.append(n*n)
    return squared_number

number = [2, 3, 4, 5, 6, 7, 8, 9]
print(get_squared_number(number))