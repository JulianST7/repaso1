#Escribir una función que calcule el área de un círculo dado su radio.

import math

def area_circulo(radio):
    area = math.pi * radio **2
    return area

radio = 30
area_circulo = area_circulo(radio)
print(f" La area del circulo es = {area_circulo}")