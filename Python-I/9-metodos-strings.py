gameName = "Fifa23"
gamedescription = '''
    Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports, 
    que possibilita jogar localmente ou online.
'''

print(gameName.upper()) #String Maiuscula
print(gameName.lower()) #String Minuscula
print(gameName.capitalize()) #Apenas a primeira letra em maiusculo
print(gameName.title) #Apenas a primeira letra em maiusculo
print(gameName.center(10, "-")) #Retorna a string centralizada por caractere de preenchimento
print(gameName.find("a")) #Retorna a posicao de um determinado caractere
print(gamedescription.count("f")) #Conta caracteres
print(gamedescription.replace("Fifa", "Pes")) #Altera um elemento por outro
print(gamedescription.split(","))