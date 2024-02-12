def isprime(num):
	if num <= 1:
		return False
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

lista = []
total = int(input("Digite um numero: "))

for i in range(total):
	if (isprime(i)):
		lista.append(i)

for dado in lista:
	print(dado)
