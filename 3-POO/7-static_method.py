"""
    1 - O metodod de classe não utiliza o parametro referente a classe
    2 - O metodo de classe pode acessar mas não modificar o estado da classe
    3 - Usamos o decorator @staticmethod para criar um metodo estatico
"""

class Course:
    def __init__(self,name,trail):
        self.name = name
        self.trail = trail


    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python","Módulos e PIP","Orientação a objetos"]
        elif trail == "Automação com Python":
            courses = ["Automação de tarefas","Web Scraping","Assistente virtual em Python"]
        else:
            courses = ["A definir"]
        return courses

print(Course.courses_trail("Python Fundamentos"))