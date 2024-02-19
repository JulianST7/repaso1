#. Escribir una función que calcule el factorial de un número dado.

def factorial(num):
    if num == 0 or num == 1:
     return 1
    else:
     return num * factorial(num - 1)

num = 10
factorial_num = factorial(num)
print(f"El factorial de {num} es: {factorial_num}")
