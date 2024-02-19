# Crear una función que convierta grados Fahrenheit a grados Celsius.

def convertir(Fahrenheit):
    celsius = (Fahrenheit -32  )*5/9
    return celsius

gfahrenheit = 40
gcelsius = convertir(gfahrenheit)
print(f"{gfahrenheit}Grados fahrenheit son {gcelsius} grados celsius ")