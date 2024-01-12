class Employee:
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario 

    def show(self):
        print(f"Nome: {self.nome}, Salario: {self.__salario}")

    def get_salary(self):
        return self._salary
    
    #Método para modificar atributo privado
    def set_salary(self,salary):
        self.salary = salary