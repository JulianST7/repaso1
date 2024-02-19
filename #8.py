#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir(lista):
    lista_inv = lista[::-1]
    return lista_inv

lista_normal = ["hola","que","bueno","chao"]
listan_inv = invertir(lista_normal)
print(f"Lista sin invertir {lista_normal}")
print(f"Lista invertida {listan_inv}")