gameslist = ["Resident Evil 4 ", "Star Wars Jedi Survivor", "The Legend of Zelda", "Red Dead 2", "Mario Odyssey"]

#1 tamanho da lista

print(len(gameslist))

#2 recuperar um item da lista pelo indice
print(gameslist.index("Mario Odyssey"))

#3 adicionar item no final da lista
gameslist.append("GTA V")
print(gameslist)

#4 ordenar a list
gameslist.sort()
print(gameslist)

#5 copiar os itens de uma lista para outra
gameReset = gameslist.copy()
gameReset.remove("Star Wars Jedi Survivor")
print(gameReset)

#6 remove todos os itens da lista
gameslist.clear()
print(gameslist)

#Pode repetir valores