gamesSet = {"Fifa 23", "Red Dead 2", "Star Wars", "Zelda", "Mario Odyssey", "Resident Evil 4"}

print(gamesSet)

#1- buscar o tamanho do set
print(len(gamesSet))

#2- True e 1 são considerados o mesmo valor
exampleset = {"Fifa 23",True,1,90.50}
print(exampleset)

#3 Adicionar item de outro set
gamesSet.update(exampleset)
print(gamesSet)

#4 Remover item do set
gamesSet.remove(True)
gamesSet.remove(90.5)
print(gamesSet)

#nao pode repetir valores
#nao possibilita recuperar valores via slice(fatiamento)
