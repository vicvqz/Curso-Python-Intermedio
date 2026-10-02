try:
    archivo = open("archivo_prueba.txt", "r")
    print(archivo.read())
    archivo.close()

except FileNotFoundError:
    print("El archivo no existe. Se creará uno nuevo.")

    archivo = open("archivo_prueba.txt", "w")
    archivo.write("Archivo creado correctamente.")
    archivo.close()