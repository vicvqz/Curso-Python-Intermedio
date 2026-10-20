from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase base abstracta: no se puede instanciar directamente (Abstracción)."""

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular          # público
        self._cbu = cbu                 # protegido, solo lectura
        self.saldo = saldo_inicial      # pasa por el setter -> se valida desde el inicio

    # ---------- Encapsulamiento ----------
    @property
    def cbu(self):
        return self._cbu                # sin setter => solo lectura (AttributeError al asignar)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < self._saldo_minimo():
            raise ValueError(f"El saldo no puede ser menor a {self._saldo_minimo()}.")
        self._saldo = valor

    def _saldo_minimo(self):
        """Piso del saldo. Las subclases pueden redefinirlo (ver CuentaCorriente)."""
        return 0

    # ---------- Métodos concretos ----------
    def depositar(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Depósito rechazado: el monto debe ser mayor a 0.")
            return False
        self.saldo += monto
        print(f"[{self.titular}] Depósito de ${monto:.2f} realizado. Saldo: ${self.saldo:.2f}")
        return True

    def __str__(self):
        tipo = type(self).__name__
        return f"[{tipo}] Titular: {self.titular} | CBU: {self._cbu} | Saldo: ${self._saldo:.2f}"

    # ---------- Método abstracto ----------
    @abstractmethod
    def extraer(self, monto):
        pass
