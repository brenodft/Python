def lerNlinhas(arquivo, n):
    with open(f'{arquivo}', 'r', encoding = 'utf-8') as file:
        for i in range(n):
            print(file.readline().rstrip())


def main():
    num = int(input('Digite o numero de linhas que deseja ler: '))
    arquivo = input('Digite o nome do arquivo: ')
    lerNlinhas(arquivo, num)

main()

