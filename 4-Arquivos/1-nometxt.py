

"""
A opção w é para escrever no arquivo, se o arquivo não existir ele cria um novo
A opção a é para adicionar no arquivo, se o arquivo não existir ele cria um novo
A opção r é para ler o arquivo, se o arquivo não existir ele da erro

"""



with open ("nome.txt", "r", encoding= 'utf-8') as file:
    for line in file:
        print(line.rstrip())