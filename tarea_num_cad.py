numero = 250
texto = "dfhbvblññ--''"

try:
    resultado = numero + texto
    print(resultado)

except TypeError:
    print("Error: no se puede sumar un número con una cadena.")