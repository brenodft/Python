def calcula_pontos(marcados,sofridos):
	pontos = 0
	pontosTotais = 3*len(marcados)
	for i in range(len(marcados)):
		if marcados[i] > sofridos[i]:
			pontos += 3
		elif marcados[i] == sofridos[i]:
			pontos += 1
		else:
			pontos += 0
	return pontos,100*pontos/pontosTotais
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
pontos,aprov = calcula_pontos(gols_marcados,gols_sofridos)
print(f"O time fez {pontos} pontos e teve {aprov} de aproveitamento")

