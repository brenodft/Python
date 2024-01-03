distancia = int(input("Qual distancia você deseja percorrer (em km)?\n"))

if distancia < 200:
    preco = 0.50*distancia
else:
    preco = 0.35*distancia