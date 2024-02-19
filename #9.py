#Crear un programa que genere una matriz de números y la imprima en pantalla.

import random
def generarm(filas, columnas):
    
  matriz = []
  for i in range(filas):
    fila = []
    for j in range(columnas):
      num = random.randint(1, 100)
      fila.append(num)
    matriz.append(fila)
  return matriz

def imprimirm(matriz):
    
  for fila in matriz:
    for num in fila:
      print(f"{num:3}", end=" ")
    print()

filas = 4
columnas = 4
matriz = generarm(filas, columnas)
imprimirm(matriz)