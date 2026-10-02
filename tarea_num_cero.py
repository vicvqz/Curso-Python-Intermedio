numero1 = 10
numero2 = 0

try:
    resultado = numero1 / numero2
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")