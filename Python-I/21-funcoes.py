def welcome():
    print("Hello World")

welcome()

def sum():
    return 5+4

print(sum())

#4- função para cadastrar um jogo

def create_game():
    name = input("Digite o nome do jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    planIncluded = input("Está incluso no serviço mensal?\n")

    print(f"{name} - R$ {gamePrice}")

create_game()
create_game()