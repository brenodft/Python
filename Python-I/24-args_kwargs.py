"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.
- Ponteiro


**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
- Ponteiro de ponteiro
"""

#1 - Soma de Numeros

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma total: {sum_total}")


sum(7,8,9)
sum(7,8,9,10,11,12)
    
#2 - Apresentação de cursos

def presentation(**data):
    for key,value in data.items():
        print(f"{key} - {value}")

print("Dados do curso")
presentation(name= "Python",category = "BackEnd", level = "Iniciante")
presentation(name= "Visão Computacional com Python",category = "IA", level = "Avançado")
presentation(name= "Dashboards com Dash",category = "DataScience", level = "Intermediário")