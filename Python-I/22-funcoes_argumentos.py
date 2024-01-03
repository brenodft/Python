#1 Crie uma função que receba 2 argumentos 1nome 2 nome

def full_name(fname,lname):
        print(f"Nome completo {fname}{lname}")

full_name("Breno","Pires")

#2 funcsoma
def sum(a,b):
        return a+b

print(sum(2,4))

#funccountry
def address(country = "Brasil"):
        print(f"Eu moro no {country}")

address("Canadá")

#avaliação de um jogo
def rating_game(qtdRating):
        game_name = input("Digite o nome do jogo\n")
        sum = 0
        for i in range(qtdRating):
                note = float(input("Digite a nota do jogo\n"))
                sum+= note
        print(f"Media das notas = {sum/qtdRating}")

ratingnumber = int(input("Digite o numero de avaliações que você deseja fazer \n"))
rating_game(ratingnumber)