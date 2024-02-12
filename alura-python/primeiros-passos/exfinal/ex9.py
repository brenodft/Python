def checarGabarito(respostas):
	count = 0
	i = 0
	gabarito = ['D','A','C','B','A','D','C','C','A','B']
	for resposta  in respostas:
		if resposta == gabarito[i]:	
			count = count+1
		i = i+1
	return count	
respostas = []
for i in range(10):
	resposta = input("Digite uma resposta: ")
	respostas.append(resposta)
print(f"Voce tirou: {checarGabarito(respostas)} pontos") 
