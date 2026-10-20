from .cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    TASA = 0.001  # 0.1 %

    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: monto inválido.")
            return False
        if monto > self.saldo:
            print(f"[{self.titular}] Extracción de ${monto:.2f} rechazada: saldo insuficiente "
                  f"(${self.saldo:.2f}).")
            return False
        self.saldo -= monto
        print(f"[{self.titular}] Extracción de ${monto:.2f} OK. Saldo: ${self.saldo:.2f}")
        return True

    def aplicar_interes(self):
        interes = self.saldo * self.TASA
        self.saldo += interes
        print(f"[{self.titular}] Interés aplicado: ${interes:.2f}. Saldo: ${self.saldo:.2f}")
        return interes