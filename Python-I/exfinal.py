#vai ser uma lista de dicionarios emaranhados

listadejogadores = []
done = False

def listarTime(lista):
    for i,time in enumerate(lista):
        print(f"{i} - {time["nomeTime"]} - Jogadores: {time["jogadores"]}")

def addTime(lista):
    nomeTime = input("Digite o nome do time\n")
    for time in lista:
        if nomeTime == time["nomeTime"]:
            print("O time ja existe")
            return 
        
    nomeTime = {
        "nomeTime": nomeTime,
        "jogadores": []
    }
    lista.append(nomeTime)
    print("Time adicionado com sucesso!")

def removerTime(lista): 
    listarTime(lista)
    index = int(input("Digite o indice do time a ser removido \n "))
    if 0 <= index < len(lista):
        time_removido = lista.pop(index)
        print(f"Time {time_removido["nomeTime"]} removido com sucesso!")
    else:
        print("Indice Inválido!")

def addJogador(lista):
    jogador = input("Digite o nome do jogador\n")
    print("\n")
    listarTime(lista)
    index = int(input("\nDigite o indice do time do qual esse jogador jogará\n"))
    if 0 <= index < len(lista):
        lista[index]["jogadores"].append(jogador)
        print(f"O jogador {jogador} foi para o time {lista[index]["nomeTime"]}")


def removeJogador(lista):
    listarTime(lista)
    index = (int(input("\nQual o indice do time que o jogador a ser removido joga?\n")))
    if 0 <= index <len(lista):
        nomeJogador = input("Digite o nome do jogador a ser removido\n")
        if nomeJogador in lista[index]["jogadores"]:
            lista[index]["jogadores"].remove(nomeJogador)
            print(f"O jogador {nomeJogador} foi removido com sucesso do time {lista[index]["nomeTime"]}")
        else:
            print(f"O jogador {nomeJogador} não joga no time {lista[index]["nomeTime"]}")

    else:
        print("Indice invalido")

def listarJogadores(lista):
    listarTime(lista)
    index = (int(input("Qual o indice do time que você deseja realizar a consulta de jogadores?\n")))
    if 0 <= index <len(lista):
        print(f"{lista[index]["jogadores"]}")
    else:
        print("Indice invalido")

while not done:

    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")

    choice = input("> ")

    if choice == "1":
        addTime(listadejogadores)
        pass
    elif choice == "2":
        removerTime(listadejogadores)
        pass
    elif choice == "3":
        listarTime(listadejogadores)
        pass
    elif choice == "4":
        addJogador(listadejogadores)
        pass
    elif choice == "5":
        removeJogador(listadejogadores)
        pass
    elif choice == "6":
        listarJogadores(listadejogadores)
        pass
    elif choice == "7":
        done = True
        pass

