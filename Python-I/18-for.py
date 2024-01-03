gameList = ["Fifa","God of War","Red Dead 2","Uncharted"]
for game in gameList:
    print(game)

for game in gameList:
    if game == "Red Dead 2":
        break
    print(game)

for game in gameList:
    if game == "Red Dead 2":
        continue
    print(game)

gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite o numero de avaliações do jogo\n"))
    
sum = 0

for i in range(gameRating):
    note = float(input("Digite uma nota para o jogo\n"))
    sum += note

print(f"Media de avaliação do jogo {gameName} é: {sum/gameRating}")