from .cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: monto inválido.")
            return False
        total = monto + self.costo_emision
        if total > self.saldo:
            print(f"[{self.titular}] Extracción de ${monto:.2f} + comisión ${self.costo_emision:.2f} "
                  f"rechazada: saldo insuficiente (${self.saldo:.2f}).")
            return False
        self.saldo -= total
        print(f"[{self.titular}] Extracción de ${monto:.2f} + comisión ${self.costo_emision:.2f} OK. "
              f"Saldo: ${self.saldo:.2f}")
        return True