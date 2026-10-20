"""
Práctica 2 - Operador ternario y *args
Cada ejercicio es una función; el menú del final permite probarlos por teclado.
"""


# 1) Mayor de dos números con operador ternario
def mayor_de_dos(a, b):
    return a if a >= b else b


# 2) Buscar una palabra en una lista usando *args y operador ternario
def buscar_palabra(palabra, *args):
    encontrada = palabra.lower() in (p.lower() for p in args)
    return f"'{palabra}' SÍ está en la lista" if encontrada else f"'{palabra}' NO está en la lista"


# 3) Par o impar (también con ternario, para mantener el estilo)
def par_o_impar(n):
    return "par" if n % 2 == 0 else "impar"


# 4) Promedio de una lista de números usando *args y operador ternario
#    El ternario evita la división por cero si no se pasan números.
def promedio(*args):
    return sum(args) / len(args) if args else 0


# 5) Mensaje de error si no se pasan suficientes argumentos
def sumar_minimo_dos(*args, minimo=2):
    if len(args) < minimo:
        print(f"Error: se necesitan al menos {minimo} argumentos y se recibieron {len(args)}.")
        return None
    return sum(args)


# ----------------- Entrada por teclado -----------------
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Valor inválido, ingresá un número.")


def pedir_lista_numeros(mensaje):
    while True:
        texto = input(mensaje).replace(",", " ").split()
        try:
            return [float(x) for x in texto]
        except ValueError:
            print("Hay valores que no son números, probá de nuevo.")


def menu():
    opciones = """
--- PRÁCTICA 2 ---
1. Mayor de dos números
2. Buscar una palabra en una lista
3. Par o impar
4. Promedio de una lista de números
5. Validar cantidad de argumentos
0. Salir
"""
    while True:
        print(opciones)
        op = input("Elegí una opción: ").strip()

        if op == "1":
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")
            print(f"El mayor es: {mayor_de_dos(a, b)}")

        elif op == "2":
            palabras = input("Ingresá palabras separadas por espacio: ").split()
            palabra = input("Palabra a buscar: ").strip()
            print(buscar_palabra(palabra, *palabras))

        elif op == "3":
            n = int(pedir_numero("Número entero: "))
            print(f"{n} es {par_o_impar(n)}")

        elif op == "4":
            numeros = pedir_lista_numeros("Números separados por espacio: ")
            resultado = promedio(*numeros)
            print(f"Promedio: {resultado:.2f}" if numeros else "No ingresaste números.")

        elif op == "5":
            numeros = pedir_lista_numeros("Números a sumar (mínimo 2): ")
            resultado = sumar_minimo_dos(*numeros)
            if resultado is not None:
                print(f"Suma: {resultado}")

        elif op == "0":
            print("¡Chau!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()