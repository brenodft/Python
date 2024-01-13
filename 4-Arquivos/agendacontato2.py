from exagendacontato import adicionar_contato, listar_contatos, remover_contato
import csv

finalizar = False
while finalizar != True:
    print("#Menu de Contatos#")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("0 - Sair")
    print("###################")
    opcao = int(input("Digite uma opção: "))


    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = int(input("Digite o telefone do contato: "))
        adicionar_contato(nome, telefone)
    elif opcao == 2:
        listar_contatos()
    elif opcao == 3:
        nome = input("Digite o nome do contato: ")
        remover_contato(nome)
    elif opcao == 0:
        finalizar = True


