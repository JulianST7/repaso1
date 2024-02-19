#Escribir una función que calcule la media aritmética de una lista de números

def calcular_media(lista):
  suma = sum(lista)
  num_elementos = len(lista)
  media = suma / num_elementos
  return media

lista_num = [8,2,7,9,3]
media_aritmetica = calcular_media(lista_num)
print(f"La media es: {media_aritmetica}")