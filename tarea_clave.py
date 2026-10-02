persona = {
    "nombre": "Lucía",
    "edad": 25
}

try:
    print(persona["dni"])

except KeyError:
    print("Error: la clave no existe en el diccionario.")