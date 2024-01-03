num1 = int(input("Digite o primeiro operador: "))
num2 = int(input("Digite o segundo operador: "))

#Aritmeticos
sum = num1+num2
sub = num1-num2
div = num1/num2
mult = num1*num2
mod = num1%num2
exp = num1**num2

print(f"O resto da divisão entre {num1} e {num2} é: {mod}")
print(f"{num1} elevado a {num2} é igual a {exp}")

#Comparação

bigger = num1 > num2
smaller = num1<num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1>= num2
smallerEqual = num1<=num2

print(f"Os numeros {num1} e {num2} são iguais? {equal}")
print(f"O numero {num1} é maior ou igual a {num2}? {biggerEqual}")


