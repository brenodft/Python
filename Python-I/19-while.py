gameName = input("Digite o nome do jogo\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

#Escrever codigo em que pega as notas do jogo e para de pedir quando rating for diferente de -1

while(rating != -1):
    rating = float(input("Digite uma nota para o jogo\n"))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating/qtdRating
print(f"A media das notas do jogo {gameName} é igual a {average:.2f}")