def contarprod(prods):
	numprods = sum(prods.values())
	return numprods
def maisvendido(prods):	
	ref = max(prods, key = prods.get)
	return ref
prods = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
print(f"Quantidade de vendas: {contarprod(prods)}\nProduto mais vendido: {maisvendido(prods)}")

