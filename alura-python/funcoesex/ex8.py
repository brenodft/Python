def format(nome,sobrenome):
	nomeCompleto = []
	for i in range(len(nome)):
		nomeCompleto.append(nome[i].capitalize() + " "  +  sobrenome[i].capitalize())
	return nomeCompleto

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

print(format(nomes,sobrenomes))

