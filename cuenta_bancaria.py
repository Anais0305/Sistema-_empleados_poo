class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        pass
class CuentaAhorros(CuentaBancaria):
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def retirar(self, monto):
        if self.saldo - monto >= -self.limite:
            self.saldo -= monto
        else:
            print("Límite de sobregiro alcanzado")
cuenta1 = CuentaAhorros("Carlos", 1000)
cuenta2 = CuentaCorriente("Azumi", 500, 300)

cuentas = [cuenta1, cuenta2]

for cuenta in cuentas:
    cuenta.retirar(1200)
    print(f"{cuenta.titular} saldo: {cuenta.saldo}")
