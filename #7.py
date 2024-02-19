#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def econtrar(lista):
    grande = lista[0]
    pequeño = lista[0]
    for num in lista:
        if num > grande:
            grande = num
        elif num < pequeño:
            pequeño = num
    return grande, pequeño

listan = [1,2,9,0,30]
grande, pequeño = econtrar(listan)
print(f"El numero mas grande es : {grande}")
print(f"El numero mas pequeño es : {pequeño}")