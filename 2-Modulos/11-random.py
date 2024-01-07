import random

#1 - Seleciona o valor aleatorio de uma lista

list1 = [1,7,9,2,4,6]
print(random.choice(list1))

#2- Gera um numero aleatorio em um intervalo de valores

print(random.randint(2,6))

#3 - escolhe caractere aleatorio de uma string

string = "oi tudo bem"
print(random.choice(string))  

#4 - Seleciona mais de um valor aleatorio

print(random.sample(list1,3))