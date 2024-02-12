def aprovado(lista):
	maior = max(lista)
	menor = min(lista)
	media = sum(lista)/len(lista)
	if media >= 6:
		situacao = "Aprovado(a)"
	else:
		situacao = "Reprovado(a)"
	return maior,menor,media,situacao
notas = []
for i in range(4):
	nota = float(input())
	notas.append(nota)
maior,menor,media,situacao = aprovado(notas)
print(maior,menor,media,situacao)

