from math import sqrt
numeros = [2, 8, 15, 23, 91, 112, 256]
raizinteira = []
for i in numeros:
	if sqrt(i) % 1 == 0:
		raizinteira.append(i)
print(f"Numeros que possuem raiz inteira {raizinteira}") 
