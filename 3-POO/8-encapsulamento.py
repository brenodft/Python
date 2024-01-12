class Employee:
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario 

    def show(self):
        print(f"Nome: {self.nome}, Salario: {self.__salario}")

