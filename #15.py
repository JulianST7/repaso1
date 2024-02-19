#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no

def palindromo(cadena):
  cadena = cadena.lower().replace(" ", "")
  for i in range(len(cadena) // 2):
    if cadena[i] != cadena[-i - 1]:
      return False
  return True

cadena = input("Ingrese una cadena de texto: ")
if palindromo(cadena):
  print(f"La cadena '{cadena}' es un palíndromo")
else:
  print(f"La cadena '{cadena}' no es un palíndromo")