def designvencedor(designs):
	vencedor = max(designs, key = designs.get)
	return vencedor
def percvencedor(designs):
	maiorvalor = designs[designvencedor(designs)]
	perc = 100*maiorvalor/sum(designs.values())
	return perc
designs = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210,'Design 5': 1811}
print(f"Design vencedor: {designvencedor(designs)}\nPorcentagem de votos: {percvencedor(designs)}")
