import os

def addproduct(lista):
    prod = input("Digite o nome do produto: ")
    lista.append(prod)
    return lista

def listproduct(lista):
    print("Lista de produtos:\n")
    for i,produto in enumerate(lista):
        print(f"{i}, Produto: {produto}")
    
def removeproduct(lista):
    listproduct(lista)
    try:
        prod = int(input("Digite o indice do produto a ser removido: "))
        lista.pop(prod)
    except:
        print("Indice invalido!")
        input("")

lista = []
feito = False

while feito != True:
    print("1- Adicionar produto\n2- Listar produtos\n3- Remover produto\n0- Sair")
    try:
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            os.system("clear")
            addproduct(lista)
        elif op == 2:
            os.system("clear")
            listproduct(lista)
        elif op == 3:
            os.system("clear")
            removeproduct(lista)
            os.system("clear")
        elif op == 0:
            os.system("clear")
            feito = True
        else:
            os.system("cls")
            print("Opção inválida!")
    except:
        print("Opção inválida!")
        input("")