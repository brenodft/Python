gamesTuple = ("Fifa 23","Red Dead 2", "Mario Odyssey", "The Legend of Zelda")
print(gamesTuple)
print(type(gamesTuple))

#Nao possibilita adicionar valores
#Nao possibilita remover valores
#Nao possibilita ordenar valores
#Nao pode repetir valores

#buscar 2 primeiros itens
print(gamesTuple[:2])
#buscar ultimo item
print(gamesTuple[-1])
#buscar jogos até uma determinada posicao
print(gamesTuple[:3])
#buscar jogos de uma posição em diante
print(gamesTuple[2:])
#recuperar um item pelo indice
print(gamesTuple.index("Red Dead 2"))