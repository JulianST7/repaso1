#Crear un programa que genere una lista de números pares entre 1 y 100.

def generar_pares():
  listap = []
  for num in range(1, 101):
    if num % 2 == 0:
      listap.append(num)
  return listap

listap = generar_pares()
print(f"Lista de números pares entre 1 y 100: {listap}")
