lista = {'doce': [], 'amargo': []}
id = 0
for i in range(10):
	id = int(input("Digite um id: "))
	if id % 2 == 0:
		lista['doce'].append(id)
	else:
		lista['amargo'].append(id)
print(f"Doces: {len(lista['doce'])} Amargos: {len(lista['amargo'])}")
