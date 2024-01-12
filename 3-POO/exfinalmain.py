from exfinal import Contact,ContactBook
import os

contatos = ContactBook()
acabou = False
while acabou == False:
    os.system("clear")
    print("###MENU PRINCIPAL###\n1- Adicionar um contato\n2- Ver todos os contatos\n3- Procurar um contato\n4- Remover um contato\n5- Sair do programa")
    opcao = int(input("Digite uma opção: "))
    os.system("clear")
    if opcao == 1:
        contatos.addcontact()
    elif opcao == 2:
        contatos.listcontacts()
        input("")
    elif opcao == 3:
        contatos.searchcontacts()
        input("")
    elif opcao == 4:
        contatos.removecontacts()
    elif opcao == 5:
        acabou = True