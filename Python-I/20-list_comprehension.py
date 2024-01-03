# 1 - Liste valores de 0 a 10 que sejam menor que 4
# for i in range(10):
#     if i<4:
#         print(i)    
listNumbers = [i for i in range(10) if i<4]
print(listNumbers)

gamesList = ["Mario Odyssey", "Dk Country", "Kirby", "Luigis Mansion"]

#jogos q possuem a letra a
newlist = [x for x in gamesList if "a" in x]
print(newlist)

#jogos que eu zerei
gamesFinished = [x for x in gamesList if x!= "Kirby"]
print(gamesFinished)