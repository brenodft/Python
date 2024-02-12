def notamanobra(lista):
	maior = lista.index(max(lista))
	menor = lista.index(min(lista))
	lista.pop(maior)
	lista.pop(menor)
	return sum(lista)/len(lista)
notas = []
for i in range(5):
	nota = float(input())
	notas.append(nota)
print(notamanobra(notas))
