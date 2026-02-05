
class Empleado:
    def __init__(self, nombre, salario_base):
        self._nombre = nombre
        self._salario_base = salario_base

    def calcular_salario(self):
        return self._salario_base

    def mostrar_info(self):
        return f"{self._nombre} cobra {self.calcular_salario()}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario_base, horas):
        super().__init__(nombre, salario_base)
        self._horas = horas

    def calcular_salario(self):
        return self._salario_base * self._horas


empleado1 = Empleado("Ana", 2500)
empleado2 = EmpleadoPorHoras("Luis", 20, 120)

empleados = [empleado1, empleado2]

for emp in empleados:
    print(emp.mostrar_info())
