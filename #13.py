#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("ingrese segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
if n2 != 0:
    division = n1 / n2
else:
    division = "No se puede dividir entre cero"
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multi)
print("Division:", division)