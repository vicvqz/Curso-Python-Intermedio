from .cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        # El límite se define ANTES de llamar al padre, porque el setter de saldo lo usa.
        self.limite_descubierto = limite_descubierto
        super().__init__(titular, cbu, saldo_inicial)

    def _saldo_minimo(self):
        # La cuenta corriente puede quedar en negativo hasta el límite de descubierto.
        return -self.limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: monto inválido.")
            return False
        disponible = self.saldo + self.limite_descubierto
        if monto > disponible:
            print(f"[{self.titular}] Extracción de ${monto:.2f} rechazada: supera saldo + descubierto "
                  f"(${disponible:.2f}).")
            return False
        self.saldo -= monto
        print(f"[{self.titular}] Extracción de ${monto:.2f} OK. Saldo: ${self.saldo:.2f}")
        return True
