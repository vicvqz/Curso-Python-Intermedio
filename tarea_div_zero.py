try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    resultado = numero1 / numero2

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

except ValueError:
    print("Error: debe ingresar números válidos.")