def multiplos3(lista):
	m3 = []
	for num in lista:
		if num%3 == 0:
			m3.append(num)
	return m3
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
print(multiplos3(lista))
